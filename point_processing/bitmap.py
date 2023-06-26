import cv2
import numpy as np

# Load input image
img1 = cv2.imread("space.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img1, (300,350), 
                 interpolation=cv2.INTER_CUBIC)
# Get image dimensions
w, h = img.shape

# Initialize eight new images with same dimensions as input image
img1 = np.zeros([w, h, 3], dtype=np.uint8)
img2 = np.zeros([w, h, 3], dtype=np.uint8)
img3 = np.zeros([w, h, 3], dtype=np.uint8)
img4 = np.zeros([w, h, 3], dtype=np.uint8)
img5 = np.zeros([w, h, 3], dtype=np.uint8)
img6 = np.zeros([w, h, 3], dtype=np.uint8)
img7 = np.zeros([w, h, 3], dtype=np.uint8)
img8 = np.zeros([w, h, 3], dtype=np.uint8)

# Define function to extract bit value at a given position
def bitget(nbr, pos):
    return (nbr >> pos) & 1

# Apply bit plane slicing to input image
planes = 8
for i in range(0, w):
    for j in range(0, h):
        for p in range(planes - 1):
            if p == 7:
                img1[i][j] = 255 * bitget(img[i][j], p)
            elif p == 6:
                img2[i][j] = 255 * bitget(img[i][j], p)
            elif p == 5:
                img3[i][j] = 255 * bitget(img[i][j], p)
            elif p == 4:
                img4[i][j] = 255 * bitget(img[i][j], p)
            elif p == 3:
                img5[i][j] = 255 * bitget(img[i][j], p)
            elif p == 2:
                img6[i][j] = 255 * bitget(img[i][j], p)
            elif p == 1:
                img7[i][j] = 255 * bitget(img[i][j], p)
            else:
                img8[i][j] = 255 * bitget(img[i][j], p)

# Display resulting eight images
cv2.imshow("Bit Plane 1", img1)
cv2.imshow("Bit Plane 2", img2)
cv2.imshow("Bit Plane 3", img3)
cv2.imshow("Bit Plane 4", img4)
cv2.imshow("Bit Plane 5", img5)
cv2.imshow("Bit Plane 6", img6)
cv2.imshow("Bit Plane 7", img7)
cv2.imshow("Bit Plane 8", img8)


# Wait for user input to close window
cv2.waitKey(0)
cv2.destroyAllWindows()
