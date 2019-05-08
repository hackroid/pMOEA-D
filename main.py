from PMOEAD import PMOEAD, PMOEAD_bytime
from store_result import store_result
from controller import parallel_run, parallel_run_bytime, naive_paralle
import time
import sys
import argparse

INF = 1E9


def run_test(file_name):
    feature_num = 13
    if file_name == 'clean1.txt':
        feature_num = 167
    if file_name == 'Wine.txt':
        feature_num = 13
    population_size = max(100, min(200, feature_num))
    run_time = 60
    iteration_num = 10
    test_times = 1
    begin = 0
    end = population_size
    # parallel run without time
    for i in range(test_times):
        population, obj = parallel_run_bytime(max_time=run_time, iteration_num=iteration_num, cpu_num=8,
                                              file_name=file_name,
                                              dimension=feature_num, population_size=population_size)
        name = 'clean1_cpu8_{}'.format(i)
        store_result(obj, name)
        # single run
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
    for i in range(test_times):
        population, obj = parallel_run_bytime(max_time=run_time, iteration_num=iteration_num, cpu_num=8,
                                              file_name=file_name,
                                              dimension=feature_num, population_size=population_size,
                                              overlapping_ratio=0.2, auto_adjust=True)
        name = 'clean1_cpu8_aut_{}'.format(i)
        store_result(obj, name)


#     Wine 13 clean1 167

def load_dataset_prop():
    dataset = [
        {
            "name": "clean1",
            "file_name": "./src/dataset/clean1.txt",
            "features": 167,
            "population_size": 167
        },
        {
            "name": "wine",
            "file_name": "./src/dataset/Wine.txt",
            "features": 13,
            "population_size": 100
        }
    ]
    return dataset


def sys_args():
    dataset = load_dataset_prop()
    description = "OVERVIEW: pMOEA/D Interface\n\n" \
                  "USAGE: python3 reader.py -m [method] <inputs>\n" \
                  "    method: 1 for single core\n" \
                  "            2 for parallel\n" \
                  "            3 for parallel with overlapping\n" \
                  "            4 for parallel overlap auto adjust\n" \
                  "    inputs: Parameters\n" \
                  "    EXAMPLES:\n" \
                  "        python3 reader.py -h/--help\n" \
                  "        python3 -m 3 -o 0.1 -d wine\n" \
                  "        python3 -m 2 -t 600 -i 10 -c 8 -d clean1\n"
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-m",
                        "--method",
                        help="Choose a method for running",
                        nargs=1,
                        metavar="1/2/3/4",
                        choices=[1, 2, 3, 4],
                        type=int,
                        required=True
                        )
    parser.add_argument("-t",
                        "--time",
                        help="Time for one run (unit: second)",
                        nargs=1,
                        metavar="600",
                        default=600,
                        type=int
                        )
    parser.add_argument("-i",
                        "--iter",
                        help="Iterations for each generation",
                        nargs=1,
                        metavar="10",
                        default=10,
                        type=int
                        )
    parser.add_argument("-c",
                        "--cores",
                        help="Acquired cores for running(for method 2/3/4)",
                        nargs=1,
                        metavar="8",
                        default=8,
                        type=int
                        )
    parser.add_argument("-o",
                        "--overlap",
                        help="Overlapping ratio(for method 3/4)",
                        nargs=1,
                        metavar="0",
                        default=0,
                        type=float
                        )
    parser.add_argument("-d",
                        "--dataset",
                        help="Choose a dataset for running",
                        nargs=1,
                        metavar="Iris",
                        required=True
                        )
    args = parser.parse_args()
    method = args.method[0]
    packs = {}
    if method == 1:
        packs['method'] = method
        if isinstance(args.time[0], int) and args.time[0] > 0:
            packs['time'] = args.time[0]
        else:
            print("[ERROR]: Invalid time format")
            sys.exit()
        file_exist = False
        for item in dataset:
            if item['name'] == args.dataset[0]:
                file_exist = True
                packs['name'] = item['name']
                packs['file_name'] = item['file_name']
                packs['dimension'] = item['features']
                packs['population_size'] = item['population_size']
                packs['begin'] = 0
                packs['end'] = item['population_size']
                break
        if file_exist is False:
            print("[ERROR]: No such dataset exists: " + args.dataset[0])
            sys.exit()
    elif method == 2:
        packs['method'] = method
        if isinstance(args.time[0], int) and args.time[0] > 0:
            packs["time"] = args.time[0]
        else:
            print("[ERROR]: Invalid time format")
            sys.exit()
        if isinstance(args.iter, int) and args.iter > 0:
            packs["iter"] = args.iter
        else:
            print("[ERROR]: Invalid iteration format")
            sys.exit()
        if isinstance(args.cores, int) and args.cores > 0:
            packs["cores"] = args.cores
        else:
            print("[ERROR]: Invalid cores number format")
            sys.exit()
        file_exist = False
        for item in dataset:
            if item["name"] == args.dataset[0]:
                packs["name"] = item["name"]
                file_exist = True
                packs["file_name"] = item["file_name"]
                packs["dimension"] = item["features"]
                packs["population_size"] = item["population_size"]
                break
        if file_exist is False:
            print("[ERROR]: No such dataset exists: " + args.dataset[0])
            sys.exit()
    elif method == 3:
        packs["method"] = method
        if isinstance(args.time[0], int) and args.time[0] > 0:
            packs["time"] = args.time[0]
        else:
            print("[ERROR]: Invalid time format")
            sys.exit()
        if isinstance(args.iter, int) and args.iter > 0:
            packs["iter"] = args.iter
        else:
            print("[ERROR]: Invalid iteration format")
            sys.exit()
        if isinstance(args.cores, int) and args.cores > 0:
            packs["cores"] = args.cores
        else:
            print("[ERROR]: Invalid cores number format")
            sys.exit()
        if isinstance(args.overlap[0], float) and args.overlap[0] > 0:
            packs["overlap"] = args.overlap[0]
        else:
            print("[ERROR]: Invalid overlap ratio format")
            sys.exit()
        file_exist = False
        for item in dataset:
            if item["name"] == args.dataset[0]:
                packs["name"] = item["name"]
                file_exist = True
                packs["file_name"] = item["file_name"]
                packs["dimension"] = item["features"]
                packs["population_size"] = item["population_size"]
                break
        if file_exist is False:
            print("[ERROR]: No such dataset exists: " + args.dataset[0])
            sys.exit()
    elif method == 4:
        packs["method"] = method
        if isinstance(args.time[0], int) and args.time[0] > 0:
            packs["time"] = args.time[0]
        else:
            print("[ERROR]: Invalid time format")
            sys.exit()
        if isinstance(args.iter, int) and args.iter > 0:
            packs["iter"] = args.iter
        else:
            print("[ERROR]: Invalid iteration format")
            sys.exit()
        if isinstance(args.cores, int) and args.cores > 0:
            packs["cores"] = args.cores
        else:
            print("[ERROR]: Invalid cores number format")
            sys.exit()
        if isinstance(args.overlap[0], float) and args.overlap[0] > 0:
            packs["overlap"] = args.overlap[0]
        else:
            print("[ERROR]: Invalid overlap ratio format")
            sys.exit()
        file_exist = False
        for item in dataset:
            if item["name"] == args.dataset[0]:
                packs["name"] = item["name"]
                file_exist = True
                packs["file_name"] = item["file_name"]
                packs["dimension"] = item["features"]
                packs["population_size"] = item["population_size"]
                break
        if file_exist is False:
            print("[ERROR]: No such dataset exists: " + args.dataset[0])
            sys.exit()
    else:
        print("[ERROR]: No such method: " + str(args.method[0]))
        sys.exit()
    return packs


