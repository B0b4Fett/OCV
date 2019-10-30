# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:28:35 2019

@author: Graham
"""

import cv2
import time
def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img = cv2.imread(imgp)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels= img.shape
    angle = 360
    while True:
        if angle == 360:
            angle = 0
        R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, 1)
    
        output = cv2.warpAffine(img, R, (columns, rows))
        cv2.imshow("Rotated image", output)
        angle = angle - 1
        time.sleep(0.001)
        if cv2.waitKey(1) == 27:
            break
    print("\nRotated Image",R)
    cv2.destroyAllWindows()
if __name__ =="__main__":
    main()