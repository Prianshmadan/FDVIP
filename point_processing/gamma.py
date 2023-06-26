import cv2
import numpy as np
  
# Open the image.
img = cv2.imread('space.png',0)
  
# Trying 4 gamma values.
for gamma in [0.1, 0.8,1.5,2.4]:
      
    # Apply gamma correction.
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
  
    # Save edited images.
    cv2.imwrite(''+str(gamma)+'.jpg', gamma_corrected)
    

cv2.waitKey(0)