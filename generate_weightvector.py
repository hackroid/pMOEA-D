import numpy
'''
    Generate population_num weight vectors.
    Split the interval into population_num -1 parts
    
'''
def generate_weightvector(population_num):
    weight_vector = numpy.zeros((population_num , 2))
    ratio = 1/(population_num-1)
    for i in range(population_num):
        weight_vector[i][1] = i*ratio
    return weight_vector

# if __name__=='__main__':
#     print(generate_weightvector(5))