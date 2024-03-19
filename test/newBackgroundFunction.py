import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
backSub = cv2.createBackgroundSubtractorMOG2()
ret, frame = cap.read()

prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
if not cap.isOpened():
	print("Error opening video file")

while cap.isOpened():
	# Capture frame-by-frame
	ret, frame = cap.read()
	if ret:
		# cv2.imshow('Original Image', frame)

		#Resize
		height, width, channels = frame.shape
		down_width = int(width/2)
		down_height = int(height/2)
		down_points = (down_width, down_height)
		resized_down = cv2.resize(frame, down_points, interpolation= cv2.INTER_LINEAR)
		#cv2.imshow('Scaled down', resized_down)
		
		img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		diff = cv2.absdiff(img_gray, prev_gray)
		# Apply background subtraction
		#fg_mask = backSub.apply(resized_down)
		fg_mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

		prev_gray = img_gray
		#cv2.imshow('FG Mask', fg_mask)

		# Find contours
		contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		# print(contours)
		frame_ct = cv2.drawContours(resized_down, contours, -1, (0, 255, 0), 2)
		# Display the resulting frame
		cv2.imshow('Frame_final', frame_ct)


		# apply global threshold to remove shadows
		retval, mask_thresh = cv2.threshold( fg_mask, 180, 255, cv2.THRESH_BINARY)

		# "Erode" white areas.  Basically, get rid of any wires that stick out of the object.
		kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
		mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)


		#Draw bounding boxes:

		#Set size limit for white areas.
		min_contour_area = 500  # Define your minimum area threshold
		large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

		frame_out = resized_down.copy()
		for cnt in large_contours:
			x, y, w, h = cv2.boundingRect(cnt)
			frame_out = cv2.rectangle(resized_down, (x, y), (x+w, y+h), (0, 0, 200), 3)
		
		# Display the resulting frame
		cv2.imshow('Bounding boxes', frame_out)

	#Break	
	k = cv2.waitKey(1)
	if k != -1:
		break
	
cap.release()
cv2.destroyAllWindows()
