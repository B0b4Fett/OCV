# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:17:33 2019

@author: Graham

Subject: cv2.split() and cv2.merge()
"""

import cv2
import matplotlib.pyplot as plt
def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.01.tiff"
#    imgp2 = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img1 = cv2.imread(imgp, 1)
#    img2 = cv2.imread(imgp2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    r, g, b = cv2.split(img1)
    mer = cv2.merge((r, g, b))
    titles = ["Original","Red","Green","Blue"]
    images = [mer, r, g, b]
    
    print("\nThe Subplotted images by using split and Merge:\n")
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        if i==0:
            plt.imshow(images[i])
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])
        else:
            plt.imshow(images[i],cmap = "gray")
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()