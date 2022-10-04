# Author: Johnny Lee

from PIL import Image, ImageOps
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np
import cv2

# 4. use lenna image
# a. implement a derivative of Gaussian, with sigma = 1, 3, 5, and
#    convolve with the Lenna image. Show the derivatives in the X and Y directions.
#    Compute and show magnitude with edge direction.

img = Image.open("Homework 2/images/Lenna.png")
lenna = ImageOps.grayscale(img)

# stores images for use later in the problem
imageStorageArray = []

# implements derivative of Gaussian, loops through with different values of sigma
sigmaValuesA = [1, 3, 5]
for sigma in sigmaValuesA:
    diffGaussian = ndi.gaussian_laplace(lenna, sigma)
    plt.imshow(diffGaussian)
    plt.title('Derivative of Gaussian, sigma = ' + str(sigma))
    plt.axis('off')
    plt.show()
    imageStorageArray.append(diffGaussian)

# show derivatives in x and y direction
dx = np.diff(lenna, axis = 1)
dy = np.diff(lenna, axis = 0)

# generate plot
fig = plt.figure(figsize=(10,7))

fig.add_subplot(1,2,1)
plt.imshow(dx)
plt.title('derivative in x')
plt.axis('off')
fig.add_subplot(1,2,2)
plt.imshow(dy)
plt.title('derivative in y')
plt.axis('off')

plt.show()

# compute and show magnitude with edge directions
def showEdgeMagnitudeDirection(imageStorageArray):
    # Sobel
    gaussian_dx_sigma3 = cv2.Sobel(imageStorageArray[1], cv2.CV_64F, 1, 0)
    gaussian_dy_sigma3 = cv2.Sobel(imageStorageArray[1], cv2.CV_64F, 0, 1)

    # Magnitude and Orientation
    mag_c1 = np.sqrt((gaussian_dx_sigma3 ** 2) + (gaussian_dy_sigma3 ** 2))
    orient_c1 = np.arctan2(gaussian_dy_sigma3, gaussian_dx_sigma3) * (180 / np.pi) % 180

    # generate plot
    fig = plt.figure(figsize = (10, 7))
    fig.add_subplot(1,2,1)
    plt.imshow(mag_c1)
    plt.title("Gradient Magnitude")
    fig.add_subplot(1,2,2)
    plt.imshow(orient_c1)
    plt.title("Gradient Orientations [0-180]")
    plt.show()

# 0th element -> sigma=1, 1st element -> sigma=3, 2nd element -> sigma=5 
showEdgeMagnitudeDirection(imageStorageArray)

# b. Show the zero-crossing image for sigma = 1, 2, 8.
sigmaValuesB = [1, 2, 8]
for sigma in sigmaValuesB: 
    LoG = ndi.gaussian_laplace(lenna, sigma)
    threshold = np.absolute(LoG).mean() * 0.1
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

# c. What are your insights based on a, b?
#
#    Increasing the value of sigma in the Derivative of Gaussian filter puts 
#    more weight to the sides of the filter, which produces a ‘blurring’ effect
#    and tends to also erase details in an image. As sigma increases, the DoG and
#    LoG comparisons of different sigma values reveal that edges lose strength
#    when applying a derivative of gaussian with a high sigma value.