def run_task(packs: dict):
    if packs["method"] == 1:
        population, obj = PMOEAD_bytime(
            file_name=packs["file_name"],
            dimension=packs["dimension"],
            population_size=packs["population_size"],
            max_time=packs["time"],
            begin=packs["begin"],
            end=packs["end"]
        )
        name = '[dataset_{}][method_{}][time_{}]'.format(packs["name"],
                                                         packs["method"],
                                                         packs["time"])
    elif packs["method"] == 2:
        population, obj = parallel_run_bytime(
            max_time=packs["time"],
            iteration_num=packs["iter"],
            cpu_num=packs["cores"],
            file_name=packs["file_name"],
            dimension=packs["dimension"],
            population_size=packs["population_size"]
        )
        name = '[dataset_{}][method_{}][time_{}][cpu_{}]'.format(packs["name"],
                                                                 packs["method"],
                                                                 packs["time"],
                                                                 packs["cores"])
    elif packs["method"] == 3:
        population, obj = parallel_run_bytime(
            max_time=packs["time"],
            iteration_num=packs["iter"],
            cpu_num=packs["cores"],
            file_name=packs["file_name"],
            dimension=packs["dimension"],
            population_size=packs["population_size"],
            overlapping_ratio=packs["overlap"]
        )
        name = '[dataset_{}][method_{}][time_{}][cpu_{}][ovlp_{}]'.format(packs["name"],
                                                                          packs["method"],
                                                                          packs["time"],
                                                                          packs["cores"],
                                                                          packs["overlap"])
    else:
        population, obj = parallel_run_bytime(
            max_time=packs["time"],
            iteration_num=packs["iter"],
            cpu_num=packs["cores"],
            file_name=packs["file_name"],
            dimension=packs["dimension"],
            population_size=packs["population_size"],
            overlapping_ratio=packs["overlap"],
            auto_adjust=True
        )
        name = '[dataset_{}][method_{}][time_{}][cpu_{}][ovlp_{}][auto]'.format(packs["name"],
                                                                                packs["method"],
                                                                                packs["time"],
                                                                                packs["cores"],
                                                                                packs["overlap"])
    store_result(obj, name)


if __name__ == '__main__':
    pack = sys_args()
    run_task(pack)

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
