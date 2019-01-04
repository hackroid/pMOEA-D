import numpy


def generate(population_size, dimension):
    population = numpy.random.randint(0, 2, (population_size, dimension))
    return numpy.array(population)

# if __name__ == '__main__':
#     print(generate(10, 5))
