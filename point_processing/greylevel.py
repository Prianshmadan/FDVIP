import cv2
import numpy as np
  
# Open the image.
img = cv2.imread('space.png',0)
[w,h]=img.shape

for i in range(0,w):
    for j in range(0,h):
        if img[i][j]>100 and img[i][j]<200:
            img[i][j]=210
        else:
            img[i][j]=0

cv2.imshow('img',img)
cv2.waitKey(0)