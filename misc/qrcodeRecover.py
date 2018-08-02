#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt


def main(src, dst):
    image = plt.imread(src)
    x, y, _ = image.shape
    image.flags.writeable = True

    grays = []
    thresold = 111

    for i in range(x):
        for j in range(y):
            R, G, B = image[i][j]
            Gray = (R * 299 + G * 587 + B * 114 + 500) / 1000.0
            grays.append(Gray)
            image[i][j] = [(Gray > thresold) * 255] * 3

    # fill gap
    for bias in range(3, 1, -1):
        for i in range(bias, x - bias):
            for j in range(bias, y - bias):
                if image[i - bias][j][0] == image[i + bias][j][0]:
                    image[i][j] = image[i - bias][j]

    grays = np.array(grays)
    print("thresold: %s" % grays.mean())
    plt.imsave(fname=dst, arr=image)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
