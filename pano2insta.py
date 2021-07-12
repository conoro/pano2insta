#!/usr/bin/python

# pano2insta - Panorama to Instagram
# Copyright Conor O'Neill 2021, conor@conoroneill.com

from wand.image import Image
from wand.display import display
import math
import sys

if len(sys.argv) != 2:
    sys.exit("gimme a panoramic image filename")

with Image(filename=sys.argv[1]) as img:
    # Rotation needed for Huawei P30 Pro panoramas. Don't know about other devices. Comment out if not needed.
    img.rotate(-90)

    # Change height to 1080 whilst keeping aspect ratio
    img.transform(resize='x1080')

    # Figure out overhangs on multiple of 1080 wide
    overhang = img.width % 1080
    leftc = math.floor(overhang/2)
    rightc = img.width - math.ceil(overhang/2)

    # Crop left and right of image equally to make image a multiple of 1080 wide
    img.crop(left=leftc, right=rightc)

    # Generate each sub-image as 1080x1080
    k=0
    for j in range(0,img.width,1080):
        with img[j:j+1080, 0:1080] as cropped:
            # De-rotation needed for Huawei P30 Pro panoramas. Don't know about other devices. Comment out if not needed.
            cropped.rotate(90)

            # Save as JPEG and include sequence number in name
            cropped.format = 'jpeg'
            rootfilename = '.'.join(sys.argv[1].rsplit(".")[:-1])
            splitfilename = rootfilename + "_pano_" + str(k) + '.jpg'
            print(splitfilename)
            cropped.save(filename=splitfilename)
            k +=1

