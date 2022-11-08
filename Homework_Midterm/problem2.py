## Examine the image called HE_Brain.bmp. It is a tissue section that has been stained with 
## two dye for labeling nuclei in blue and protein in pink. Your task is to decompose this image into 
## its basis or fundamental colors. You can reduce the size of the image to make memory and 
## computation manageable.

import cv2
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import decomposition

# reads images
brain = cv2.imread("Homework_Midterm/HE_Brain.bmp")
maskB = cv2.imread('Homework_Midterm/HE_Brain_mask.bmp',0)

# grabs blue color channel by applying mask to original image, coverts to grayscale after
blueChannel = cv2.bitwise_and(brain, brain, mask = maskB)
blueChannel = cv2.cvtColor(blueChannel, cv2.COLOR_BGR2GRAY)


# grabs pink color chanel by applying inverted mask for blue channel
maskP = cv2.bitwise_not(maskB)
pinkChannel = cv2.bitwise_and(brain, brain, mask = maskP)
pinkChannel = cv2.cvtColor(pinkChannel, cv2.COLOR_BGR2GRAY)


## Apply NMF (e.g, V = WH) by randomly initializing W and H. Do this 3 times. Display 
## the basis images. Are results consistent?

#
# plots bases W, H and then their product V
#
def plotfigs(img1, title1, img2, title2, img3, title3):
    fig = plt.figure(figsize = (14, 8))

    imgArr = [img1, img2, img3]
    titleArr = [title1, title2, title3]

    for i in range(2):
        fig.add_subplot(1,2,i+1)
        plt.imshow(imgArr[i])
        plt.title(titleArr[i])
        plt.axis('off')
    plt.show()

    plt.figure()
    plt.imshow(img3)
    plt.title(title3)
    plt.show()

# 
# performs NMF on image 3 times, each with randomly initalized W & H matrices
#
def nmfRandInit(img):
    estimator = decomposition.NMF(n_components = 20, init = 'random', tol=5e-3)    
    W = estimator.fit_transform(img)
    H = estimator.components_
    V = np.dot(W, H)
    plotfigs(W, "W basis", H, "H basis", V, "V = WH")

#
# performs NMF on blue color channel 3 times, plots each result
#
for i in range(3):
    nmfRandInit(blueChannel)

#
# performs NMF on pink color channel
#
for i in range(3):
    nmfRandInit(pinkChannel)

# results seem consistent, although there are slight differences in the value of the color
# in the reconstructed images in each iteration. However, there were differences in 
# processing speeds when cycling through random initializations.

## Now lets’s initialize the matrix W with some prior knowledge. How would you do this? 
## You can move the cursor over the image manually, read the values, and substitute in W 
## or you may want to take advantage of a precomputed mask, named HE_Brain_mask.bmp.

# Some "prior knowledge" that would aid in selecting a good intialization of W include:
# - setting the dimensions of W to reflect the number of bases and number of color channels
#      - number of bases (eigenvectors) used set to 20
#      - number of color channels is 1, each color channel was split from original image and grayscaled
# A good initialization of W allows for the algorithm to run more effciently and output a better result

def nmfManualInit(img, WInit, HInit):
    estimator = decomposition.NMF(n_components = 20, init = 'custom')    
    W = estimator.fit_transform(img, y = None, W = WInit, H = HInit)
    H = estimator.components_
    V = np.dot(W, H)
    plotfigs(W, "W basis", H, "H basis", V, "V = WH")

WInit = [] # an array of size 1x20
HInit = [] # an array of size 20x1072 (image length)
