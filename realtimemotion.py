import cv2

# Function to resize the input image
def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error opening video file")

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret:
        # Resize the frame
        resized_frame = resize_image(frame, 50)  # Downscale by 50%
        
        # Display the resized frame
        cv2.imshow('Resized Frame', resized_frame)
    
    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
