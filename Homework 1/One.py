from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np

# a. open the image, display in color and grayscale
img = Image.open("Winter.png") #mac path
#img = Image.open("BME 481\Winter.png") #windows path
# display image (color)
img.show()
# display image (grayscale)
imgGray = ImageOps.grayscale(img)
imgGray.show()

# b. generate grayscale histogram, normalize
imgHist = np.ravel(imgGray)
plt.hist(imgHist, density = "true", bins = 255)
plt.title("Winter, grayscale")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()

# crop 100x100 snowy region on ground, display, generate histogram
left = 5
top = 400
right = 105
bottom = 500

# c. crops image with above parameters
imgCropped = imgGray.crop((left, top, right, bottom))
imgCropped.show()
# generates historgram of cropped image
imgCrpHst = np.ravel(imgCropped)
plt.hist(imgCrpHst, density = "true", bins = 240)
plt.title("Winter (cropped), grayscale")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()

# d. overlay the histograms of entire and cropped image 
plt.hist(imgHist, bins = 255, density = "true", alpha = 0.7, label = "full img")
plt.hist(imgCrpHst, bins = 240, density = "true", alpha = 0.7, label = "cropped img")
plt.title("Winter (full vs cropped)")
plt.legend(loc = "upper left")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()

# e. read Desert.png, convert to grayscale, display
imgDesert = Image.open("Desert.png") #mac path
#imgDesert = Image.open("BME 481\Winter.png") #windows path
imgDsrtGry = ImageOps.grayscale(imgDesert)
imgDsrtGry.show()

# f. compare histograms of b. and e. by overlapping
imgDsrtHst = np.ravel(imgDsrtGry)
plt.hist(imgHist, bins = 255, density = "true", alpha = 0.7, label = "winter")
plt.hist(imgDsrtHst, bins = 200, density = "true", alpha = 0.7, label = "desert")
plt.title("Winter vs Desert, grayscale")
plt.legend(loc = "upper left")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()
