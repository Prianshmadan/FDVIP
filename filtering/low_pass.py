
# import cv2
# import numpy as np

##AVERGING##


# img = cv2.imread('mri.jpeg',0)
# blur = cv2.boxFilter(img,-1,(5,5), normalize = True)
# # or use cv2.blur() as shown below

# # blur = cv2.blur(img,(5,5))
# img1 = cv2.hconcat([img,blur])
# cv2.imshow('img',img1)
# cv2.waitKey(0)

import cv2
import numpy as np
from skimage.util import random_noise
 
# Load an image
img = cv2.imread('cameraman.jpg')
 
# Add salt and pepper noise to the image
noise_img = random_noise(img, mode="s&p",amount=0.3)
noise_img = np.array(255*noise_img, dtype = 'uint8')

# Apply median filter
median = cv2.medianBlur(noise_img,5)
 
# Display the image
img1 = cv2.hconcat([img,noise_img,median])
cv2.imshow('img',img1)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
