import numpy as np


def sum_matrix(img):
    tot = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            if (img[i][j] < 128):
                tot += 1
    return tot


def validate_partite(img, treshold):

    tot = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            if (img[i][j] < 128):
                tot += 1
    return (tot > treshold)