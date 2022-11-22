import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Homework 5/Dapi_1.png', 0)
image = cv2.equalizeHist(image)

# calculate histogram
hist = cv2.calcHist([image],[0],None,[256],[0,256])
# plot the above computed histogram
plt.plot(hist, color='b')
plt.title('Image Histogram For Blue Channel GFG')
plt.show()

# show image
cv2.imshow("test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

