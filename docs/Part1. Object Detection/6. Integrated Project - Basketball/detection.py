import cv2
import numpy as np

im = cv2.imread('data\\ball_3.jpg')

# convert to HSV space
im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
# take only the orange, highly saturated, and bright parts
im_hsv = cv2.inRange(im_hsv, (7,180,180), (11,255,255))

# To show the detected orange parts:
im_orange = im.copy()
im_orange[im_hsv==0] = 0
# cv2.imshow('im_orange',im_orange)

# Perform opening to remove smaller elements
element = np.ones((5,5)).astype(np.uint8)
im_hsv = cv2.erode(im_hsv, element)
im_hsv = cv2.dilate(im_hsv, element)

points = np.dstack(np.where(im_hsv>0)).astype(np.float32)
# fit a bounding circle to the orange points
center, radius = cv2.minEnclosingCircle(points)
# draw this circle
cv2.circle(im, (int(center[1]), int(center[0])), int(radius), (255,0,0), thickness=3)

out = np.vstack([im_orange,im])
cv2.imwrite('out.png',out)