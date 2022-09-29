from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# 2) generate a synthetic image
synthImg = Image.new( mode = "RGB", size = (150, 150), color = (250, 0, 0) )
synthImg.show()