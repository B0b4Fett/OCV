# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:02:21 2019

@author: Graham

How to Read a video file and process it.
"""

import cv2
def main():
    windowName = "OpenCV video feed."
    cv2.namedWindow(windowName)
    filename = 'E:\\OCV\\Output\\P4-XVID2.avi'
    cap = cv2.VideoCapture(filename)
    
    while cap.isOpened():
        
        ret, frame = cap.read()
        
        print(ret)
        
        if ret:
            cv2.imshow(windowName, frame)
            if cv2.waitKey(33) == 27:
                break
        else:
            break
    
    cv2.destroyAllWindows()  
    cap.release()

if __name__ =="__main__":
    main()