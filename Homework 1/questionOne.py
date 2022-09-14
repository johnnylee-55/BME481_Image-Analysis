from PIL import Image,ImageOps
import matplotlib.pyplot as plt
import cv2
import numpy as np

#open the image
#mac
img = Image.open("Winter.png")
#windows
#img = Image.open([enter filepath here])

#color
img.show()
#gray
imgGray = ImageOps.grayscale(img)
imgGray.show()

#plot grayscale histogram
