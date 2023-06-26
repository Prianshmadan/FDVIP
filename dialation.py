import cv2
import numpy as np

img=cv2.imread('mri.jpeg',0)
# cv2.imshow('Original Image',img)

binr=cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# define the kernel 
kernel = np.ones((3,3), np.uint8)

# invert the image
dilation = cv2.dilate(binr,kernel,iterations=1)
erosion = cv2.erode(binr,kernel,iterations=1)
invert = cv2.bitwise_not(binr)
dilation_i = cv2.dilate(invert,kernel,iterations=1)
erosion_i = cv2.erode(invert,kernel,iterations=1)
img1 = cv2.hconcat([binr,dilation,erosion])
img2 = cv2.hconcat([invert,dilation_i,erosion_i])
img3 = cv2.vconcat([img1,img2])



cv2.imshow('dilated image', img3)
cv2.waitKey(0)