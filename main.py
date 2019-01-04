from PMOEAD import PMOEAD
from PF import get_pf
from store_result import store_result
if __name__ == '__main__':
    file_name = 'clean1.txt'
    feature_num = 166
    population_size = 100
    iteration_num = 100
    begin = 0
    end = population_size
    population, obj = PMOEAD(file_name,feature_num, population_size, iteration_num, begin, end)
    # result = open('result.txt','w')
    # for i in range(len(obj)):
    #     result.write(str(obj[i][0]))
    #     result.write(' ')
    # result.write('\n')
    # for i in range(len(obj)):
    #     result.write(str(obj[i][1]))
    #     result.write(' ')
    # result.close()
    store_result(obj,file_name,population_size,iteration_num)
    get_pf(obj,file_name,population_size,iteration_num)
