# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:45:47 2019

@author: Graham
"""

import cv2
import numpy as np
windowName = 'Drawing'
img =np.zeros((512,512,3), np.uint8)
cv2.namedWindow(windowName)

# Mouse callback function
def draw_circle(event, x, y, flags, param):

#Creates and Displays a circle on the canvas when the Left-Mouse-Button is Double-clicked.
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y), 20, (0,255,0), -1)

#Creates and Displays a circle on the canvas when the Scroll-Wheel is pressed.
    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img, (x,y), 30, (255,0,0), -1)

#Creates and Displays a circle on the canvas when the Right-Mouse-Button is pressed.    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y), 40, (0,0,255), -1)

# Mouse callback function to window
cv2.setMouseCallback(windowName, draw_circle)

def main():
    while(True):
        cv2.imshow(windowName,img)

# 27 indicates it's the Escape key on the keyboard.Onpressing the Escape key we close the active Window("Drawing" in this case)
        
        if cv2.waitKey(20) == 27:
            break
        
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()