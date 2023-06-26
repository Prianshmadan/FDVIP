import cv2
  
# path
path = r'./cameraman.jpg'
  
img = cv2.imread(path, 0)
img1 = cv2.resize(img, (300,300), 
                 interpolation=cv2.INTER_CUBIC)
# Window name in which image is displayed
window_name = 'image'

img2= cv2.rotate(img1, cv2.ROTATE_180)

img11 = cv2.add(img1, img2)
img12= cv2.subtract(img1, img2)
img13 = cv2.multiply(img1, img2)
img14=cv2.multiply(img1, 1.5)
img15=cv2.divide(img1, 2.5)
img16 = cv2.divide(img1, img2)
# Displaying the image
top_row = cv2.hconcat([cv2.putText(img1, "Original Image", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2),
cv2.putText(img2, "Rotated Image", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2),cv2.putText(img11, "Addition", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2),
cv2.putText(img12, "Subtraction", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)])
bottom_row = cv2.hconcat([cv2.putText(img13, "Multiplication", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2),
cv2.putText(img14, "Multiply by 1.5", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2),
cv2.putText(img15, "Divide by 2.5", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2),
cv2.putText(img16, "Division", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)])
result = cv2.vconcat([top_row, bottom_row])
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()