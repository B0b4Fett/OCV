# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:28:37 2019

@author: Graham
"""
import cv2
def main():
    windowName = "Capture Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    filename = "E:\\OCV\\Output\\P4-XVID2.avi"
    codec = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate = 30
    
# The height and width of the capture device can be obtained using the following.

#   print('width' + str(cap.get(3)))
    
#   print('height' + str(cap.get(4))) 
    
    resolution = (640,480)
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        frame = cv2.flip(frame, -1 )
        VideoFileOutput.write(frame)
        cv2.imshow(windowName, frame)
        if cv2.waitKey(17) == 27:
            break
    
    cv2.destroyAllWindows()
    VideoFileOutput.release()
    cap.release()
if __name__ == "__main__":
    main()
