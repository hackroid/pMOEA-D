
import copy

import numpy
from evaluate_solution import evaluate_single

'''
    Funtion used to get the accuracy of each feature
    return a [(index,accuracy),,,], accuracy from low to high
'''
def cal_accuracy(file_name,dimension):
    data = numpy.loadtxt(file_name)
    ret = []
    for i in range(dimension):
        sol = [0 for _ in range(dimension)]
        sol[i] = 1
        res = evaluate_single(sol,copy.copy(data))
        ret.append((i,res[1]))
    ret = sorted(ret,key= lambda x:x[1])
    return ret
