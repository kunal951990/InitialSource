# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 00:11:47 2018

@author: kisku
"""

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('hh.jpg',0)

#It wont show any image but will display 'None' if image is not read by imread()
#It will show the matrix if image is read by imread()
print (img)

#To Display an image
cv2.imshow('cv2.WINDOW_NORMAL',img)
cv2.waitKey(0)

#Below code is will destroy all image windows with passing '0'
cv2.destroyAllWindows()
cv2.waitKey(0)

#To Display an image
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)

#To Close an image window, follow destroyWindow with 
#waitKey and give any alphabet or number, after image window is opened
#press the key given in waitKey, it will close the image window
#cv2.destroyWindow('image') 
#cv2.waitKey(a)

#Below program loads an image in grayscale, displays it, 
#save the image if you press ‘s’ and exit, or simply exit without saving
#if you press ESC key.

#k = cv2.waitKey(0)
#if k == 27:         # wait for ESC key to exit
#    cv2.destroyAllWindows()
#elif k == ord('s'): # wait for 's' key to save and exit
#    cv2.imwrite('messigray.png',img)
#    cv2.destroyAllWindows()


