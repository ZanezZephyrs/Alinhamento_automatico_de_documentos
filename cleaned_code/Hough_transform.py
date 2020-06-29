from skimage.transform import (hough_line, hough_line_peaks)
from estatistics import moda, NULL_ANGLE
from Rotation import rotate
from skimage.feature import canny
import numpy as np


def hough_method(image):
    minima_amostragem = 5  #minima amostragem de picos
    factor = 1  #fator de ajuste do valor dos picos

    image = canny(image, 2, 1, 25)
    h, theta, d = hough_line(image)
    picos = [[0], [0], [0]]
    tot = 0
    while (len(picos[0]) < minima_amostragem and tot < 10):
        factor /= 2
        tot += 1
        picos = hough_line_peaks(h, theta, d, threshold=np.max(h) * factor)
    saved_angles = (np.rad2deg(picos[1]))
    saved_angles = np.round(saved_angles)
    moda_ang = moda(saved_angles)
    #print(saved_angles)
    if (moda_ang < 0):
        return -1 * (90 - abs(moda_ang))
    else:
        return 90 - moda_ang
