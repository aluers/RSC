# let's start with the Imports 
import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
	ret, image = cam.read()
	height, width, channels = image.shape
	#print("Original Height and Width:", height,"x", width)
	cv2.imshow('Original Image', image)
	
	# let's downscale the image using new  width and height
	down_width = int(width/2)
	down_height = int(height/2)
	down_points = (down_width, down_height)
	resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
	
	# let's upscale the image using new  width and height
	up_width = int(width*1.5)
	up_height = int(height*1.5)
	up_points = (up_width, up_height)
	resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)
	
	# Display images
	cv2.imshow('Resized Down by defining height and width', resized_down)
	cv2.imshow('Resized Up image by defining height and width', resized_up)

	k = cv2.waitKey(1)
	if k != -1:
		break
	
cam.release()
cv2.destroyAllWindows()