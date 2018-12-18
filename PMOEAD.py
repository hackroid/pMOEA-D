from Initial import Initial
import random
from Variation import CrossOver
from evaluate_solution import evaluate_singlefitness, evaluate_solution, evaluate_single
import numpy
from copy import deepcopy
from math import floor


def PMOEAD(file_name, dimension, population_size, max_iteration, begin, end):
    population, weight_vecotr, neighbours, obj, z, fitness = Initial(population_size, dimension, file_name)
    iteration = 0
    negihbour_num = len(neighbours[0])
    while iteration < max_iteration:
        iteration += 1
        index = begin
        while index < end:
            p = random.sample(range(0, negihbour_num), 2)  # select two parents from its neighbour
            indiviual = CrossOver(population[p[0]], population[p[1]], dimension)
            i_obj = evaluate_single(indiviual, file_name)
            if i_obj[0] < z[0]:
                z[0] = obj[0]
            if i_obj[1] < z[1]:
                z[1] = obj[1]
            update_neighbour(population, neighbours[index], indiviual, obj, fitness)
            index +=1
        print(f'iteration {iteration}')
    return population, obj


def update_neighbour(population, neighbour, indiviual, obj, fitness):
    s = numpy.sum(indiviual)
    ratio = 1 / (len(population) - 1)
    for i in neighbour:
        index = int(i)
        temp = evaluate_singlefitness(obj[index][0], obj[index][1], s, floor(index * ratio))
        if fitness[index] > temp:
            population[index] = deepcopy(indiviual)
            fitness[index] = temp
