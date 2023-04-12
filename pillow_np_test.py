# """Image handler method 1."""
from PIL import Image
import numpy as np
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# load the image
im = np.array(Image.open("assets/image/maze_aeral_1.jpg").convert('L'))
Image.fromarray(im).save('assets/image/maze_aeral_2.jpg')

im = np.array(Image.open("assets/image/maze_aeral_1.jpg").convert('P'))
Image.fromarray(im).save('assets/image/maze_aeral_3.jpg')


# img = cv.imread('assets/image/maze_aeral_1.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# edges = cv.Canny(img, 300, 300)
# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()

# img = cv.imread("assets/image/maze_aeral_1.jpg")

img = cv.imread("assets/image/maze_small.png")
# creating mask using thresholding over `red` channel (use better use histogram to get threshoding value)
# I have used 200 as thershoding value it can be different for different images
# ret, mask = cv.threshold(img[:, :,2], 200, 255, cv.THRESH_BINARY)

# mask3 = np.zeros_like(img)
# mask3[:, :, 0] = mask
# mask3[:, :, 1] = mask
# mask3[:, :, 2] = mask

# # extracting `orange` region using `biteise_and`
# orange = cv.bitwise_and(img, mask3)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

# # extracting non-orange region
# gray = cv.bitwise_and(img, 255 - mask3)

# # orange masked output
# out = gray + orange
# kernel = np.ones((1, 1), np.uint8)
# img_dilation = cv.dilate(img, kernel, iterations=1)
# retval, threshold = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
# plt.imshow(threshold)
plt.imshow(img)
# threshold_blur = 255 - cv.medianBlur(threshold, 5)
# plt.imshow(threshold_blur,cmap='gray', vmin = 0, vmax = 255)
# test = cv.imwrite('orange.png', orange)
# test1 = cv.imwrite('gray.png', gray)
# test2 = cv.imwrite("output.png", out)
# plt.subplot(), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.show()


