from PMOEAD import PMOEAD
# from PF import get_pf
from store_result import store_result
from controller import parallel_run
import time

if __name__ == '__main__':
    begin_time = time.time()
    file_name = 'clean1.txt'
    feature_num = 166
    population_size = max(100, min(200, feature_num))
    iteration_num = 100

    begin = 0
    end = population_size
    # population, obj = PMOEAD(file_name, feature_num, population_size, iteration_num, begin, end)
    population, obj = parallel_run(10, 10, 12, file_name, 166, population_size)
    store_result(obj, file_name, population_size, iteration_num)
    # get_pf(obj, file_name, population_size, iteration_num)
    print(time.time() - begin_time)
