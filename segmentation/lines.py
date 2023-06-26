import cv2
import numpy as np

img = cv2.imread('lines.png',0)

kernel = np.ones((2,19), np.uint8)
horizontal_lines=cv2.erode(img,kernel,iterations=1)

kernel1 = np.ones((11,3), np.uint8)
vertical_lines=cv2.erode(img,kernel1,iterations=1)
img1 = cv2.hconcat([img,vertical_lines,horizontal_lines])
cv2.imshow('original image',img1)
cv2.waitKey(0)