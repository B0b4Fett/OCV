# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:03:26 2019

@author: Graham
"""

import cv2
import numpy as np
def main():
    img = np.zeros((512,512,3),np.uint8)
    
#This is for executing the geometrical shapes.
    cv2.line(img, (0,99), (99,0), (0,255,0), 2)
    cv2.rectangle(img, (0,99), (58,120), (0,0,255), 2)
    cv2.circle(img, (99,99),40, (255,0,0),-1)
    
#For elipse (position of center(x,y),scale(vertical,horizontal),rotaion x,rotation y,image clipping(in circular like test 90 to understand),color(B,G,R),filled or hollow value(-1 for filled and any positive value is border thickness))    
    cv2.ellipse(img, (160,260),(60,20),0,50,360,(255,255,0),-1)

#For Polygonal shapes
    points = np.array([[286,320],[125,5],[179,9],[230,5],[30,50]],np.int32)
    points = points.reshape((-1,1,2))
    cv2.polylines(img,[points],True,(255,0,255))
    
#For Text on images, (img variable, text variable,coordinates(x,y),font type (cv2.font),font size,text color)
    text='Boba Fett'
    cv2.putText(img,text,(220,100),cv2.FONT_HERSHEY_SIMPLEX,1.7,(255,255,0))
#    img = cv2.imread(imgpath)
    cv2.imshow('Test', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Test')
if __name__ == "__main__":
    main()