# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:34:45 2019

@author: Graham
"""

import cv2
import matplotlib.pyplot as plt

def main():
    imgpath="E:\\OCV\\Images\\standard_test_images\\lena_color_512.tif"
    
# cv2.imread reads is BGR format    
    
    img=cv2.imread(imgpath, 1)
    
#Converts BGR to RGB colorspace.
    
    img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# In Matplotlib --> plt.imshow displays image in RGB format without cv2.cvtColor() function used.
    
    plt.imshow(img)
    plt.title("Default Colormap using Matplotlib")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
# This displays the image which is expected in the colored format(RGB converted).
    
    plt.imshow(img1)
    plt.title("Default Colormap after using cvt")
    plt.xticks([])
    plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()