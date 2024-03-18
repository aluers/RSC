import cv2
import numpy as np

# Function to downscale the image
def downscale_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

# Function to create a difference mask
def create_difference_mask(prev_frame, current_frame):
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    diff_mask = cv2.absdiff(prev_gray, current_gray)
    _, diff_mask = cv2.threshold(diff_mask, 30, 255, cv2.THRESH_BINARY)
    return diff_mask

# Function to detect motion boxes
def detect_motion_boxes(diff_mask):
    contours, _ = cv2.findContours(diff_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    motion_boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        motion_boxes.append((x, y, x + w, y + h))
    return motion_boxes

# Function to upscale motion boxes and highlight motion
def highlight_motion(image, motion_boxes, scale_percent):
    for box in motion_boxes:
        scaled_box = [int(coord * (100 / scale_percent)) for coord in box]
        cv2.rectangle(image, (scaled_box[0], scaled_box[1]), (scaled_box[2], scaled_box[3]), (0, 255, 0), 2)

cap = cv2.VideoCapture(0)
backSub = cv2.createBackgroundSubtractorMOG2()

if not cap.isOpened():
    print("Error opening video file")

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        # Downscale the frame
        downscaled_frame = downscale_image(frame, 50)  # Downscale by 50%
        
        # Apply background subtraction
        fg_mask = backSub.apply(downscaled_frame)
        
        # Create difference mask
        diff_mask = create_difference_mask(downscaled_frame, downscaled_frame)
        
        # Detect motion boxes
        motion_boxes = detect_motion_boxes(diff_mask)
        
        # Highlight motion on original image
        highlight_motion(frame, motion_boxes, 50)  # Upscale motion boxes by 50%
        
        # Display the resulting frame
        cv2.imshow('Motion Detection', frame)
        
    k = cv2.waitKey(1)
    if k != -1:
        break

cap.release()
cv2.destroyAllWindows()
