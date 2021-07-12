# pano2insta - Panorama to Instagram

LICENSE: Apache-2.0

Copyright Conor O'Neill 2021, conor@conoroneill.com

Converts Huawei P30 Pro (and presumably other phone) panoramic images to multiple square 1080x1080 images for use on Instagram as a pseudo-panorama

## Usage on Windows, Linux, OSX, etc

To use this you'll need Python and then install ImageMagick and Wand

* Imagemagick: https://imagemagick.org/script/download.php
* Wand: `pip install wand`

## Windows Executable

Want to use it as a Windows Executable instead of installing Python etc every time?

* `pip install auto-py-to-exe`
* `auto-py-to-exe`

* Select the py file
* Choose "Single File" output.

## Usage on Android
* Install [Termux](https://termux.com/)
* `pkg install imagemagick`
* `pip install wand`

## Notes
* Imagemagick incorrectly recognises the orientation of the panoramic images from my Huawei P30 Pro. It thinks they are long and narrow. Hence the use of the -90 and 90 rotations in the code. If it gets it right for your phone, simply comment out the two rotate lines in the code.
* [Blogpost](https://conoroneill.net/2021/07/12/pano2insta-panoramic-photo-to-instagram-converter/) about the tool.

## TO-DO
* Handle images wider than 10800 (the maximum on Instagram via 10 x 1080)
* Proper error handling

