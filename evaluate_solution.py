import numpy
from KNN import kNNClassify

K = 10
Ratio = 0.7
INF = 233
Alpha = 1  # two objects are the same important


def evaluate_single(solution, file_name):
    data = numpy.loadtxt(file_name)
    del_index = get_delindex(solution)
    feature_count = len(solution) - len(del_index)
    data = numpy.delete(data, del_index, axis=1)
    numpy.random.shuffle(data)
    label = data[:, -1]
    data = numpy.delete(data, -1, axis=1)
    traning = int(Ratio * len(data))
    traning_data = data[:traning]
    testing_data = data[traning:]
    traning_label = label[:traning]
    testing_label = label[traning:]
    error_count = 0
    total_count = 0
    for i in range(len(testing_data)):
        tag = kNNClassify(testing_data[i], traning_data, traning_label, K)
        # print(f'predict tag: {tag}  real label: {testing_label[i]}')
        if tag != testing_label[i]:
            error_count += 1
        total_count += 1
    frate = feature_count / len(solution)
    erate = feature_count / total_count
    return [frate, erate]


def get_delindex(solution):
    del_index = []
    for i in range(len(solution)):
        if solution[i] == 0:
            del_index.append(i)
    return del_index


def evaluate_solution(solution, file_Name):
    obj = numpy.zeros((len(solution), 2))
    min_erate = INF
    min_frate = INF
    for i in range(len(solution)):
        result = evaluate_single(solution[i], file_Name)
        obj[i][0] = result[0]
        obj[i][1] = result[1]
        if result[0] < min_frate:
            min_frate = result[0]
        if result[1] < min_erate:
            min_erate = result[1]
    return obj, [min_frate, min_erate]


def evaluate_singlefitness(frate, erate, s, nref):
    return erate + 100 * max(s - nref, 0) + Alpha * frate


# if __name__ == '__main__':
#     solution = numpy.random.randint(0, 2, (10, 166))
#     for i in range(10):
#         print(solution[i])
#         print(evaluate(solution[i]))

def evaluate_fitness(solutions, obj):
    fitness = numpy.zeros(len(solutions))
    solution_num = len(solutions)
    ratio = 1 / (solution_num - 1)
    for i in range(solution_num):
        s = numpy.sum(solutions[i])
        nref = i  # reference point choose i features
        fitness[i] =evaluate_singlefitness(obj[i][0],obj[i][1],s,nref)
    return fitness