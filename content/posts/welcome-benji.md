title = "Welcome Benji!"
date = 2020-11-03T11:47:00+02:00
preview_image = "../assets/dogs/benji.jpg"
preview_image_name = "Benji"
preview = "Another Aussie has entered the building! This lil guy has kept us sane (and insane at the same time) ..."

load_template = 1
gallery_locations = ["dogs/benji"]

tags = ["Daily"]
+++++
{% import "macros.html" as macros %}

Another Aussie has entered the building! This lil guy has kept us sane (and insane at the same time) 

{{ macros.post_gallery(this.gallery.dogs_benji) }}