import numpy as np
import cv2
img = np.fromfile('stream_000001_left_640x480_14bit.thermal.raw', dtype="<i2")
img.shape
img1 = img[:].reshape(480, 640) - 7267
cv2.imwrite('result.png', img1)


# f = open('stream_000001_left_640x480_14bit.thermal.raw', 'rb') # opening a binary file
# content = f.read() # reading all lines
# f.close()

# import imageio
# im = imageio.imread('stream_000001_left_640x480_14bit.thermal.raw')
# imageio.imwrite('result.png',im) 

