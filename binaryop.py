import cv2


import numpy as np 
     
# path to input images are specified and   
# images are loaded with imread command  
img1 = cv2.imread('blck1.png')  
img2 = cv2.imread('white.png') 
  
dest1 = cv2.bitwise_and(img2, img1, mask = None)
dest2 = cv2.bitwise_or(img2, img1, mask = None)
dest3 = cv2.bitwise_xor(img2, img1, mask = None)
dest4 = cv2.bitwise_not(img2, mask = None)
top_row = cv2.hconcat([cv2.putText(img1, "img1", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2),
cv2.putText(img2, "img2", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2),cv2.putText(dest1, "Bitwise_and", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
])

bottom_row = cv2.hconcat([cv2.putText(dest2, "Bitwise_or", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2),
cv2.putText(dest3, "Bitwise_xor", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2),
cv2.putText(dest4, "Bitwise_not", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,0,0), 2)])
result = cv2.vconcat([top_row, bottom_row])
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
# De-allocate any associated memory usage  
cv2.waitKey(0)  
#     cv2.destroyAllWindows() 