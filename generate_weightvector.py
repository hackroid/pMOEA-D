import numpy

'''
    Generate population_num weight vectors.
    Split the interval into population_num -1 parts
    
'''


def generate_weightvector(population_num):
    weight_vector = [[0 for _ in range(2)] for _ in range(population_num)]
    ratio = 1 / population_num
    for i in range(population_num):
        weight_vector[i][0] = (i + 1) * ratio  # The reference point is on the fratio
    return weight_vector

# if __name__=='__main__':
#     print(generate_weightvector(5))
