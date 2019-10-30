# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:19:17 2019

@author: Graham

Subject: Scaling an Image.
"""

import cv2

def main():
    imgp = "E:\\OCV\\Images\\misc\\4.2.02.tif"
    img = cv2.imread(imgp)

# The fx is used to scale the image in vertical and fy is used to scale the image in horizontal manner.
    img1 = cv2.resize(img, None, fx=1, fy=1, interpolation = cv2.INTER_LINEAR)
#    img2 = cv2.resize(img, None, fx=1, fy=1, interpolation = cv2.INTER_NEAREST)
#    img3 = cv2.resize(img, None, fx=0.4, fy=0.4, interpolation = cv2.INTER_AREA)
#    img4 = cv2.resize(img, None, fx=1, fy=1, interpolation = cv2.INTER_CUBIC)
#    img5 = cv2.resize(img, None, fx=1, fy=1, interpolation = cv2.INTER_LANCZOS4)
    
    cv2.imshow("Linear resize", img1)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


"""
USE ONLY IF YOUR COMPUTER CAN HANDLE MULTIPLE OPEN WINDOWS.    
    
    images = [img1, img2, img3, img4, img5]
    titles = ["Linear", "Nearest", "Area", "Cubic", "LANCZOS4"]
    
    for i in range(5):
        cv2.imshow(titles[i], images[i])
"""

