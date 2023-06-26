import cv2
import numpy as np
path = r'./cameraman.jpg'

img = cv2.imread(path,1)
img_log = (np.log(img + 1)/(np.log(1+np.max(img))))*255
# Specify the data typ0
img_log = np.array(img_log,dtype=np.uint8)
img3=cv2.hconcat([img,img_log])

cv2.imshow('img3',img3)
# cv2.imshow('log_image',img )
cv2.waitKey(0)