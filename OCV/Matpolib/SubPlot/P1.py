# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:06:48 2019

@author: Graham

Subject: Plotting Images using Subplot from Matplotlib.
"""

import cv2
import matplotlib.pyplot as plt

def main():
    path = "E:\\OCV\\Images\\misc\\"
    imgpath1 = path + "4.2.01.tiff"
    imgpath2 = path + "4.2.02.tif"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    titles = ['Liquid Drop', 'Lena']
    images = [img1, img2]
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

# Use plt.show() only 1ce after the end of row.

    plt.show()
if __name__ == "__main__":
    main()