#!/usr/bin/python

## Converts Huawei P30 Pro (and presumably other phone's) panoramic images to multiple square 1080x1080 images for use on Instagram as a pseudo-panorama
## To use this you'll need to have Python and then install ImageMagick and Wand
## Imagemagick: https://imagemagick.org/script/download.php
## Wand: pip install wand
# On Android:
#  * Install [Termux](https://termux.com/)
#  * pkg install imagemagick
#  * pip intall wand
# 
# Want to use it as a Windows Executable instead of installing Python etc every time?
# pip install auto-py-to-exe
# auto-py-to-exe
#   * Select the py file
#   * Choose "Single File" output.

from wand.image import Image
from wand.display import display
import math
import sys

if len(sys.argv) != 2:
    sys.exit("gimme a panoramic image filename")

with Image(filename=sys.argv[1]) as img:
    img.rotate(-90)
    img.transform(resize='x1080')
    overhang = img.width % 1080
    leftc = math.floor(overhang/2)
    rightc = img.width - math.ceil(overhang/2)
    img.crop(left=leftc, right=rightc)
    k=0
    for j in range(0,img.width,1080):
        with img[j:j+1080, 0:1080] as cropped:
            cropped.rotate(90)
            cropped.format = 'jpeg'
            rootfilename = '.'.join(sys.argv[1].rsplit(".")[:-1])
            splitfilename = rootfilename + "_pano_" + str(k) + '.jpg'
            print(splitfilename)
            cropped.save(filename=splitfilename)
            k +=1

