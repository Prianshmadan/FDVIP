import cv2
import numpy as np

img=cv2.imread('new.jpg')
# cv2.imshow('Original Image',img)

binr=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# define the kernel 

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
opening = cv2.morphologyEx(binr, cv2.MORPH_OPEN, kernel,iterations=10)
closing = cv2.morphologyEx(binr, cv2.MORPH_CLOSE, kernel,iterations=10)
img3 = cv2.hconcat([img,opening,closing])

cv2.imshow('dilated image', img3)
cv2.waitKey(0)
