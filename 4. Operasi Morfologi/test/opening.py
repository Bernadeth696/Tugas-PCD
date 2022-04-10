import cv2 as cv2
import numpy as np

img = cv2.imread("jejak.png")
cv2.imshow("Original Image", img)
kernell = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernell)
cv2.imshow('Opening', opening)


cv2.waitKey(0)
cv2.destroyAllWindows()