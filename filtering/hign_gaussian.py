
import cv2
  
img = cv2.imread("cameraman.jpg")
img = cv2.resize(img, (500,500), 
                 interpolation=cv2.INTER_CUBIC)
  

# after subtracting add 127 to the total result
hpf = img - cv2.GaussianBlur(img, (21, 21), 3)+127
  
# display both original image and filtered image

img1 = cv2.hconcat([img,hpf])
cv2.imshow('img',img1)
  
cv2.waitKey(0)
cv2.destroyAllWindows()