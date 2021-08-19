#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:20:42 2020

@author: kesaprm
"""


import cv2
from cv2_rolling_ball import subtract_background_rolling_ball
from matplotlib import pyplot as plt

##### Read Images and convert them to grayscale
img =  cv2.imread("/Users/kesaprm/Learning/Images_NEUO/Day16_2_Plate_D_p00_0_A01f01d0.PNG",0)
imgT1 =  cv2.imread("images/20X MQAE 7.5mM well 1 + IVM t1.PNG",0)
imgT2 =  cv2.imread("images/20X MQAE 7.5mM well 1 + IVM t2.PNG",0)

### Rolling ball radius - defaulted to 50 as in ImageJ
radius =50

####Backgorund subtraction using subtract_background_rolling_ball
final_img, background = subtract_background_rolling_ball(img, radius, light_background=False, use_paraboloid=False, do_presmooth=True)
final_img1, background1 = subtract_background_rolling_ball(imgT1, radius, light_background=False, use_paraboloid=False, do_presmooth=True)
final_img2, background2 = subtract_background_rolling_ball(imgT2, radius, light_background=False, use_paraboloid=False, do_presmooth=True)


##### Contrast limited adaptive histogram equalization (CLAHE) 
clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
clahe_img = clahe.apply(final_img)
clahe_img1 = clahe.apply(final_img1)
clahe_img2 = clahe.apply(final_img2)


#### Plotting the hiostograms for all the 3 images 
plt.hist(background.flat,bins=100, range=(20,100),label="Well1")
plt.hist(background1.flat,bins=100, range=(20,100),label="Well1+T1")
plt.hist(background2.flat,bins=100, range=(20,100),label="Well1+T2")
plt.legend()
plt.title('Before BG')
plt.xlabel('Intensity')
plt.ylabel('Pixel Count')
plt.hist(final_img.flat,bins=100, range=(0,20),label="Well1")
plt.hist(final_img1.flat,bins=100, range=(0,20),label="Well1+T1")
plt.hist(final_img2.flat,bins=100, range=(0,20),label="Well1+T2")
plt.legend()
plt.title('After BG')
plt.xlabel('Intensity')
plt.ylabel('Pixel Count')
plt.hist(clahe_img.flat,bins=100, range=(0,100),label="Well1")
plt.hist(clahe_img1.flat,bins=100, range=(0,100),label="Well1+T1")
plt.hist(clahe_img2.flat,bins=100, range=(0,100),label="Well1+T2")
plt.legend()
plt.title('After Contrast limited adaptive histogram equalization (CLAHE) ')
plt.xlabel('Intensity')
plt.ylabel('Pixel Count')

####auto-thresholding using OTSU for img
retBG,thresh =cv2.threshold(background,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retFinal,thresh1 =cv2.threshold(final_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retHE,thresh2 =cv2.threshold(clahe_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



####auto-thresholding using OTSU for img1
retBG1,thresh11 =cv2.threshold(background1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retFinal1,thresh111 =cv2.threshold(final_img1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retHE1,thresh211 =cv2.threshold(clahe_img1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

####auto-thresholding using OTSU for img2
retBG2,thresh22 =cv2.threshold(background2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retFinal2,thresh122 =cv2.threshold(final_img2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retHE2,thresh222 =cv2.threshold(clahe_img2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


####show the images- for example: images of img
cv2.imshow("Background image",background)
cv2.imshow("After CLAHE", clahe_img)
cv2.imshow("After Back sub",final_img)
cv2.imwrite("Day16_2_Plate_D_p00_0_A01f01d0.PNG",final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

