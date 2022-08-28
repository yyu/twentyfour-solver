#!/usr/bin/env python3

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import imutils
from imutils.perspective import four_point_transform
from imutils import contours


def read_jpeg(filename):
    img = cv.imread(filename)
    #print(dir(img))

    #cv.imshow('image', img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    # pre-process the image by resizing it, converting it to graycale, blurring it, and computing an edge map
    image = imutils.resize(img, height=500)
    image = img
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    edged = cv.Canny(blurred, 50, 200, 255)

    # find contours in the edge map, then sort them by their size in descending order
    contours = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv.contourArea, reverse=True)

    numimgs = []

    # loop over the contours
    for c in contours:
        # approximate the contour
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.02 * peri, True)

        # if the contour has four vertices, then we have found the thermostat display
        if len(approx) == 4:
            numimgs.append(approx)

    n = len(numimgs)

    for i, contour in enumerate(numimgs):
        # extract the thermostat display, apply a perspective transform to it
        #warped = four_point_transform(gray, contour.reshape(4, 2))
        output = four_point_transform(image, contour.reshape(4, 2))

        img = output

        plt.subplot(2, n//2, i+1)
        plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

    plt.show()


if __name__ == '__main__':
    read_jpeg('nums_1_5_12_12.jpeg')

