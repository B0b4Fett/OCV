# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:01:29 2019

@author: Graham

Subject : Object Tracking.
"""

import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        
        ret, frame = cap.read()
        
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
# Blue Color Tracking.
        
        low = np.array([100,50,50])
        high = np.array([140,255,255])        
        
        img_mask = cv2.inRange(hsv, low, high)
        
        bitM = cv2.bitwise_and(frame, frame,mask = img_mask)
        
        
        cv2.imshow("Original Feed.", frame)
        cv2.imshow("Feed with Image Mask.", img_mask)
        cv2.imshow("Color Blue Tracking.", bitM)
        
        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()