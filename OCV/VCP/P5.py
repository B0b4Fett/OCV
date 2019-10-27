# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:15:48 2019

@author: Graham
"""

import cv2
def main():
     windowName = "Resolution Check"
     cv2.namedWindow(windowName)
     cap = cv2.VideoCapture(0)

# To print the current resolution ie the width and height of the Live feed.
     print("The Resolution before setting the custom resolution.")
     print("Width: "+str(cap.get(3)))     
     print("Height: "+str(cap.get(4)))
     
# To set the width and height resolution of the capture quality.     
     cap.set(3,5000) #5000 to check max resolution in width.
     cap.set(4,5000) #5000 to check max resolution in height.
     
     print("\nThe Resolution after resetting the resolution.")
     print("Width:"+str(cap.get(3)))
     print("Height: "+str(cap.get(4)))
     
     if cap.isOpened():
        ret, frame = cap.read()
     else:
        ret = False
        
     while ret:
        ret, frame = cap.read()
        
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow(windowName, frame)
        cv2.imshow("The Gray Scale", output)
        if cv2.waitKey(1) == 27:
            break
     cv2.destroyAllWindows()
     
if __name__ == "__main__":
    main()