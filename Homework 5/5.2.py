import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
image = cv2.imread('Homework 5/Dapi_1.png', 0)
image = cv2.equalizeHist(image)
dapi = image
image = cv2.medianBlur(image, 7)
ret,image = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)

# Set our filtering parameters
# Initialize parameter setting using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params.filterByArea = True
params.minArea = 150

# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.2

# Set Convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.4
	
# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.0001

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
	
# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(image, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
