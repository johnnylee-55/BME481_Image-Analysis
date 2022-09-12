import cv2
import matplotlib.pylab as plt

#file path for Winter
path = "/Users/johnnylee/dev/python/BME_481/images/Winter.png"

#reading image as grayscale
winterGrayscale = cv2.imread(path,0)
winterColor = cv2.imread(path,1)

cv2.imshow("winterGrayscale", winterGrayscale)
cv2.imshow("winterColor", winterColor)
