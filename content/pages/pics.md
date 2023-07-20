title = "Pics"
order = 4
load_template = 1
gallery_locations = ["pics"]
+++++

<!-- refered to
https://timnwells.medium.com/create-a-simple-responsive-image-gallery-with-html-and-css-fcb973f595ea -->


<!DOCTYPE html>
<html lang="en">
 <head>
  <!-- <link rel="stylesheet" type="text/css" href="/css/pics.css" />
  <meta charset="utf-8">   -->
  <title>Image Gallery</title>
  <meta name="description" content="Responsive Image Gallery">
  <meta name="author" content="Tim Co">
</head>

{% import "macros.html" as macros %}
{{ macros.gallery(this.gallery.pics) }}
</html>