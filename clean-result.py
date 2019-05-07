import numpy as np


def clean(file_name, target_name):
    # file_name = 'result/clean1-single-time-3600-166-3600.txt'
    obj = np.loadtxt(file_name)
    result = {}
    for i in range(len(obj)):
        frate = obj[i][0]
        erate = obj[i][1]
        for j in range(len(obj)):
            if obj[j][0] > frate and obj[j][1] > erate:
                obj[j][0] = frate
                obj[j][1] = erate
    x = []
    y = []
    for i in range(len(obj)):
        frate = obj[i][0]
        erate = obj[i][1]
        result[frate] = erate
    f = open(target_name, 'w')
    for key in result:
        if key != 0:
            f.write(str(key))
            f.write(' ')
            f.write(str(result[key]))
            f.write('\n')
    f.close()


if __name__ == '__main__':
    clean('result/clean1_single_t3600-167-3600.txt', 'result/clean1_single_t3600.txt')
