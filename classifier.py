#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:04:45 2018

@author: amandatsai
"""

from sklearn.externals import joblib
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy as np


# download handwritten digits dataset (images)
dataset = datasets.fetch_mldata("MNIST Original")
features = np.array(dataset.data, 'int16')
labels = np.array(dataset.target, 'int')

print dataset.data.shape
print dataset.target.shape

# calculate HOG features for each image 
list_hog_fd = []
for feature in features: 
    fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualize=False)
    list_hog_fd.append(fd)
hog_features = np.array(list_hog_fd, 'float64')

# SVM
clf = LinearSVC()
clf.fit(hog_features, labels)

# save classifier 
joblib.dump(clf, "digits_cls.pkl", compress=3)

#
#    
