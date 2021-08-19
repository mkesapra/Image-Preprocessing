#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:09:13 2020

@author: kesaprm
"""

import os
from PIL import Image, ImageOps 

PATH = "/Users/kesaprm/Downloads/Device13_Images_For_Analysis/"
Copy_to_path="/Users/kesaprm/Downloads/gray_13/"

for filename in os.listdir(PATH):
    img = Image.open(os.path.join(PATH, filename)) # images are color images
    img = ImageOps.grayscale(img)
    img.save(Copy_to_path+filename) 

