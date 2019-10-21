#This is a program to read an image using cv2.imread() to read image and display using cv2.imshow().
import cv2
def main():
    imgpath = "E:\\OCV\\Images\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindows('Lena')

if __name__ == "__main__":
    main()