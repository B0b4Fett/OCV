# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:56:42 2019

@author: Graham
"""

import cv2
def emptyFunction():
    pass

def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.01.tiff"
    imgp2 = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img1 = cv2.imread(imgp, 1)
    img2 = cv2.imread(imgp2, 1)
    
    alpha = 0.5
    beta = 0.5
    gamma = 0
    
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    
    windowName = "Transition Demo"
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('Alpha', windowName, 0, 10, emptyFunction)
    while True:
        cv2.imshow(windowName, output)
        
        alpha = cv2.getTrackbarPos('Alpha', windowName) / 10
        beta = 1 - alpha
        gamma = 0
        
        output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
        print(alpha, beta)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()