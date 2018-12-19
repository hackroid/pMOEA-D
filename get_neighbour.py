# 找到每个weight vector的邻居，邻居个数默认为population_size/10


def get_neighbour(population_size):
    num = population_size // 10
    neighbours = [[0 for _ in range(num)] for _ in range(population_size)]
    for i in range(population_size):
        neighbours[i][0] = i  # The neighbour contains itself
        count = 1
        dis = 1
        while count < num:
            if count < num and (i - dis) >= 0:
                neighbours[i][count] = i - dis
                count += 1
            if count < num and (i + dis) < population_size:
                neighbours[i][count] = i + dis
                count += 1
            dis += 1
    return neighbours

# if __name__=='__main__':
#     print(get_neighbour(100))
