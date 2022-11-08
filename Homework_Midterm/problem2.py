## Examine the image called HE_Brain.bmp. It is a tissue section that has been stained with 
## two dye for labeling nuclei in blue and protein in pink. Your task is to decompose this image into 
## its basis or fundamental colors. You can reduce the size of the image to make memory and 
## computation manageable.

import numpy as np
import matplotlib.pyplot as plt 
from sklearn import decomposition
from PIL import Image, ImageOps

brain = Image.open("Homework_Midterm/HE_Brain.bmp")
img = ImageOps.grayscale(brain)

## Apply NMF (e.g, V = WH) by randomly initializing W and H. Do this 3 times. Display 
## the basis images. Are results consistent?

# plots bases W, H next to their product V
def plot3figs(img1, title1, img2, title2, img3, title3):
    fig = plt.figure(figsize = (11, 8))
    
    imgArr = [img1, img2, img3]
    titleArr = [title1, title2, title3]

    arr = [0, 1 ,2]
    for i in arr:
        fig.add_subplot(1,3,i+1)
        plt.imshow(imgArr[i])
        plt.title(titleArr[i])
        plt.axis('off')
    
    plt.show()

# performs NMF on image 3 times, each with randomly initalized W & H matrices
for i in range(3):
    estimator = decomposition.NMF(n_components = 15, init = 'random', tol=5e-3)    
    W = estimator.fit_transform(img)
    H = estimator.components_
    V = np.dot(W, H)
    plot3figs(W, "W basis", H, "H basis", V, "V = WH")

# results seem consistent, although there are slight differences in the value of the color
# in the reconstructed images.

## Now lets’s initialize the matrix W with some prior knowledge. How would you do this? 
## You can move the cursor over the image manually, read the values, and substitute in W 
## or you may want to take advantage of a precomputed mask, named HE_Brain_mask.bmp.

