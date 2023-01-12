# """Image handler method 1."""
from PIL import Image
import numpy as np
# load the image

im = np.array(Image.open("assets/image/maze_aeral_1.jpg").convert('L')) 
print(type(im))
print(im)

Image.fromarray(im).save('assets/image/maze_aeral_2.jpg')


# """Image handler method 2."""
# from matplotlib import image
# from matplotlib import pyplot

# image = image.imread("assets/image/maze_example_1.jpg")
# print(image.dtype)
# print(image.shape)

# pyplot.imshow(image)
# pyplot.show()