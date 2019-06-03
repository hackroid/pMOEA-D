'''
    KNN calculate accuracy
    Dynamic reference point(40) and fixed reference point(60)
    4 partitions
    10 iteration move once
    Assign the neighbour dynamically

'''
import random
import time
from copy import copy

import numpy

from Variation import CrossOver
from get_accuracy import cal_accuracy
from generate_population import generate
from evaluate_solution import evaluate_solution, evaluate_single, evaluate_fitness
from PMOEAD import update_neighbour

'''
    Get neighbour special for MOEADDYN
'''


def get_dyn_neighbour(neighbours, num, begin, end):
    for i in range(begin, end):
        neighbours[i][0] = i  # The neighbour contains itself
        count = 1
        dis = 1
        while count < num:
            if count < num and (i - dis) >= 0:
                neighbours[i][count] = i - dis
                count += 1
            if count < num and (i + dis) < end:
                neighbours[i][count] = i + dis
                count += 1
            dis += 1
    return neighbours


''''
Generate the reference point for static and dynamic
'''


def get_ref(population_size):
    fix = int(population_size * 0.6)
    dyn = population_size - fix
    fix_ref = [0 for _ in range(fix)]
    dyn_ref = [0 for _ in range(dyn)]
    fix_ratio = 1 / fix
    dyn_ratio = 1 / (4 * dyn)
    for i in range(1, fix + 1):
        fix_ref[i] = int(fix_ratio * i)
    for i in range(1, dyn + 1):
        dyn_ref[i] = int(dyn_ratio * i)
    return fix_ref, dyn_ref


'''
    Reallocate : right move
'''


def rigth_reallocate(ref, begin, deta):
    for i in range(begin, len(ref)):
        ref[i] = ref[i] + deta
    return ref


def left_reallocate(ref, begin, interval):
    num = len(ref) - begin
    ratio = interval / (4 * num)
    for i in range(begin, len(ref)):
        ref[i] = (i - begin + 1) * ratio
    return ref


'''
    Fix the solution, add or delete one feature
'''


def fix_solution(sol, acur, s):
    s1 = sum(sol)
    if s1 < s:
        # Add det features, from high accuracy to low
        det = s - s1
        for i in range(len(acur) - 1, -1, -1):
            index = acur[i][0]
            if sol[index] == 0:
                sol[index] = 1
                det -= 1
            if det == 0:
                break
    else:
        # delete the features, from low accuracy to high
        det = s1 - s
        for i in range(len(acur)):
            index = acur[i][0]
            if sol[index] == 1:
                sol[index] = 0
                det -= 1
            if det == 0:
                break
    return sol


def MOEADDYN(file_name, dimension, population_size, max_time):
    begin_time = time.time()
    # Number of fix and dyn reference points
    fix = int(population_size * 0.6)
    # Whether the reallocating should continue
    flag = True
    # Dynamic points in which interval
    interval = 0
    # Number of solutions in each interval
    dyn = population_size - fix
    acur = cal_accuracy(file_name, dimension)
    # Number of the neighbours
    ref_points = get_ref(population_size)
    num = population_size // 10
    neighbours = [[0 for _ in range(population_size // 10)] for _ in range(population_size)]
    # Generate the neighbours for fix and dyn
    neighbours = get_dyn_neighbour(neighbours, population_size // 10, 0, fix)
    neighbours = get_dyn_neighbour(neighbours, population_size // 10, fix, population_size)
    data = numpy.loadtxt(file_name)
    population = generate(population_size, dimension)
    obj, z = evaluate_solution(population, data)
    fitness = evaluate_fitness(population, obj, ref_points)
    iteration = 0
    while time.time() - begin_time < max_time:
        index = 0
        if iteration % 10 == 0 and iteration > 0 and flag:
            if interval == 0:
                ref_points = rigth_reallocate(ref_points, fix, 1 / 4)
                for i in range(fix, population_size):
                    population[i] = fix_solution(population[i], acur, int(ref_points[index] * dimension))
                obj, z = evaluate_solution(population, data)
                fitness = evaluate_fitness(population, obj, ref_points)
            else:
                pre_erate = 2
                cur_erate = 2
                # find the lowest error rate in previous interval and current interval
                frate1 = interval / 4
                frate2 = (interval + 1) / 4
                for i in range(population_size):
                    if ref_points[i] < frate1 and obj[i][1] < pre_erate:
                        pre_erate = obj[i][1]
                    if frate1 <= ref_points[i] < frate2 and obj[i][1] < cur_erate:
                        cur_erate = obj[i][1]
                if pre_erate > cur_erate:
                    interval += 1
                    ref_points = rigth_reallocate(ref_points, fix, 1 / 4)
                else:
                    ref_points = left_reallocate(ref_points, fix, interval)
                    flag = False
                obj, z = evaluate_solution(population, data)
                fitness = evaluate_fitness(population, obj, ref_points)
        else:
            while index < population_size:
                p = random.sample(range(0, num), 2)  # select two parents from its neighbour
                p1 = int(neighbours[index][p[0]])
                p2 = int(neighbours[index][p[1]])
                indiviual = CrossOver(population[p1], population[p2], dimension)
                indiviual = fix_solution(indiviual, acur, int(ref_points[index] * dimension))
                i_obj = evaluate_single(indiviual, copy(data))
                if i_obj[0] < z[0]:
                    z[0] = i_obj[0]
                if i_obj[1] < z[1]:
                    z[1] = i_obj[1]
                update_neighbour(population, neighbours[index], indiviual, i_obj, obj, fitness, ref_points)
                index += 1
        print("iteration:", iteration)
        iteration += 1
