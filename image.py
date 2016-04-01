import colorsys
import Image
import numpy as np

limit = 9000
image=Image.open("lisa.jpg")

x, y = (image > limit).nonzero()
vals = image[x, y]

print vals
#colorsys.rgb_to_hsv()