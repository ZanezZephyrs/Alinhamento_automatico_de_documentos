import numpy as np
import imutils


def rotate(img, angle):
    temp = np.bitwise_not(img)
    rotate = imutils.rotate_bound(temp, angle)
    return np.bitwise_not(rotate)