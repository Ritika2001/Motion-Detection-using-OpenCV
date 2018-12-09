import numpy as np
import cv2

cap = cv2.VideoCapture(0) #return value from first webcam
#fourcc = cv2.VideoWriter_fourcc(*'XVID') #codec used
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480)) #output file specs
 
while(True): #starts infinite loop
    ret, frame = cap.read() #ret, frame deines as cap.read, ret whether there was retun and frame is actual frame returned 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts to grayscale
    #out.write(frame) #write to output video
    cv2.imshow('frame',frame) #show video or image
    cv2.imshow('gray',gray) #show video or image	
    if cv2.waitKey(1) & 0xFF == ord('q'): #waits for key q to be pressed. of pressed, break
        break

cap.release() #releases webcam
#out.release()
cv2.destroyAllWindows() 
