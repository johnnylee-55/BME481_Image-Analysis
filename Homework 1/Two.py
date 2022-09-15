from PIL import Image, ImageOps

# i) covert image to grayscale
img = Image.open("Lenna.png") #mac path
#img = Image.open("BME 481\Lenna.png") #windows path
imgGray = ImageOps.grayscale(img)

# ii) downsample the image by three levels
for x in range(3):
    width, height = imgGray.size
    newSize = (width//2, height//2)
    imgGray = imgGray.resize(newSize)
    imgGray.show()
