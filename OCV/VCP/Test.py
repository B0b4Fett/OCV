# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:22:21 2019

@author: Graham
"""

import cv2 as cv 

def testDevice(source):
   cap = cv.VideoCapture(source) 
   if cap is None or not cap.isOpened():
       print('Warning: unable to open video source: ', source)

testDevice(0) # no printout
testDevice(1) # prints message