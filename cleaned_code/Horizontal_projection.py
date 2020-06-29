from Rotation import rotate
from estatistics import NULL_ANGLE
import cv2
import numpy as np


def calcula_proj(img):
    temp = np.bitwise_not(img)
    project = np.sum(temp, 1)
    return project


def pico_projection(projection):
    return np.max(projection)


def horizontal_projection(src):
    angulo_encontrado = NULL_ANGLE
    vp = -15
    for angulo in range(-90, 91, 1):
        aux = rotate(src, angulo)
        projecao = calcula_proj(aux)
        valor_pico = pico_projection(projecao)
        #print(valor_pico)
        if (valor_pico > vp):
            angulo_encontrado = angulo
            vp = valor_pico
    return angulo_encontrado
