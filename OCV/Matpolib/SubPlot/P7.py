# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:46:21 2019

@author: Graham

Subject: Negative of an image in RGB and Gray-Scale.Applies mostly on plain matrices.
"""

import cv2
import matplotlib.pyplot as plt
def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.06.tiff"
    img1 = cv2.imread(imgp)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    
# Negative of the image by using formula of highest channel - image
    
    img3 = abs(255 - img1)
    img4 = abs(255 - img2)
    
    images = [img1, img2, img3, img4]
    titles = ["Original", "Gray-Scale", "Og-Negative", "Gray-Negative"]
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
    
if __name__ == "__main__":
    main()