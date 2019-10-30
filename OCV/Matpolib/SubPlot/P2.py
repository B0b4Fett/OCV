# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:16:05 2019

@author: Graham

Subject: Apply Arithmetic operations on the images.
"""

import cv2
import matplotlib.pyplot as plt

def main():
    imgpath = "E:\\OCV\\Images\\misc\\4.2.01.tiff"
    imgpath2 = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img1 = cv2.imread(imgpath, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    images = [img1, img2]
    titles = ["Droplet", "Lena"]
    
    print("Original Images plotted.")
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
    plt.show()    
    print("\nEdited images.")

# Possible Arithmetic operations between img1 and img2.    
    add = img1 + img2
    mult = img1 * img2
    sub1 = img1 - img2
    sub2 = img2 - img1
    div1 = img1 / img2
    div2 = img2 / img1
    
    
    imgs = [add, mult, sub1, sub2, div1, div2]
    tits = ["Add", "Multiply", "Sub1", "Sub2", "Div1", "Div2"]
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(imgs[i])
        plt.title(tits[i])
        plt.xticks([])
        plt.yticks([])
    
    plt.show()
    
if __name__ == "__main__":
    main()