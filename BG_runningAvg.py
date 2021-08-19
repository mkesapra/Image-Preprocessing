#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:26:57 2020

@author: kesaprm
"""
# organize imports 
import cv2 
import numpy as np 
  
# capture frames from a camera 
cap = cv2.VideoCapture('well1.avi') 
  
# read the frames from the camera 
_, img = cap.read() 
  
# modify the data type 
# setting to 32-bit floating point 
averageValue1 = np.float32(img) 

# We need to set resolutions. 
# so, convert them from float to integer. 
frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4)) 
   
size = (frame_width, frame_height) 
   
  
result = cv2.VideoWriter('filename.avi',  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, size) 

# loop runs if capturing has been initialized.  
while(4):
    # reads frames from a camera  
    _, img = cap.read() 
     
    # using the cv2.accumulateWeighted() function 
    # that updates the running average 
    cv2.accumulateWeighted(img, averageValue1, 0.02) 
      
    # converting the matrix elements to absolute values  
    # and converting the result to 8-bit.  
    resultingFrames1 = cv2.convertScaleAbs(averageValue1) 
    
  
    # Show two output windows 
    # the input / original frames window 
    result.write(resultingFrames1)
    cv2.imshow('InputWindow', img) 
  
    # the window showing output of alpha value 0.02 
    cv2.imshow('averageValue1', resultingFrames1) 
      
    # Wait for Esc key to stop the program  
    k = cv2.waitKey(30) & 0xff
    if k == 27:  
        break
  
# Close the window  
cap.release()  

result.release() 
    
# De-allocate any associated memory usage  
cv2.destroyAllWindows()


# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
   # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite("frame%d.jpg" % count, image) 
  
        count += 1 
        
FrameCapture('filename.avi')

