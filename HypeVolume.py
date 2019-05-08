import os

import numpy as np


def calhy(x, y):
    l = len(x)
    res = 0.0
    for i in range(l):
        if i == 0:
            res = res + x[1] * (1 - y[0])
        elif i == l - 1:
            res = res + (1 - x[i]) * (1 - y[i])
        else:
            res = res + (x[i + 1] - x[i]) * (1 - y[i]);
    return res


def get_hv(filename):
    m1 = np.loadtxt(filename)
    x1, y1 = get_can(m1)
    return calhy(x1, y1)


def get_can(m1):
    index = np.argsort(m1, axis=0)
    x1 = []
    y1 = []
    r = len(index)
    for i in range(r):
        a = index[i][0]
        x1.append(m1[a][0])
        y1.append(m1[a][1])
    return x1, y1


def get_directory(path):
    fp = []
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for f in files:
                cur = root + "/" + f
                fp.append(cur)
    else:
        fp.append(path)
    return fp


def get_directory_hv(path):
    fp = get_directory(path)

    for path in fp:
        print(path, get_hv(path))


if __name__ == '__main__':
    get_directory_hv('/home/kaiqiang/result')
