# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:14:48 2019

@author: Graham
"""

#The realationship between Numbers and Images.

"""
Humans = Biology = pattern

Senses = Visual, audio, smell, touch etc.

Computers = Mathematical numbers = data in form of numbers.
"""

import cv2
def main():
    imgpath = "E:\\OCV\\Images\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath)


#===> Shows the numpy.ndarray data
#    print(img)
    print("The DataType of image:",type(img))
    print("The Shape of image:",img.shape)
    print("The Dimention of image:",img.ndim)
    print("The Constituent memebers of ndarray:",img.dtype)
#Image size on memory it's the product of the dimensional values.In this case 256x256x3 = 196608
    print("The Size of the image:",img.size)

#    cv2.imshow('Lena',img)
#    cv2.waitKey(0)
#    cv2.destroyWindow('Lena')

if __name__ == "__main__":
    main()