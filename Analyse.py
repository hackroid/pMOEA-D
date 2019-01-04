import numpy
import PF


def analyse(file_name):
    data = numpy.loadtxt(file_name)
    obj = [[0 for _ in range(2)] for _ in range(100)]
    print(data)
    for i in range(100):
        obj[i][0] =data[0][i]
        obj[i][1] =data[1][i]
    print(obj)
    PF.get_pf(obj, 'clean1')


if __name__ == '__main__':
    analyse('result.txt')
