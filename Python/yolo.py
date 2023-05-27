# import required packages
import cv2
import argparse
import numpy as np

cap = cv2.VideoCapture(0) #get image from camera

while True:
	ret, frame = cap.read()
	
	
	
	# Display
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()