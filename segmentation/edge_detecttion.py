import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('tiger.jpg', 0)


edges = cv2.Canny(img, 100, 200)

img1 = cv2.hconcat([img,edges])
cv2.imshow('edge',img1)
cv2.waitKey(0)
