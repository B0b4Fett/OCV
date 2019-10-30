# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:56:24 2019

@author: Graham

Subject: Blending and Trasitioning of images using addWeighted().
"""

import cv2
import matplotlib.pyplot as plt
def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.01.tiff"
    imgp2 = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img1 = cv2.imread(imgp, 1)
    img2 = cv2.imread(imgp2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    images = [img1, img2]
    titles = ["Droplet", "Lena"]
    print("\nOriginal images")
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
# Subplotted images.
    
    alpha = 0.4
    beta = 0.6
    gamma = 0
    
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    
    imgs = [img1, img2, output]
    tits = ["Droplet","Lena","Weighted Addition"]
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(imgs[i])
        plt.title(tits[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    print("")
if __name__ =="__main__":
    main()