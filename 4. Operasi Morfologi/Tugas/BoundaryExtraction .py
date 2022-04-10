import cv2
import numpy as np

structure_element2 = np.ones((5,5),np.uint8)
img = cv2.imread('peppers.png')

# External Boundary Extraction
dilate = cv2.dilate(img,structure_element2,iterations = 1)
ebe = np.subtract(dilate, img)
cv2.imshow("External Boundary Extraction Original Image", img)
cv2.imshow("External Boundary Extraction Output Image", ebe)
cv2.waitKey(0)

# Internal Boundary Extraction
erode = cv2.erode(img,structure_element2,iterations = 1)
ibe = np.subtract(img,erode)
cv2.imshow("External Boundary Extraction Original Image", img)
cv2.imshow("Internal Boundary Extraction Output Image", ibe)
cv2.waitKey(0)
