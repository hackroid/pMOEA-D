import random
from copy import copy, deepcopy
import time
import PMOEAD
import multiprocessing as mp

from Initial import initial
from Variation import CrossOver
from evaluate_solution import evaluate_single

INF = 1e9
Time_limit = 3600


class ParallelWorker(mp.Process):
    def __init__(self, in_queue, out_queue, random_seed):
        super(ParallelWorker, self).__init__(target=self.start)
        self.inQ = in_queue
        self.outQ = out_queue
        random.seed(random_seed)

    def run(self):
        while True:
            task = self.inQ.get()
            population, neighbours, z, obj, weight_vector, dimension, fitness, iteration_num, begin, end, data = task
            sol = parallel(population, neighbours, z, obj, weight_vector, dimension, fitness, iteration_num, begin, end,
                           data)
            self.outQ.put(sol)


def create_worker(num):
    workers = []
    for i in range(num):
        workers.append(ParallelWorker(mp.Queue(), mp.Queue(), random.randint(0, 10 ** 9)))
        workers[i].start()
    return workers


def finish_worker(workers):
    for w in workers:
        w.terminate()


def parallel(population, neighbours, z, obj, weight_vector, dimension, fitness, iteration_num, begin, end, data):
    iteration = 0
    neighbor_num = len(neighbours[0])
    start_time = time.time()
    while iteration < iteration_num and time.time() - start_time < Time_limit:
        print('iteration', iteration, 'time', time.time() - start_time)
        iteration += 1
        index = begin
        while index < end:
            p = random.sample(range(0, neighbor_num), 2)  # select two parents from its neighbour
            p1 = int(neighbours[index][p[0]])
            p2 = int(neighbours[index][p[1]])
            individual = CrossOver(population[p1], population[p2], dimension)
            i_obj = evaluate_single(individual, copy(data))

            if i_obj[0] < z[0]:
                z[0] = i_obj[0]
            if i_obj[1] < z[1]:
                z[1] = i_obj[1]

            PMOEAD.update_neighbour(population, neighbours[index], individual, i_obj, obj, fitness, weight_vecotr)

            index += 1
    return population, obj, fitness


def combine_population(result, cpu_num, population_size):
    new_population = [0 for _ in range(population_size)]
    new_obj = [None for _ in range(population_size)]
    new_fitness = [0 for _ in range(population_size)]
    for i in range(population_size):
        index = 0
        min_fitness = result[0][2][i]
        for j in range(cpu_num):
            if min_fitness > result[j][2][i]:
                index = j
                min_fitness = result[j][2][i]
        new_population[i] = result[index][0][i]
        new_obj[i] = result[index][1][i]
        new_fitness[i] = result[index][2][i]
    return new_population, new_obj, new_fitness


def parallel_run(rounds, iteration_num, cpu_num, file_name, dimension, population_size):
    population, weight_vector, neighbours, obj, z, fitness, data = initial(population_size, dimension, file_name)
    workers = create_worker(cpu_num)
    length = population_size // cpu_num
    result = [[None for _ in range(3)] for _ in range(cpu_num)]
    while rounds > 0:
        for i in range(cpu_num):
            begin = length * i
            end = length * (i + 1)
            if i == cpu_num:
                end = population_size
            workers[i].inQ.put(
                (deepcopy(population), neighbours, deepcopy(z), deepcopy(obj), weight_vector, dimension,
                 deepcopy(fitness), iteration_num, begin, end, data))
        for i in range(cpu_num):
            result[i][0], result[i][1], result[i][2] = workers[i].outQ.get()
        population, obj, fitness = combine_population(result, cpu_num, population_size)
        print(rounds)
        rounds -= 1
    finish_worker(workers)
    return population, obj


def naive_paralle(total_iteration, cpu_num, file_name, dimension, population_size):
    population, weight_vecotr, neighbours, obj, z, fitness, data = initial(population_size, dimension, file_name)
    workers = create_worker(cpu_num)
    length = population_size // cpu_num
    result = [[None for _ in range(3)] for _ in range(cpu_num)]
    for i in range(cpu_num):
        begin = length * i
        end = length * (i + 1)
        if i == cpu_num:
            end = population_size
        workers[i].inQ.put(
            (deepcopy(population), neighbours, deepcopy(z), deepcopy(obj), weight_vecotr, dimension,
             deepcopy(fitness), total_iteration, begin, end, data))
    # result[i][0] population , result[i][1] obj  The value of erate and frate
    # result[i][1] obj,[[frate,erate],[],,]
    for i in range(cpu_num):
        result[i][0], result[i][1], result[i][2] = workers[i].outQ.get()
    population, obj, fitness = combine_population(result, cpu_num, population_size)
    finish_worker(workers)
    return population, obj


def parallel_run_bytime(max_time, iteration_num, cpu_num, file_name, dimension, population_size, overlapping_ratio=0,
                        auto_adjust=False):
    TIME = time.time()
    round_turn = 1
    population, weight_vector, neighbours, obj, z, fitness, data = initial(population_size, dimension, file_name)

    workers = create_worker(cpu_num)
    length = population_size // cpu_num
    overlapping_part = int(overlapping_ratio * length)
    result = [[None for _ in range(3)] for _ in range(cpu_num)]

    while time.time() - TIME < max_time:

        for i in range(cpu_num):
            begin = length * i
            end = min(length * (i + 1) + overlapping_part, population_size)
            if i == cpu_num:
                end = population_size
            workers[i].inQ.put(
                (deepcopy(population), neighbours, deepcopy(z), deepcopy(obj), weight_vector, dimension,
                 deepcopy(fitness), iteration_num, begin, end, data))
        for i in range(cpu_num):
            result[i][0], result[i][1], result[i][2] = workers[i].outQ.get()
        population, obj, fitness = combine_population(result, cpu_num, population_size)
        print(round_turn)
        round_turn += 1
    finish_worker(workers)
    return population, obj
