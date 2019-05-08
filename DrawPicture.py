import matplotlib.pyplot as plt
import numpy as np
from HypeVolume import *


def draw_pic():
    m1 = np.loadtxt('result/clean1_cpu8_0.txt')
    m2 = np.loadtxt('result/clean1_cpu8_aut_0.txt')
    m3 = np.loadtxt('result/clean1_cpu8_o.2_0.txt')
    m4 = np.loadtxt('result/clean1_single_0.txt')
    # m5 = np.loadtxt('result/Wine_overlapping_p100_t120_o0.5_c8.txt')
    # m6 = np.loadtxt('result/Wine-single-p100-t120.txt')
    # m7 = np.loadtxt('result/Wine-pmoead-p100-t120-c4.txt')
    x1, y1 = get_can(m1)
    h1 = calhy(x1, y1)
    x2, y2 = get_can(m2)
    h2 = calhy(x2, y2)
    x3, y3 = get_can(m3)
    h3 = calhy(x3, y3)
    x4, y4 = get_can(m4)
    h4 = calhy(x4, y4)
    # x5, y5 = get_can(m5)
    # h5 = calhy(x5, y5)
    # x6, y6 = get_can(m6)
    # h6 = calhy(x6, y6)
    # x7, y7 = get_can(m7)
    # h7 = calhy(x7, y7)
    l1 = plt.plot(x1, y1, 'r--', label=f'cpu8 h={h1}')
    l2 = plt.plot(x2, y2, 'g--', label=f'auto h={h2}')
    l3 = plt.plot(x3, y3, 'b--', label=f'Overlapping Ratio = 0.2 h={h3}')
    l4 = plt.plot(x4, y4, 'r-*', label=f'singel h={h4}')
    # l5 = plt.plot(x5, y5, 'b-+', label=f'Overlapping Ratio = 0.5 h={h5}')
    # l6 = plt.plot(x6, y6, 'g:', label=f'MOEAD h={h6}')
    # l7 = plt.plot(x7, y7, 'r-.', label=f'PMOEAD h={h7}')

    plt.plot(x1, y1, 'r--', x2, y2, 'g--', x3, y3, 'b--', x4, y4, 'r-*')
    plt.title('Cleans')
    plt.xlabel('chosen features ratio')
    plt.ylabel('error rate')
    plt.legend()
    plt.savefig('result/Wine_Ratio.png')
    plt.show()


if __name__ == '__main__':
    draw_pic()
