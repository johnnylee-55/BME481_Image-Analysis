from PIL import Image, ImageEnhance, ImageOps
import matplotlib.pyplot as plt
import numpy as np

# open image
img = Image.open("nature.JPG")
img.show()

# dimensions
left = 300
top = 500
right = 675
bottom = 875
# crop to dimensions
imgCropped = img.crop((left, top, right, bottom))
imgCropped.show()

# brightens image
enhancer = ImageEnhance.Brightness(imgCropped)
factor = 3 #brightens the image
imgBrightened = enhancer.enhance(factor)
imgBrightened.show()

# equalizes image
imgEqualized = ImageOps.equalize(imgBrightened, mask = None)
imgEqualized.show()