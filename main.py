from PF import get_pf
from PMOEAD import PMOEAD,PMOEAD_bytime
#from PF import get_pf
from store_result import store_result
from controller import parallel_run, parallel_run_bytime
import time

if __name__ == '__main__':
    begin_time = time.time()
    file_name = 'clean1.txt'
    feature_num = 166
    population_size = max(100, min(200, feature_num))
    iteration_num = 100

    begin = 0
    end = population_size
    #------ This is the single core--------
    # population, obj = PMOEAD(file_name=file_name, dimension=feature_num, population_size=population_size,
                             # max_iteration=iteration_num, begin=begin, end=end)
    # ------------------------------------

    # -----------This is the multiple cores
    # round, iteration_num, cpu_num, file_name, dimension, population_size
    # population, obj = parallel_run(round=10, iteration_num=10, cpu_num=8, file_name=file_name, dimension=166, population_size=population_size)
    # ------------------------------------

    # -------------Run by time parallel----------------------
    # max_time,iteration_num, cpu_num, file_name, dimension, population_size
    # run_time =200
    # population, obj = parallel_run_bytime(max_time=run_time, iteration_num=10, cpu_num=8, file_name=file_name, dimension=166, population_size=population_size)
    # file_name = file_name +'-parallel run by time'
    # store_result(obj, file_name, population_size, run_time)
    # ------------------------------------------

    # ----------------Run by time single core---------------
    # file_name, dimension, population_size, max_time, begin, end
    run_time =200
    population, obj = PMOEAD_bytime(file_name=file_name, dimension=feature_num, population_size=population_size, max_time=run_time, begin=begin, end=end)
    file_name = file_name +'-single core run by time'
    store_result(obj, file_name, population_size, run_time)

    # --------------------------------------------------------

    # store_result(obj, file_name, population_size, iteration_num)
    get_pf(obj, file_name, population_size, iteration_num)
    print(time.time()-begin_time)
