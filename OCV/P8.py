# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:45:39 2019

@author: Graham
"""
import cv2
import numpy as np

windowName = "Drawing Demo"
img = np.zeros((255,255,3), np.uint8)
cv2.namedWindow(windowName)

# True if mouse is pressed
drawing = False

# If mode is True, then draw a Rectangle else draw a Circle. Pressing 'M' on keyboard to toggle "Curve"
mode = True
(ix, iy) = (-1,-1)

# Mouse callback Function
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode
    
#Left-Mouse-Button pressed.
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x,y

#While Left-Mouse-Button is being pressed and still mouse is moving,execute below block of code.        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y),(0,255,0),-1)
            else:
                cv2.circle(img, (x, y),3,(0,0,255),-1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y),(0,255,0), -1)
        else:
            cv2.circle(img, (x, y),3,(0,0,255),-1)

# Connecting the Callback function to our custon window i.e Drawing Demo in this case.
cv2.setMouseCallback(windowName, draw_shape)
def main():
    global mode
    
    while(True):
        cv2.imshow(windowName, img)
        
        k = cv2.waitKey(1)
        if k == ord('m') or k == ord('M'):
            mode = not mode
        elif k == 27:
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main()__":
    main()