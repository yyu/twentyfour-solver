#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:31:26 2018

@author: amandatsai
"""

# Import the modules
import cv2
from sklearn.externals import joblib


# Load the classifier
clf = joblib.load("digits_cls.pkl")

# Read the input image 
im = cv2.imread("/Users/amandatsai/IMG_1482.jpg")
#im =  cv2.imread("/Users/amandatsai/digit.jpg")

# Convert to grayscale and apply Gaussian filtering
#im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

# convert to hsv 
im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

print im_hsv.shape

# bounds for green color 
lower_green = (40,0,0)
upper_green = (70, 255,255)

# threshold the image
mask = cv2.inRange(im_hsv,lower_green, upper_green)

#imask = mask>0
#green = np.zeros_like(im, np.uint8)
#green[imask] = im[imask]

#invert mask
mask = cv2.bitwise_not(mask)

print mask.shape

cv2.imwrite("mask.jpg", mask)

