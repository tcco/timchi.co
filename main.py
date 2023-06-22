import markdown, jinja2, toml, re
import os, glob, pathlib, distutils.dir_util
import inflect
import json


def load_config(config_filename):

  with open(config_filename, 'r') as config_file:
    config = toml.loads(config_file.read())

  ie = inflect.engine()
  for content_type in config["types"]:
    config[content_type]["plural"] = ie.plural(content_type)

  return config


def load_content_items(config, content_directory):

  def load_content_type(content_type):
    items = []
    for fn in glob.glob(
        f"{content_directory}/{config[content_type]['plural']}/*.md"):
      with open(fn, 'r') as file:
        frontmatter, content = re.split("^\+\+\+\+\+$", file.read(), 1,
                                        re.MULTILINE)

      item = toml.loads(frontmatter)
      item['content'] = markdown.markdown(content)
      item['slug'] = os.path.splitext(os.path.basename(file.name))[0]
      if config[content_type]["dateInURL"]:
        item[
          'url'] = f"/{item['date'].year}/{item['date'].month:0>2}/{item['date'].day:0>2}/{item['slug']}/"
      else:
        item['url'] = f"/{item['slug']}/"

      items.append(item)

    # sort according to config
    items.sort(key=lambda x: x[config[content_type]["sortBy"]],
               reverse=config[content_type]["sortReverse"])

    return items

  content_types = {}
  for content_type in config["types"]:
    content_types[config[content_type]['plural']] = load_content_type(
      content_type)

  return content_types


def load_templates(template_directory):
  file_system_loader = jinja2.FileSystemLoader(template_directory)
  return jinja2.Environment(loader=file_system_loader)


def render_site(config, content, environment, output_directory):

  def render_type(content_type):  # <-- new inner function
    # Post pages
    template = environment.get_template(f"{content_type}.html")
    for item in content[config[content_type]["plural"]]:
      path = f"public/{item['url']}"
      pathlib.Path(path).mkdir(parents=True, exist_ok=True)
      with open(path + "index.html", 'w') as file:
        file.write(template.render(this=item, config=config, content=content))

  if os.path.exists(output_directory):
    distutils.dir_util.remove_tree(output_directory)
  os.mkdir(output_directory)

  for content_type in config["types"]:  # <-- new for loop
    render_type(content_type)

  # Homepage
  index_template = environment.get_template("index.html")
  with open(f"{output_directory}/index.html", 'w') as file:
    file.write(index_template.render(config=config, content=content))

  # Static files
  distutils.dir_util.copy_tree("static", output_directory)


def list_files(startpath):
  for root, dirs, files in os.walk(startpath):
    level = root.replace(startpath, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for f in files:
      print(f"{subindent}{f}")


def main():

  config = load_config("config.toml")
  print(json.dumps(config, indent=2))
  content = load_content_items(config, "content")
  environment = load_templates("layout")
  output_dir = "public"
  render_site(config, content, environment, output_dir)
  list_files(output_dir)


main()
