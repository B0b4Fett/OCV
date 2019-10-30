# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:01:29 2019

@author: Graham

Subject: Using Bitwise Logical Operations on images.
"""

import cv2
import matplotlib.pyplot as plt
def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.01.tiff"
    imgp2 = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img1 = cv2.imread(imgp)
    img2 = cv2.imread(imgp2)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    img3 = cv2.bitwise_not(img1)
    img4 = cv2.bitwise_and(img1, img2)
    img5 = cv2.bitwise_or(img1, img2)
    img6 = cv2.bitwise_xor(img1, img2)
    
    images = [img1, img2, img3, img4, img5, img6]
    titles = ["Droplet", "Lena", "NOT", "AND", "OR", "XOR"]
    
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()