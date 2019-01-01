# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:24:12 2018

@author: kisku
"""

import numpy as np
import cv2

#Create a black image
img = np.zeros((512,512,3), np.uint8)


"""To draw a line, you need to pass starting and ending coordinates of line. 
We will create a black image and draw a blue line on it from top-left to bottom-right corners.
Draw a diagonal blue line with thickness of 5 px"""
#img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

"""To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. 
This time we will draw a green rectangle at the top-right corner of image.
Draw a rectangle"""
#img = cv2.rectangle(img,(512,512),(128,128),(255,0,0),3)

"""To draw a circle, you need its center coordinates and radius. 
We will draw a circle inside the rectangle drawn above."""
#img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

"""One argument is the center location (x,y). 
Next argument is axes lengths (major axis length, minor axis length). 
Angle is the angle of rotation of ellipse in anti-clockwise direction. 
StartAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis. 
i.e. giving values 0 and 360 gives the full ellipse."""
#img = cv2.ellipse(img,(256,256),(100,50),0,360,180,255,-1)


""" draw a polygon, first you need coordinates of vertices. 
Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and 
it should be of type int32. Here we draw a small polygon of with four vertices in yellow color."""
#pts = np.array([[150,30],[100,50],[200,50],[200,10],[100,10]], np.int32)
#pts = pts.reshape((-1,1,2))
#img = cv2.polylines(img,[pts],True,(0,255,255))

"""Adding Text to Images:
It will be done by cv2.putText()"""
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Kunal',(50,250), font, 4,(0,255,255),2,cv2.LINE_AA)

cv2.imshow('Frame',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.waitKey(0)