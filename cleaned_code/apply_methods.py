import setup as s
import cv2
import numpy as np
import pandas as pd
import os
from Rotation import rotate
import Partition as part
from Fourier_transform import fourier_method
from Hough_transform import hough_method
from Horizontal_projection import horizontal_projection
from estatistics import moda, get_mediana
from segment_image import cut_extra_pixels

for root, dirs, files in os.walk(s.IMAGE_DIRECTORY_PATH):
    for file in files:
        if ".png" in file:
            img = cv2.imread(root + "/" + file, cv2.IMREAD_GRAYSCALE)
            print("calculando imagem {}".format(file))
            if (s.HJ):
                ang_hproj = horizontal_projection(img)
                res = rotate(img, ang_hproj)
                res = cut_extra_pixels(res)
                cv2.imwrite(s.IMAGE_RESULTS_FOLDER + "/" + file, res)
            elif (s.HT):
                ang_hough = hough_method(img)
                res = rotate(img, ang_hough)
                res = cut_extra_pixels(res)
                cv2.imwrite(s.IMAGE_RESULTS_FOLDER + "/" + file, res)
            elif (s.FT):
                ang_fourier = np.round(fourier_method(img))
                res = rotate(img, ang_fourier)
                res = cut_extra_pixels(res)
                cv2.imwrite(s.IMAGE_RESULTS_FOLDER + "/" + file, res)
            elif (s.ALL):
                partitions = part.partite(img, 3)
                ang_fourier = np.round(fourier_method(img))
                ang_hough = hough_method(img)
                ang_hproj = horizontal_projection(img)
                p_ang_fourier = part.apply_fourier_to_partite(partitions)
                p_ang_hough = part.apply_hough_to_partite(partitions)
                p_ang_hproj = part.apply_hj_to_partite(partitions)
                mediana = get_mediana([
                    ang_hproj,
                    int(ang_hough),
                    int(ang_fourier),
                    int(p_ang_hproj),
                    int(p_ang_hough),
                    int(p_ang_fourier)
                ])
                res = rotate(img, mediana)
                res = cut_extra_pixels(res)
                cv2.imwrite(s.IMAGE_RESULTS_FOLDER + "/" + file, res)

            # fails += 1
            # print("entrou no except, total de fails=", fails)
            # continue
