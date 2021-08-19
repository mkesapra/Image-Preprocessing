#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:28:24 2020

@author: Manasa Kesapragada
"""

import glob
from skimage import io,img_as_ubyte

path_images = "images/*"
path_masks = "masks/*"

#create empty folders images_conv & masks_conv, to save the converted images & masks

for file in glob.glob(path_images):
    img=io.imread(file, as_gray=True)
    img= img_as_ubyte(img)
    io.imsave('images_conv/'+file[7:], img)
 
for file in glob.glob(path_masks):
    mask=io.imread(file, as_gray=True)
    mask= img_as_ubyte(mask)
    io.imsave('masks_conv/'+file[6:], mask)
    