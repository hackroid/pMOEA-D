from PMOEAD import PMOEAD, PMOEAD_bytime
from store_result import store_result
from controller import parallel_run, parallel_run_bytime, naive_paralle

INF = 1E9


def run_test(file_name):
    feature_num = 13
    if file_name == 'clean1.txt':
        feature_num = 167
    if file_name == 'Wine.txt':
        feature_num = 13
    population_size = max(100, min(200, feature_num))
    run_time = 120
    iteration_num = 10
    test_times = 15
    begin = 0
    end = population_size
    cpu_num = 8
    overlapping_ratio = 0.2
    f = open('./result/chosenFile.txt', 'a')
    # parallel run
    # test_parallel_run_by_time(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num, population_size)
    # single run
    # test_PMOEAD_bytime(f, test_times, file_name, feature_num, population_size, run_time, begin, end)  # single
    # fix ratio
    #test_parallel_run_by_time_ratio(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num,
    #                                population_size, 0.1)
    #test_parallel_run_by_time_ratio(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num,
    #                                population_size, 0.3)
    #test_parallel_run_by_time_ratio(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num,
    #                                population_size, 0.4)
    #test_parallel_run_by_time_ratio(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num,
    #                               population_size, 0.5)

    # auto run
    test_parallel_run_by_time_auto(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num,
                                   population_size)

    f.close()


#     Wine 13 clean1 167
# Using hyper volume to choose th middle file
def chose_file(res):
    res = sorted(res, key=lambda x: x[1])
    l = int((len(res) + 1) / 2 - 1)
    return res[l][0]


def test_parallel_run_by_time(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num, population_size):
    res = []
    print('run parallel', file_name, 'starts')
    for i in range(test_times):
        population, obj = parallel_run_bytime(max_time=run_time, iteration_num=iteration_num, cpu_num=cpu_num,
                                              file_name=file_name,
                                              dimension=feature_num, population_size=population_size)
        name = '{}_cpu{}_{}'.format(file_name[:-4], cpu_num, i)
        hv = store_result(obj, name)
        res.append((i, hv))
    order = chose_file(res)
    name = '{}_cpu{}'.format(file_name[:-4], cpu_num)
    f.write('file:{}   chosen:the {} file\n'.format(name, order))
    print('run parallel', file_name, 'ends')


def test_PMOEAD_bytime(f, test_times, file_name, feature_num, population_size, run_time, begin, end):
    res = []
    print('run single', file_name, 'starts')
    for i in range(test_times):
        population, obj = PMOEAD_bytime(file_name=file_name, dimension=feature_num, population_size=population_size,
                                        max_time=run_time, begin=begin, end=end)
        name = '{}_single_{}'.format(file_name[:-4], i)
        hv = store_result(obj, name)
        res.append((i, hv))
    order = chose_file(res)
    name = '{}_single'.format(file_name[:-4])
    f.write('file:{}   chosen:the {} file\n'.format(name, order))
    print('run single', file_name, 'ends')


def test_parallel_run_by_time_ratio(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num,
                                    population_size, ratio):
    res = []
    print('run ratio', file_name, 'starts')
    for i in range(test_times):
        population, obj = parallel_run_bytime(max_time=run_time, iteration_num=iteration_num, cpu_num=cpu_num,
                                              file_name=file_name,
                                              dimension=feature_num, population_size=population_size,
                                              overlapping_ratio=ratio)
        name = '{}_cpu{}_o{}_{}'.format(file_name[:-4], cpu_num, ratio, i)
        hv = store_result(obj, name)
        res.append((i, hv))
    order = chose_file(res)
    name = '{}_cpu{}_o{}'.format(file_name[:-4], cpu_num, ratio)
    f.write('file:{}   chosen:the {} file\n'.format(name, order))
    print('run single', file_name, 'ends')


def test_parallel_run_by_time_auto(f, test_times, run_time, iteration_num, cpu_num, file_name, feature_num,
                                   population_size):
    res = []
    print('run auto', file_name, 'starts')
    for i in range(test_times):
        population, obj = parallel_run_bytime(max_time=run_time, iteration_num=iteration_num, cpu_num=cpu_num,
                                              file_name=file_name,
                                              dimension=feature_num, population_size=population_size,
                                              overlapping_ratio=0, auto_adjust=True)
        name = '{}_cpu{}_auto_{}'.format(file_name[:-4], cpu_num, i)
        hv = store_result(obj, name)
        res.append((i, hv))
    order = chose_file(res)
    name = '{}_cpu{}_auto'.format(file_name[:-4], cpu_num)
    f.write('file:{}   chosen:the {} file\n'.format(name, order))
    print('run auto', file_name, 'ends')


if __name__ == '__main__':
    file_name = 'clean1.txt'
    run_test(file_name)
