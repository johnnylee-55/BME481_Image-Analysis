from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np

# read "valley.tif", apply image enhancement, and show histogram before and after
img = Image.open("valley.tif") #mac path
#img = Image.open("BME 481\valley.tif") #windows path

imgE = ImageOps.equalize(img, mask = None)

# show images
img.show()
imgE.show()

# show histograms
imgHist = np.ravel(img)
imgEHist = np.ravel(imgE)
plt.hist(imgHist, bins = 256, density = "true", alpha = 0.7, label = "source")
plt.hist(imgEHist, bins = 256, density = "true", alpha = 0.7, label = "filtered")
plt.title("Source vs Filtered")
plt.legend(loc = "upper left")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()
