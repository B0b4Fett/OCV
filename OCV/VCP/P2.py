# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:45:03 2019

@author: Graham
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
        
    else:
        ret = False
    
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img1)
    plt.title("Default frame in RGB.")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    cap.release()

if __name__ == "__main__":
    main()