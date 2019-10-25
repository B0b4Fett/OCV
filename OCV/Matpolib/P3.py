# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:08:52 2019

@author: Graham
"""

import cv2
def main():
    i = 0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            i=i+1
    print("\n\nThere are",str((i+1)),"color conversion flags in the cv2.cvtColor() function available in OpenCV.")

if __name__ == "__main__":
    main()