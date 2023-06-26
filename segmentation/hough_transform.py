import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('tiger.jpg', 0)
img1 = cv2.imread('tiger.jpg', 0)

edges = cv2.Canny(img, 100, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, maxLineGap=250)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)


img2 = cv2.hconcat([img1,img,edges])
cv2.imshow('edge',img2)
cv2.waitKey(0)
