# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:50:25 2019

@author: Graham
"""

#This program is used to read image and display image along with different methods involved in reading and also to write the image to the disc.
# imread(),imwrite() and imshow() methods used.

import cv2
def main():
    imgpath = "E:\\OCV\\Images\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath, 0)
    outpath = "E:\\OCV\\Output\\lena_gray_scale_256.jpg"
    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')

if __name__ == "__main__":
    main()