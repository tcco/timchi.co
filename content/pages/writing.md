title = "Writing"
order = 3
load_template = 1
+++++

<html>
  <head>
    <link rel="stylesheet" type="text/css" href="../css/writing.css" />
    <meta charset="utf-8">
  </head> 
  <body>
    <ul>
      {% for post in content.posts %}
        <div style="display:flex; flex-direction:row;">
            {% if post.preview_image %}
            <img src="{{ post.preview_image }}" alt="{{ post.preview_image_name }}" style="width: 50%; margin-right: 10px">
            {% endif %}
            <article>
               timco <br>
               {{ post.date.date() }}
              <a href="{{ post.url }}" style="text-decoration: none; color: black" onmouseover="this.style.color='lightblue';" onmouseout="this.style.color='black';" >
                <h2>{{ post.title }}</h2>
                <p>{{ post.preview }}</p>
              </a>
            <hr style="border: none; background-color: rgba(128, 128, 128, 0.5); height: 1px; margin-bottom: 1em;">
            </article>
        </div>
      {% endfor %}
    </ul>
  </body>
</html>
