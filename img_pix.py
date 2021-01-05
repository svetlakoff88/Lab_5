#!usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import cv2

image = 'CrLoken.jpg'
"""Percentage of black-white colors in the image"""


def img_prep(source):
    img = cv2.imread(source)
    colors, counts = np.unique(img.reshape(-1, 3), axis=0, return_counts=True)
    bin_percent = (max(counts)+min(counts))/(sum(counts)/100)
    return print('Изображение черно-белое на: ', round(bin_percent), '%')


img_prep(image)
