#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:11:40 2020

@author: kesaprm
"""

import numpy as np 
import cv2 


cap = cv2.VideoCapture("well1.avi")




fgbg = cv2.createBackgroundSubtractorMOG2() 

#### This creates a foreground mask of the image  
while(1): 
    ret, frame = cap.read() 
  
    fgmask = fgbg.apply(frame) 
   
    cv2.imshow('fgmask', fgmask) 
    cv2.imshow('frame',frame ) 
    cv2.imwrite('image2.png', fgmask)

      
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
      
  
cap.release() 
cv2.destroyAllWindows() 



img = cv2.imread("images/20X MQAE 7.5mM well 1 .PNG", 0)
def remove_bg(raw_img, avg):

	cv2.accumulateWeighted(raw_img,avg,0.0005)
	bg_img = cv2.convertScaleAbs(avg)
	#cv2.imshow('bg_img',bg_img)

	return bg_img, avg

remove_bg(img,0)