# -*- coding: utf-8 -*-
"""
Spyder Editor

In this Practical we learn how to use Matplotlib library to plot image on a graph.
We can see how to display them in console by defining the path of the image in a variable and then plot it using Matplotlib. 
"""
import cv2
import matplotlib.pyplot as plt
def main():
    imgpath = "E:\\OCV\\Images\\standard_test_images\\lena_color_512.tif"
    img = cv2.imread(imgpath, 0)
    
# Shows the image plotted in the console
    
    plt.imshow(img)
    plt.title("Default Colormap")
    plt.show()
    
    plt.imshow(img, cmap="gray")
    plt.title("Gray Colormap")
    plt.show()
    
    plt.imshow(img, cmap="Blues")
    plt.title("Blues Colormap")
    plt.show()
    
    plt.imshow(img, cmap="Greens")
    plt.title("Greens Colormap")
    plt.show()
    
    plt.imshow(img, cmap="Reds")
    plt.title("Reds Colormap")
    plt.show()

"""    
# Shows a gray scale image of Lena in a Window.    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""
if __name__ == "__main__":
    main()