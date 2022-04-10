import cv2

image1 = cv2.imread('peppers.png')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gambar Original", image1)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                             cv2.THRESH_OTSU)

cv2.imshow('Otsu Threshold', thresh1)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


