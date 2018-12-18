from Initial import Initial
import random
from Variation import CrossOver
from evaluate_solution import evaluate_singlefitness, evaluate_solution, evaluate_single
import numpy
from copy import deepcopy


def PMOEAD(file_name, dimension, population_size, max_iteration, begin, end):
    population, weight_vecotr, neighbours, obj, z, fitness = Initial(population_size, dimension, file_name)
    iteration = 0
    negihbour_num = len(neighbours[0])
    while iteration < max_iteration:
        iteration += 1
        index = begin
        while index < end:
            p = random.sample(range(0, negihbour_num), 2)  # select two parents from its neighbour
            p1 = int(neighbours[index][p[0]])
            p2 = int(neighbours[index][p[1]])
            indiviual = CrossOver(population[p1], population[p2], dimension)
            i_obj = evaluate_single(indiviual, file_name)
            if i_obj[0] < z[0]:
                z[0] = i_obj[0]
            if i_obj[1] < z[1]:
                z[1] = i_obj[1]
            update_neighbour(population, neighbours[index], indiviual, obj, fitness, weight_vecotr)
            index += 1
        print(f'iteration {iteration}')
    return population, obj


def update_neighbour(population, neighbour, indiviual, obj, fitness, weight_vector):
    s = numpy.sum(indiviual)
    population_num = len(population)
    for i in neighbour:
        index = int(i)
        temp = evaluate_singlefitness(obj[index][0], obj[index][1], s, int(weight_vector[index][0] * population_num))
        if fitness[index] > temp:
            population[index] = deepcopy(indiviual)
            fitness[index] = temp
