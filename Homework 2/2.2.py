from PIL import Image, ImageFilter
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 2) generate a synthetic image
synthImg = Image.new( mode = "L", size = (150, 150), color = (50) )
foreground = Image.new( mode = "L", size = (75, 75), color = (150) )

synthImg.paste(foreground, (75//2, 75//2), mask = foreground)

synthImg.show()


