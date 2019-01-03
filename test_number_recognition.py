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


# Threshold the image
ret, im_gray = cv2.threshold(im_gray, 250, 255, cv2.THRESH_BINARY_INV)


# Find contours in the image
im_gray, ctrs, hier = cv2.findContours(im_gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# save contour image
cv2.imwrite("ctr.jpg", im_gray)

# min contour area 
threshold_area = 5000

height, width = im_gray.shape
min_x, min_y = width, height
max_x = max_y = 0


hier = hier[0]

num =[]

# initialize contour position 
ctr2 = 0
temp = 0

# sort contours from top to bottom, left to right 
#ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0] + cv2.boundingRect(ctr)[1] * im.shape(1))

# computes the bounding box for the contour, and draws it on the frame,
for contour, hier in zip(ctrs, hier):
    
    area = cv2.contourArea(contour)
    if area > threshold_area:
       
        # contour index is [next, previous,first child, parent ]
        # find digits (contours that do not have inner contours(children) have -1 for first child)
        if hier[2] == -1:
            
            ctr1 = temp 
            ctr2 = contour[0]
            temp = ctr2
            d = ctr2 - ctr1 
            print "d"
            print d
            (x,y,w,h) = cv2.boundingRect(contour)
            
            min_x, max_x = min(x, min_x), max(x+w, max_x)
            min_y, max_y = min(y, min_y), max(y+h, max_y)
            cv2.rectangle(im, (x,y), (x+w,y+h), (0, 255, 0), 2)
            roi = im[y:(y+h), x:(x+w)]

 
            # Resize the image
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_LINEAR)
            roi = cv2.dilate(roi, (3, 3))
            
            # Calculate the HOG features
            roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualize=False)
            
            # estimate number 
            nbr = clf.predict(np.array([roi_hog_fd], 'float64'))
            cv2.putText(im, str(int(nbr[0])), (x, y),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)
            nbr = nbr.astype(int)
#            if abs(d[0][0]) < 300:
#                num.append(nbr[0]*10)
#            else: 
#                num.append(nbr[0])
            num.append(nbr[0])
#cv2.imshow("Resulting Image with Rectangular ROIs", mask)
print num         
cv2.imwrite("test.jpg", im)