# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:55:27 2019

@author: Graham

Subject 
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img = cv2.imread(imgp)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rows, columns, channels = img.shape
    
    T = np.float32([[1, 0, 50], [0, 1, 50]])
    
    output = cv2.warpAffine(img, T, (columns, rows))
    
    plt.imshow(img)
    plt.title("Original image")
    plt.show()
    plt.imshow(output)
    plt.title("Shifted Image")
    plt.show()
    print("\nTranslation =",T)
if __name__ == "__main__":
    main()