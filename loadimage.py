import cv2
import numpy as np
from matplotlib import pyplot as plt

#reads image GRAYSCALE(0), COLOUR(1), UNCHANGED(-1)
img = cv2.imread('pillow.jpeg',cv2.IMREAD_COLOR)

#using opencv
cv2.imshow('image',img) #displays in window with imae written on top
cv2.waitKey(0) #waits for ay key to be pressed
cv2.destroyAllWindows() #do on key press
#cv2.imwrite('pillowgray.png',img) #save image

#using matplotlib
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic') #show image using matplotlib
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.plot([200,300,400],[100,200,300],'c', linewidth=5) #print a random line
#plt.show() #display
