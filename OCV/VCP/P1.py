# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:16:19 2019

@author: Graham
"""
import cv2
def main():
    
#This is where we define a variable to call a capture device.
    
    cap = cv2.VideoCapture(0)
    
#This is used to return the frame in nparray format.
    
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
    else:
        ret = False

if __name__ == "__main__":
    main()