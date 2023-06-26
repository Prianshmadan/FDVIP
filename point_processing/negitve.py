import cv2
import numpy as np 
# path
path = r'./car.jpg'

img1 = cv2.imread(path,0)
img = cv2.resize(img1, (300,350), 
                 interpolation=cv2.INTER_CUBIC)
# Check the datatype of the image
print(img.dtype)
# Subtract the img from max value(calculated from dtype)
img2 = 255 - img
# Show the image
img3 = cv2.hconcat([img,img2])
cv2.imshow('negative',img3)
cv2.waitKey(0)