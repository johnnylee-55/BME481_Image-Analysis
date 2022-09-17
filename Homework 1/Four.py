from PIL import Image, ImageEnhance, ImageOps
import matplotlib.pyplot as plt
import numpy as np

# open image
img = Image.open("nature.JPG")
img.show()

#enhance image
#{
# enhancerB = ImageEnhance.Brightness(img)
# imgE = enhancerB.enhance(2.0).show()

# enhancerS = ImageEnhance.Sharpness(img)
# imgE = enhancerS.enhance(2.0).show()
# }

imgE = ImageOps.equalize(img, mask = None).show()

enhancerS = ImageEnhance.Sharpness(imgE)
imgS = enhancerS.enhance(2.0).show()

