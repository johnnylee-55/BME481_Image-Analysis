from PIL import Image,ImageOps
import matplotlib.pyplot as plt
import numpy as np



#open the image
#mac
#img = Image.open("Winter.png")
#windows
img = Image.open("BME 481\Winter.png")

#color
img.show()
#gray
imgGray = ImageOps.grayscale(img)
imgGray.show()


#plot grayscale histogram
imgGrayR = np.ravel(imgGray)
plt.hist(imgGrayR, 256, [0, 255])
