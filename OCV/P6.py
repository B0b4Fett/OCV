# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
def main():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)

if __name__ == "__main__":
    main()