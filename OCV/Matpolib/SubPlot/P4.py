# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:46:08 2019

@author: Graham
"""

import cv2
import numpy as np
import time
def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.01.tiff"
    imgp2 = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img1 = cv2.imread(imgp, 1)
    img2 = cv2.imread(imgp2, 1)
    
    alpha = 0.0
    beta = 1.0
    gamma = 0
    
    for i in np.linspace(0, 1, 50):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    
        cv2.imshow("Transision",output)
        time.sleep(0.01)
    
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()