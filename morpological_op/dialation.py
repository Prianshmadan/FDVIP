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



top_row = cv2.hconcat([cv2.putText(binr, "binary image", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2),
cv2.putText(dilation, "dilation", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2),cv2.putText(erosion, "erosion", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
])

bottom_row = cv2.hconcat([cv2.putText(invert, "inverted", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2),
cv2.putText(dilation_i, "dilation_ivverted", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2),
cv2.putText(erosion_i, "erosion_inverted", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,0,0), 2)])
result = cv2.vconcat([top_row, bottom_row])
cv2.imshow('Result', result)



cv2.waitKey(0)