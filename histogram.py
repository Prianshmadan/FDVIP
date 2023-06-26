import matplotlib.pyplot as plt 
import cv2
# img1 = plt.imread('cameraman.jpg',0)

# img = cv2.equalizeHist(img1)
# histg = cv2.calcHist([img],[0],None,[256],[0,256])
# plt.hist(img.ravel(),256,[0,256])

# cv2.imshow('img3',img)
# plt.plot(histg)

# plt.show()
import numpy as np
alpha = 1.0 # Simple contrast control
beta = 0 
# Read the image
image = cv2.imread('space.png',1)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
cv.imshow('Original Image', image)
# cv.imshow('New Image', new_image)
# Wait until user press some key
cv.waitKey()