#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 19:11:18 2018

@author: amandatsai
"""

# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

# Load the classifier
clf = joblib.load("digits_cls.pkl")

# Read the input image 
im = cv2.imread("/Users/amandatsai/mask.jpg")


# convert image to gray scale 
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

cv2.imwrite("test2.jpg", im_gray)
#
#print im_gray.shape
# Threshold the image
ret, im_gray = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)
##

# Find contours in the image
im_gray, ctrs, hier = cv2.findContours(im_gray.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

print im_gray.shape
height, width = im_gray.shape
min_x, min_y = width, height
max_x = max_y = 0

print ctrs
## computes the bounding box for the contour, and draws it on the frame,
#for contour, hier in zip(ctrs, hier):
#    (x,y,w,h) = cv2.boundingRect(contour)
#    min_x, max_x = min(x, min_x), max(x+w, max_x)
#    min_y, max_y = min(y, min_y), max(y+h, max_y)
#    
#    cv2.rectangle(im_gray, (x,y), (x+w,y+h), (255, 0, 0), 2)

# Get rectangles contains each contour
#rects = [cv2.boundingRect(ctr) for ctr in ctrs]
#
# 
#for (x,y,w,h) in rects:
#    cv2.rectangle(im_gray,(x,y),(x+w,y+h),(0,255,0),3)

    # Make the rectangular region around the digit
#    leng = int(w * 1.6)
#    pt1 = int(y + h // 2 - leng // 2)
#    pt2 = int(x + w // 2 - leng // 2)
#    roi = im_gray[pt1:pt1+leng, pt2:pt2+leng]
#    print roi.shape
#    
#    
#    #print roi
#    # Resize the image
##    roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_LINEAR)
##    roi = cv2.dilate(roi, (3, 3))
#    # Calculate the HOG features
#    roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualize=False)
##    print roi_hog_fd
#    nbr = clf.predict(np.array([roi_hog_fd], 'float64'))
#    cv2.putText(im_gray, str(int(nbr[0])), (x, y),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

#cv2.imshow("Resulting Image with Rectangular ROIs", mask)
cv2.imwrite("test.jpg", im_gray)