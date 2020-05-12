#!/usr/bin/env python3

from PIL import Image
import os
import glob

source = "/home/student-02-50f10476cf94/images"
path = "/opt/icons"
target = path


if not os.path.exists(path):
    os.makedirs(path)

size = 128,128
print(source)

for filename in glob.glob("ic_*"):
   if os.path.isfile(source + "/" + filename):
        im = Image.open(source + "/" + filename)
        res_im = im.resize((size))
        conv_im = res_im.rotate(270)
        rgb_im = conv_im.convert('RGB')
        rgb_im.save(target + "/" + filename, "JPEG")
        print(os.path.join(source, filename))
        print(os.path.join(target, filename))
   else:
       print("nenhum arquivo")
