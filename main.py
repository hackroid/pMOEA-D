from PMOEAD import PMOEAD, PMOEAD_bytime
from store_result import store_result
from controller import parallel_run, parallel_run_bytime
import time

if __name__ == '__main__':

    _parallel = True if (input('Parallel?(y/n):') == 'y') else False
    _bytime = True if (input('By time?(y/n):') == 'y') else False
    _dataset = int(input('Choose your dataset: \n1. Wine\n2. clean1\n3. German\n(1/2/3): '))

    if _dataset == 1:
        feature_num = 13
        file_name = 'Wine.txt'
    elif _dataset == 2:
        feature_num = 166
        file_name = 'clean1.txt'
    else:
        feature_num = 24
        file_name = 'german.txt'

    run_time = 10
    begin_time = time.time()
    directory = './src/datasets/' + file_name
    population_size = max(100, min(200, feature_num))
    iteration_num = 20
    round_num = 10

    if not _parallel:
        argv_p = 'NP'
        if _bytime:
            argv_t = 'TT'
            argv_i = '0000'
            population, obj = PMOEAD_bytime(
                file_name=directory,
                dimension=feature_num,
                population_size=population_size,
                max_time=run_time,
                begin=0,
                end=population_size)
        else:
            argv_t = 'NT'
            argv_i = '200'
            population, obj = PMOEAD(
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
            argv_i = '20'
            population, obj = parallel_run_bytime(
                max_time=run_time,
                iteration_num=iteration_num,
                cpu_num=8,
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
                cpu_num=8,
                file_name=directory,
                dimension=feature_num,
                population_size=population_size
            )

    store_result(
        obj=obj,
        file_name=file_name,
        poplation_size=population_size,
        argv_i=argv_i,
        argv_p=argv_p,
        argv_t=argv_t
    )

    print(time.time() - begin_time)
