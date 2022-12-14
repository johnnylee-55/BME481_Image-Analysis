import cv2
import numpy as np

# reads image
hwy = cv2.imread('Homework 4/HWY447.png')

# converts color image to grayscale
gray = cv2.cvtColor(hwy, cv2.COLOR_BGR2GRAY)

# applies median blur to remove background noise
blur = cv2.medianBlur(gray,5)

# canny edge detection, Canny(image source, minimum threshold, maximum threshold)
edges = cv2.Canny(blur, 80, 110)

# applies probabilistic hough line transform method on 'edges' to obtain line end points
# returns list of endpoints for each line, with each element in the array being 4 integers (x1, y1, x2, y2)
lines = cv2.HoughLinesP(
            edges,
            1, # Distance resolution in pixels
            np.pi / 180, # Angle resolution in radians
            threshold = 120, # Min number of votes for valid line
            minLineLength = 30, # Min allowed length of line
            maxLineGap = 120 # Max allowed gap between line for joining them
            )

# iterates over lines, connects endpoints by drawing lines, adds endpoints to new array lines_array
linesArray = []
for points in lines:
    # Extracted points nested in the array
    x1,y1,x2,y2 = points[0]

    # Draw the lines joing the points on the original image 'hwy'
    cv2.line(hwy, (x1,y1), (x2,y2), (0,0,255), 2)

# prints all endpoints in lines array
print(lines)

# Save the result image as 'detectedLines.png'
cv2.imwrite('Homework 4/detectedLines.png',hwy)

# draws line for path to be taken
# "destination" point found by analyzing endpoints
cv2.line(hwy, (int(hwy.shape[0]/2), int(hwy.shape[1])), (286, 7), (0,255,0), 2)
cv2.imwrite('Homework 4/pathDrawn.png',hwy)