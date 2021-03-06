import numpy as np
import cv2
import copy

# Defaults to webcam
cap = cv2.VideoCapture(0)

# Create Window
cv2.namedWindow('tiny')

# Callback function for user input
def nothing(x):
    pass

# User input
cv2.createTrackbar('tiny', 'tiny', 0, 10, nothing)
cv2.createTrackbar('interpolation', 'tiny', 0, 4, nothing)

# Video loop
while(True):

    # Capture image
    ret, frame = cap.read()

    # Resize image
    frame = cv2.resize(frame, None, fx=0.2, fy=0.2)

    # Query user input
    tiny = (cv2.getTrackbarPos('tiny', 'tiny')+1)*5.0 / 100.0 # odd
    inter = cv2.getTrackbarPos('interpolation', 'tiny')
    if inter == 0:
        inter = cv2.INTER_LINEAR
    elif inter == 1:
        inter = cv2.INTER_AREA
    elif inter == 2:
        inter = cv2.INTER_CUBIC
    elif inter == 3:
        inter = cv2.INTER_LINEAR


    # Process images
    color = cv2.resize(frame, None, fx=tiny, fy=tiny, interpolation=inter)
    gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
    r,c,d = frame.shape
    color = cv2.resize(color, (c,r), interpolation=inter)
    gray = cv2.resize(gray, (c,r), interpolation=inter)

    # Collect images
    r,c,d = frame.shape
    images = np.zeros((r,c*2,d), np.uint8)
    images[0:r,0:c,0:3] = color
    images[0:r,c:c*2,0:3] = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    # Display images
    cv2.imshow('tiny', images)
    
    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
