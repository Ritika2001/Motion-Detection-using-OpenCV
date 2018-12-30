import cv2
import numpy as np

img = cv2.imread('veggies.jpg',cv2.IMREAD_COLOR)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,0,100])
upper_red = np.array([10,255,255])
    
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

edges = cv2.Canny(img,100,200)
cv2.imshow('Edges',edges)
image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.imshow('contour',image)
cont = cv2.drawContours(img, contours, -1, (255,0,0), 1)
cv2.imshow('contours', cont)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
