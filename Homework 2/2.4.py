# Author: Johnny Lee

from PIL import Image, ImageOps
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np
import cv2

# 4. use lenna image
# a. implement a derivative of Gaussian, with sigma = 1, 3, 5, and
#    convolve with the Lenna image. Show the derivatives in the X and Y diretions.
#    Compute and show magnitude with edge direction.

img = Image.open("Homework 2/images/Lenna.png")
lenna = ImageOps.grayscale(img)

# implement derivative of Gaussian
imageStorageArray = []

sigmaValuesA = [1, 3, 5]
for sigma in sigmaValuesA:
    diffGaussian = ndi.gaussian_laplace(lenna, sigma)
    plt.imshow(diffGaussian)
    plt.title('Deriviative of Gaussian, sigma = ' + str(sigma))
    plt.axis('off')
    plt.show()
    imageStorageArray.append(diffGaussian)
    

# show derivatives in x and y direction
dx = np.diff(lenna, axis = 1)
dy = np.diff(lenna, axis = 0)

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
#Sobel
gx_s = cv2.Sobel(imageStorageArray[0], cv2.CV_64F, 1, 0)
gy_s = cv2.Sobel(imageStorageArray[0], cv2.CV_64F, 0, 1)
gx_c1 = cv2.Sobel(imageStorageArray[1], cv2.CV_64F, 1, 0)
gy_c1 = cv2.Sobel(imageStorageArray[1], cv2.CV_64F, 0, 1)
gx_c2 = cv2.Sobel(imageStorageArray[2], cv2.CV_64F, 1, 0)
gy_c2 = cv2.Sobel(imageStorageArray[2], cv2.CV_64F, 0, 1)

#Magnitude and Orientation
mag_s = np.sqrt((gx_s ** 2) + (gy_s ** 2))
orient_s = np.arctan2(gy_s, gx_s) * (180 / np.pi) % 180
mag_c1 = np.sqrt((gx_c1 ** 2) + (gy_c1 ** 2))
orient_c1 = np.arctan2(gy_c1, gx_c1) * (180 / np.pi) % 180
mag_c2 = np.sqrt((gx_c2 ** 2) + (gy_c2 ** 2))
orient_c2 = np.arctan2(gy_c2, gx_c2) * (180 / np.pi) % 180

##Synth Plot
(fig, axs) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
axs[0].imshow(mag_c1, cmap="jet")
axs[1].imshow(orient_c1, cmap="jet")
#Title
axs[0].set_title("Gradient Magnitude")
axs[1].set_title("Gradient Orientation [0, 180]")
for i in range(0, 2):
	axs[i].get_xaxis().set_ticks([])
	axs[i].get_yaxis().set_ticks([])
plt.tight_layout()
plt.show()

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
#
#    I would say that if the user wanted to use this the DoG
#    for edge detection, a value for sigma should be between
#    1 and 3. 