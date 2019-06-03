import numpy
from KNN import kNNClassify
import copy

K = 10
Ratio = 0.7
INF = 233
Alpha = 0.01  # two objects are the same important


def evaluate_single(solution, data):
    del_index = get_delindex(solution)
    feature_count = len(solution) - len(del_index)
    data = numpy.delete(data, del_index, axis=1)
    label = data[:, -1]
    data = numpy.delete(data, -1, axis=1)
    training_num = int(Ratio * len(data))
    training_data = data[:training_num]
    testing_data = data[training_num:]
    training_label = label[:training_num]
    testing_label = label[training_num:]
    error_count = 0
    total_count = 0
    for i in range(len(testing_data)):
        tag = kNNClassify(testing_data[i], training_data, training_label, K)
        # print(f'predict tag: {tag}  real label: {testing_label[i]}')
        if tag != testing_label[i]:
            error_count += 1
        total_count += 1
    frate = feature_count / len(solution)
    erate = error_count / total_count
    return [frate, erate]


def get_delindex(solution):
    del_index = []
    for i in range(len(solution)):
        if solution[i] == 0:
            del_index.append(i)
    return del_index


def evaluate_solution(solution, data):
    obj = [[0 for _ in range(2)] for _ in range(len(solution))]
    min_erate = INF
    min_frate = INF
    for i in range(len(solution)):
        result = evaluate_single(solution[i], copy.copy(data))
        obj[i][0] = result[0]
        obj[i][1] = result[1]
        if result[0] < min_frate:
            min_frate = result[0]
        if result[1] < min_erate:
            min_erate = result[1]
    return obj, [min_frate, min_erate]


def evaluate_singlefitness(frate, erate, s, nref):
    return erate + 100 * max(s - nref, 0) + Alpha * frate

'''
    Calculate the fitness value
    Fix bugs. nref should use dimension number to multiply
'''
def evaluate_fitness(solutions, obj, weight_vector):
    solution_num = len(solutions)
    fitness = [0 for _ in range(solution_num)]
    for i in range(solution_num):
        s = sum(solutions[i])
        nref = int(weight_vector[i][0] * len(solutions[i]))
        fitness[i] = evaluate_singlefitness(obj[i][0], obj[i][1], s, nref)
    return fitness

