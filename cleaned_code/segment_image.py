import numpy as np


def calcula_proj_horizontal(img):
    temp = np.bitwise_not(img)
    project = np.sum(temp, 1)
    return project


def calcula_proj_vertical(img):
    temp = np.bitwise_not(img)
    project = np.sum(temp, 0)
    return project


def found_line_discard(proj):
    ini = 1
    fim = 1
    for i in range(1, len(proj)):
        if (proj[i] != 0):
            ini = i
            break
    for i in range(len(proj) - 1, 1, -1):
        if (proj[i] != 0):
            fim = i
            break
    return [ini, fim]


def found_column_discard(proj):
    ini = 1
    fim = 1
    for i in range(1, len(proj)):
        if (proj[i] != 0):
            ini = i
            break
    for i in range(len(proj) - 1, 1, -1):
        if (proj[i] != 0):
            fim = i
            break
    return [ini, fim]


def cut_extra_pixels(img):
    projecao = calcula_proj_horizontal(img)
    l_ini, l_end = found_line_discard(projecao)
    projecao = calcula_proj_vertical(img)
    c_ini, c_end = found_column_discard(projecao)
    print(l_ini, l_end, c_ini, c_end)
    final_img = img[l_ini:(l_end), (c_ini):(c_end)]
    return final_img