# Consider the image named gland.jpg and cows.jpg
# a. Apply Gaussian filter with sigma = 1.2, 2.4, 4.8 to smooth the image and show the results.
# b. Apply Anisotropic filter and show the results with the same sigma.
#   **note** sigma is not applicable with the anisotropic filter
#            will update code when further instructions are released
# c. Comment on your results in a-b with respect to edge preservation.

import cv2
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from medpy.filter.smoothing import anisotropic_diffusion
import numpy as np

# reads and returns image in grayscale
def ReadAndGrayscale(imgPath):
    img = cv2.imread(imgPath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


gland = ReadAndGrayscale("Homework 5/gland.jpg")
cows = ReadAndGrayscale("Homework 5/cows.jpg")


# applies gaussian filter to an image, shows images filtered with sigma values passed in as a list
def applyAndDisplayGaussian(image, sigmaValues):
    for sigma in sigmaValues:
        result = ndi.gaussian_filter(image, sigma)
        plt.imshow(result)
        plt.title('Gaussian filter, sigma = ' + str(sigma))
        plt.axis('off')
        plt.show()


# list of sigma values
sigmaValues = [1.2, 2.4, 4.8]


# a. Apply Gaussian filter with sigma = 1.2, 2.4, 4.8 to smooth the image and show the results.
applyAndDisplayGaussian(gland, sigmaValues)
applyAndDisplayGaussian(cows, sigmaValues)


# applies anisotropic filter to an image then shows image
def applyAndDisplayAnisotropic(image):
    result = anisotropic_diffusion(image)
    plt.imshow(result)
    plt.title('Anisotropic filter')
    plt.axis('off')
    plt.show()


# b. Apply Anisotropic filter and show the results with the same sigma.
#   **note** sigma is not applicable with the anisotropic filter
#            will update code when further instructions are released
applyAndDisplayAnisotropic(gland)
applyAndDisplayAnisotropic(cows)
