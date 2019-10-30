# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:12:26 2019

@author: Graham

Subject: Rotating an image.
"""

import cv2
import matplotlib.pyplot as plt
def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img = cv2.imread(imgp)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img.shape
    
    R = cv2.getRotationMatrix2D((columns/2, rows/2), 45, 0.5)
    
    output = cv2.warpAffine(img, R, (columns, rows))
    plt.imshow(img)
    plt.title("Original Image.")
    plt.show()
    plt.imshow(output)
    plt.title("Rotated Image.")
    plt.show()
    print("Rotaion Matrix",R)
if __name__ == "__main__":
    main()

