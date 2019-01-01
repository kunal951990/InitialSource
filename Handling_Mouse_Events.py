# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:27:18 2018

@author: kisku
"""

"""cv2.setMouseCallback() is used to handle Mouse events"""

#import numpy as np
#import cv2
#
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print (events)

import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(2,255,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(0)