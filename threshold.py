import cv2
import numpy as np

#thresold is basically either black or white
img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12 , 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12 , 255, cv2.THRESH_BINARY)
#second last arguments is clarity and last argument is contrast
gaus=cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)
cv2.imshow('1', img)
cv2.imshow('2', gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()

