#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:12:20 2020

@author: kesaprm
"""


# import matplotlib.pyplot as plt
# from skimage import io, restoration
# from skimage.filters.rank import entropy
# from skimage.morphology import disk

# img = io.imread("images/t120.tif")
#######entropy img - image which we cannot distinguisgh the background
# plt.imshow(entropy_img, cmap="gray")
# entropy_img = entropy(img, disk(3)) 

# from skimage.filters import try_all_threshold

# from skimage.filters import threshold_otsu

# thresh =threshold_otsu(entropy_img)

# binary = entropy_img > thresh 

# plt.imshow(binary,cmap="gray")


# from skimage import io
# import matplotlib.pyplot as plt


# img = io.imread("images/t120.tif", as_gray=True)

# from skimage.filters import roberts, sobel, scharr, prewitt

# er = roberts(img)
# sb = sobel(img)
# scharr = scharr(img)
# prewitt = prewitt(img)

# plt.imshow(er)
# plt.imshow(sb)
# plt.imshow(scharr)
# plt.imshow(prewitt)


# from PIL import Image
# img = Image.open('images/t120.tif').convert('LA')
# img.save('images/greyscale.tif')

# import matplotlib.pyplot as plt
# from skimage import io
# img = io.imread('images/t120.tif', as_gray=True)
# plt.imshow(img)



import glob
from skimage import io,img_as_float #,img_as_ubyte

#from skimage.transform import resize
#from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as nd
from skimage.restoration import denoise_nl_means, estimate_sigma
import cv2

path = "images/*"

# for file in glob.glob(path):
    
#     g=io.imread(file, as_gray=True)
#     io.imsave('images_conv/'+file[7:], g)
    
    
   # """code to create masks"""
   #  float_img= img_as_float(io.imread(file))
   #  sigma_est = np.mean(estimate_sigma(float_img, multichannel=True))
   # # gaussian_img = denoise_nl_means(float_img, h=1.15 * sigma_est, fast_mode=True,patch_size=5,patch_distance=3,  multichannel=True)
    
   #  #gaussian_img = nd.gaussian_filter(g, sigma=3)
   #  gaussian_img = nd.median_filter(g, size=3)
    
   #  #io.imsave('masks/'+file[7:], gaussian_img)
    
   #  thresh = np.mean(gaussian_img)
   #  x, y = gaussian_img.shape
   
   #  for i in range(x):
   #      for j in range(y):
   #          if(gaussian_img[i][j] > thresh):
   #              gaussian_img[i][j] = 255
   #          else:
   #              gaussian_img[i][j] = 0
   
   #  io.imsave('masks/'+file[7:], gaussian_img)
    
  #  """to convert an image to 8-bit """
    #g= img_as_ubyte(g)
    
    ###Using open-cv
    #openimg = cv2.imread(file,0)
    #cv2.imwrite('masks/'+file[7:],openimg)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
   
    ###Using Pillow
    #a= Image.open(file).convert('LA')
    #a.save('masks/'+file[7:])
    
    
"""Using denoise_nl_means for denoising and cv2 canny for edge detection""" 
# float_img= img_as_float(io.imread('images/t4101.tif'))
# sigma_est = np.mean(estimate_sigma(float_img, multichannel=True))
# gaussian_img = denoise_nl_means(float_img, h=1.15 * sigma_est, fast_mode=True,patch_size=5,patch_distance=3,  multichannel=True)

# openimg = cv2.imread('images/t4101.tif',1)
# edges = cv2.Canny(openimg,100,200)    
# kernel = np.ones((3,3),np.float32)/9
# fil_2D = cv2.filter2D(openimg, -1, kernel)

# cv2.imshow("original",openimg)
# cv2.imshow("fil_2D",fil_2D)
# #io.imsave('t01.jpg',edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# thresh = np.mean(gaussian_img)
# x, y = gaussian_img.shape

# for i in range(x):    
#     for j in range(y):
#         if(gaussian_img[i][j] > thresh):
#             gaussian_img[i][j] = 255
#         else:
#             gaussian_img[i][j] = 0
# io.imshow(gaussian_img)
#io.imsave('t01.jpg',gaussian_img)

    
"""Using cv2 canny""" 
# float_img= img_as_float(io.imread('images/t4101.tif'))
# sigma_est = np.mean(estimate_sigma(float_img, multichannel=True))
# gaussian_img = denoise_nl_means(float_img, h=1.15 * sigma_est, fast_mode=True,patch_size=5,patch_distance=3,  multichannel=True)

img = cv2.imread('images/t010.tif',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img = clahe.apply(img)
median = cv2.medianBlur(img, 3)
kernel = np.ones((3,3), np.uint8)
 
ret, thresh = cv2.threshold(img,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

cv2.imshow("thres",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
# edges = cv2.Canny(openimg,100,200)
# cv2.imshow("edges",openimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# thresh = np.mean(openimg)
# x, y = openimg.shape
# for i in range(x):    
#     for j in range(y):
#         if(openimg[i][j] > thresh):
#             openimg[i][j] = 255
#         else:
#             openimg[i][j] = 0
# io.imshow(openimg)
# io.imsave('t01.jpg',openimg)







