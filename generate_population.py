import numpy


def generate(population_size, demension):
    population = numpy.random.randint(0, 2, (population_size, demension))
    return population

# if __name__ == '__main__':
#     print(generate(10, 5))
