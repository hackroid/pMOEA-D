from PMOEAD import pmoead, pmoead_by_time
from store_result import store_result
from controller import parallel_run, parallel_run_bytime, naive_parallel
import time
import sys

if __name__ == '__main__':

    argvv = sys.argv
    _parallel = True if (argvv[1] == 'y') else False
    _bytime = True if (argvv[2] == 'y') else False
    _naive = True if (argvv[2] == 'naive') else False
    _dataset = int(argvv[3])

    if _dataset == 1:
        feature_num = 13
        file_name = 'Wine.txt'
    elif _dataset == 2:
        feature_num = 166
        file_name = 'clean1.txt'
    else:
        feature_num = 24
        file_name = 'german.txt'

    run_time = 7200
    begin_time = time.time()
    directory = './src/datasets/' + file_name
    population_size = max(100, min(200, feature_num))
    iteration_num = 50
    round_num = 100
    cpu_num = 12

    if not _parallel:
        argv_p = 'NP'
        if _bytime:
            argv_t = 'TT'
            argv_i = '0000'
            population, obj = pmoead_by_time(
                file_name=directory,
                dimension=feature_num,
                population_size=population_size,
                max_time=run_time,
                begin=0,
                end=population_size)
        else:
            argv_t = 'NT'
            argv_i = '5000'
            population, obj = pmoead(
                file_name=directory,
                dimension=feature_num,
                population_size=population_size,
                max_iteration=iteration_num * round_num,
                begin=0,
                end=population_size
            )
    else:
        argv_p = 'PP'
        if _bytime:
            argv_t = 'TT'
            argv_i = '50'
            population, obj = parallel_run_bytime(
                max_time=run_time,
                iteration_num=iteration_num,
                cpu_num=cpu_num,
                file_name=directory,
                dimension=feature_num,
                population_size=population_size
            )
        elif _naive:
            argv_t = 'NA'
            argv_i = '5000'
            population, obj = naive_parallel(
                total_iteration=iteration_num * round_num,
                cpu_num=cpu_num,
                file_name=directory,
                dimension=feature_num,
                population_size=population_size
            )
        else:
            argv_t = 'NT'
            argv_i = 'r' + str(round_num) + 'i' + str(iteration_num)
            population, obj = parallel_run(
                rounds=round_num,
                iteration_num=iteration_num,
                cpu_num=cpu_num,
                file_name=directory,
                dimension=feature_num,
                population_size=population_size
            )
    duration = time.time() - begin_time
    store_result(
        obj=obj,
        file_name=file_name,
        poplation_size=population_size,
        argv_i=argv_i,
        argv_p=argv_p,
        argv_t=argv_t,
        result_t=duration
    )

    print(duration)
