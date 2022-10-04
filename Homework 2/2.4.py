# Author: Johnny Lee

from PIL import Image, ImageOps
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np

# 4. use lenna image
# a. implement a derivative of Gaussian, with sigma = 1, 3, 5, and
#    convolve with the Lenna image. Show the derivatives in the X and Y diretions.
#    Compute and show magnitude with edge direction.

img = Image.open("Homework 2/images/Lenna.png")
lenna = ImageOps.grayscale(img)

# implement derivative of Gaussian
sigmaValuesA = [1, 3, 5]
for sigma in sigmaValuesA:
    diffGaussian = ndi.gaussian_laplace(lenna, sigma)
    plt.imshow(diffGaussian)
    plt.title('Deriviative of Gaussian, sigma = ' + str(sigma))
    plt.axis('off')
    plt.show()

# show derivatives in x and y direction
dx = np.diff(lenna, axis = 0)
dy = np.diff(lenna, axis = 1)

plt.imshow(dx)
plt.title('Derivative in the x direction')
plt.axis('off')
plt.show()

plt.imshow(dy)
plt.title('Derivative in the y direction')
plt.axis('off')
plt.show()

# compute and show magnitude with edge directions


# b. Show the zero-crossing image for sigma = 1, 2, 8.
sigmaValuesB = [1, 2, 8]
for sigma in sigmaValuesB: #loops through with sigma =
    LoG = ndi.gaussian_laplace(lenna, sigma)
    threshold = np.absolute(LoG).mean() * 0.75
    output = np.zeros(LoG.shape)
    width = output.shape[1]
    height = output.shape[0]

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            patch = LoG[i-1:i+2, j-1:j+2]
            p = LoG[i, j]
            max = patch.max()
            min = patch.min()
            if (p > 0):
                zeroCross = True if min < 0 else False
            else:
                zeroCross = True if max > 0 else False
            if ((max - min) > threshold) and zeroCross:
                output[i, j] = 1

    plt.imshow(output)
    plt.title('LoG, sigma = ' + str(sigma))
    plt.axis('off')
    plt.show()

# c. What is your insights based on a, b?

