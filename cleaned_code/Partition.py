import numpy as np
from part_validation import validate_partite, sum_matrix
from Horizontal_projection import horizontal_projection
from Fourier_transform import fourier_method
from Hough_transform import hough_method
from estatistics import moda, NULL_ANGLE


def partite(img, n):
    if (len(img) == 0):
        return -1

    xs = len(img) // n
    ys = len(img[0]) // n
    #print(xs,ys, len(img), len(img[0]))

    partite_images = []
    for i in range(n):
        for j in range(n):
            temp_image = img[i * xs:(i + 1) * xs, j * ys:(j + 1) * ys]
            partite_images.append(temp_image)

    filter_partite = []
    limiar = sum_matrix(img) // 10
    for part in partite_images:
        if (validate_partite(part, limiar)):
            filter_partite.append(part)
    return filter_partite


def apply_hough_to_partite(partite_images):
    hough_results = []
    for img in partite_images:
        try:
            #print("hough")
            hough_results.append(hough_method(img))
        except:
            print("hough except")
            continue


# print(hough_results)

    return moda(hough_results)


def apply_fourier_to_partite(partite_images):
    fourier_results = []

    for img in partite_images:
        #print("in")
        try:
            #print(img)
            angle = fourier_method(img)
            if (angle != NULL_ANGLE):
                fourier_results.append(np.round(angle))
        except:
            print("fourier except")
            continue
    #print(fourier_results)
    return moda(fourier_results)


def apply_hj_to_partite(partite_images):
    hj_results = []

    for img in partite_images:
        #print("happening")
        try:
            #print("hj")
            hj_results.append(horizontal_projection(img))
        except:
            print("hj except")
            continue
    #print(hj_results)
    return moda(hj_results)