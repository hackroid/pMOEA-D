from PMOEAD import PMOEAD, PMOEAD_bytime
from store_result import store_result
from controller import parallel_run, parallel_run_bytime, naive_paralle
import time

INF = 1E9


def run_test(file_name):
    feature_num = 13
    if file_name == 'clean1.txt':
        feature_num = 167
    if file_name == 'Wine.txt':
        feature_num = 13
    population_size = max(100, min(200, feature_num))
    run_time = 600
    iteration_num = 10
    test_times = 15
    begin = 0
    end = population_size
    # parallel run without time
    for i in range(test_times):
        population, obj = parallel_run_bytime(max_time=run_time, iteration_num=iteration_num, cpu_num=8,
                                              file_name=file_name,
                                              dimension=feature_num, population_size=population_size)
        name = 'clean1_cpu8_{}'.format(i)
        store_result(obj, name)
    #     single run
    for i in range(test_times):
        population, obj = PMOEAD_bytime(file_name=file_name, dimension=feature_num, population_size=population_size,
                                        max_time=run_time, begin=begin, end=end)
        name = 'clean1_single_{}'.format(i)
        store_result(obj, name)
    for i in range(test_times):
        population, obj = parallel_run_bytime(max_time=run_time, iteration_num=iteration_num, cpu_num=8,
                                              file_name=file_name,
                                              dimension=feature_num, population_size=population_size,
                                              overlapping_ratio=0.2)
        name = 'clean1_cpu8_o.2_{}'.format(i)
        store_result(obj, name)


#     Wine 13 clean1 167

if __name__ == '__main__':
    file_name = 'clean1.txt'
    run_test(file_name)
    # feature_num = 167
    # population_size = max(100, min(200, feature_num))
    # iteration_num = 1000
    #
    # begin = 0
    # end = population_size

    # ------ This is the single core--------

    # population, obj = PMOEAD(file_name=file_name, dimension=feature_num, population_size=population_size,
    #                              max_iteration=iteration_num, begin=begin, end=end)
    # file_name = 'clean1-single'
    # ------------------------------------

    # -----------This is the multiple cores
    # round, iteration_num, cpu_num, file_name, dimension, population_size
    # population, obj = parallel_run(rounds=100, iteration_num=10, cpu_num=4, file_name=file_name, dimension=166, population_size=population_size)
    # file_name = 'clean1-PMOEAD-1000'
    # ------------------------------------

    # -------------Run by time parallel----------------------

    # max_time,iteration_num, cpu_num, file_name, dimension, population_size
    # run_time = 3600
    # population, obj = parallel_run_bytime(max_time=run_time, iteration_num=10, cpu_num=8, file_name=file_name,
    #                                       dimension=13, population_size=population_size)
    # a = 'clean1_pmoead_t3600_c8'
    # store_result(obj, a, population_size, run_time)

    # ------------------------------------------

    # ----------------Run by time single core---------------
    # file_name, dimension, population_size, max_time, begin, end

    # run_time = 3600
    # population, obj = PMOEAD_bytime(file_name=file_name, dimension=feature_num, population_size=population_size,
    #                                 max_time=run_time, begin=begin, end=end)
    # a = 'clean1_single_t3600'
    # store_result(obj, a, population_size, run_time)


    # --------------------------------------------------------
    # naive run by the same iteration
    # total_iteration = 1000
    # population, obj = naive_paralle(total_iteration=total_iteration, cpu_num=4, file_name=file_name, dimension=166, population_size=population_size)
    # file_name = 'clean1-naive-1000'
    # --------------------------------------------------------
    # naive run by same time

    # population, obj = naive_paralle(total_iteration=INF, cpu_num=4, file_name=file_name, dimension=13, population_size=population_size)
    # a = 'Wine-naive-time-3600'
    # store_result(obj, a, population_size, 3600)
    # --------------------------------------------------------
    # store_result(obj, file_name, population_size, iteration_num)
    # get_pf(obj, file_name, population_size, iteration_num)
    # print(time.time()-begin_time)
    # ---------------------------------------------------------------------------------
    # run_time = 3600
    # population, obj = parallel_run_bytime(max_time=run_time, iteration_num=10, cpu_num=8, file_name=file_name,
    #                                       dimension=13, population_size=population_size, overlapping_ratio=0.2)
    # a = 'clean1_overlapping_t3600_o0.2_c8'
    # store_result(obj, a, population_size, run_time)

