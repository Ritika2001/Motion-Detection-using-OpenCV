import cv2

img = cv2.imread('image.png',cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscaled', gray)

blur = cv2.GaussianBlur(img,(15,15),0)
cv2.imshow('Gaussian Blurring',blur)

median = cv2.medianBlur(img,15)
cv2.imshow('Median Blur',median)

#bilFilter = cv2.bilateralFilter(img,9,75,75) 
#cv2.imshow('Bilateral Blur', bilFilter) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 


