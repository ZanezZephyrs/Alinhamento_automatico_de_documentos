import numpy as np
from Rotation import rotate
from skimage.transform import (hough_line, hough_line_peaks)
from estatistics import moda, NULL_ANGLE
from skimage.feature import canny


def fourier_method(img):
    #calcula a transformada de fourier
    fourier = np.fft.fft2(img)
    fourier_shifted = np.fft.fftshift(fourier)
    magnitude_spectrum = 20 * np.log(np.abs(fourier_shifted))
    magnitude_spectrum = (magnitude_spectrum - np.min(magnitude_spectrum)) * (
        255 / (np.max(magnitude_spectrum) - np.min(magnitude_spectrum)))
    magnitude_spectrum = np.uint8(magnitude_spectrum)

    #calcula o mapa de bordas do aspectro de frequencia
    border_map = canny(magnitude_spectrum, 2, 1, 25)
    h, theta, d = hough_line(border_map)
    #angulo_final=NULL_ANGLE
    #pega o angulo encontrado pela transformada de hough
    peaks = hough_line_peaks(h, theta, d, num_peaks=1, threshold=0.05)
    #print(peaks, len(peaks))
    for _, angle, dist in zip(*peaks):
        angulo_final = np.rad2deg(angle)
    #print(angulo_final)
    if (angulo_final == NULL_ANGLE):
        return NULL_ANGLE

    if angulo_final > 0:
        #print(angulo_final-90)
        angulo_ajustado = angulo_final - 90
    else:
        #print(angulo_final+90)
        angulo_ajustado = angulo_final + 90

    if (angulo_ajustado < 0):
        return -1 * (90 - abs(angulo_ajustado))
    else:
        return 90 - angulo_ajustado
