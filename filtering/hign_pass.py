import cv2
import numpy as np

img=cv2.imread('car.jpg')
# cv2.imshow('Original Image',img)

#3x3 mask
mask=np.array([[-1,-1,-1],
               [-1,8,-1],
               [-1,-1,-1]])

# # 5x5 mask
# mask=np.array([[-1,-1,-1,-1,-1],
#                [-1,-1,-1,-1,-1],
#                [-1,-1,24,-1,-1],
#                [-1,-1,-1,-1,-1],
#                [-1,-1,-1,-1,-1]])

mask=mask/sum(mask)

img_fil=cv2.filter2D(img,-1,mask)
cv2.imshow('original img',img)
cv2.imshow('filtered img',img_fil)
cv2.waitKey(0)