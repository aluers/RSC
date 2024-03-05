import cv2

cam = cv2.VideoCapture(0)

while True:
	ret, image = cam.read()
	# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# cv2.imshow('Imagetest',gray)
	cv2.imshow('Imagetest',image)
	k = cv2.waitKey(1)
	if k != -1:
		break
cv2.imwrite('./testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()