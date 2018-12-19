from generate_population import generate
from generate_weightvector import generate_weightvector
from get_neighbour import get_neighbour
from evaluate_solution import evaluate_solution, evaluate_single, evaluate_singlefitness, evaluate_fitness
import numpy

'''
    This method needs 
'''

OBJ_NUM = 2


def Initial(population_size, dimension, file_name):
    data = numpy.loadtxt(file_name)
    population = generate(population_size, dimension)
    weight_vector = generate_weightvector(population_size)
    neighbours = get_neighbour(population_size)
    obj, z = evaluate_solution(population, data)
    fitness = evaluate_fitness(population, obj, weight_vector)
    return population, weight_vector, neighbours, obj, z, fitness, data
