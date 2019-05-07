import matplotlib.pyplot as plt
import numpy as np
from HypeVolume import calhy


def draw_pic():
    m1 = np.loadtxt('result/Wine_overlapping_p100_t120_o0.1_c8.txt')
    m2 = np.loadtxt('result/Wine_overlapping_p100_t120_o0.2_c8.txt')
    m3 = np.loadtxt('result/Wine_overlapping_p100_t120_o0.3_c8.txt')
    m4 = np.loadtxt('result/Wine_overlapping_p100_t120_o0.4_c8.txt')
    m5 = np.loadtxt('result/Wine_overlapping_p100_t120_o0.5_c8.txt')
    m6 = np.loadtxt('result/Wine-single-p100-t120.txt')
    m7 = np.loadtxt('result/Wine-pmoead-p100-t120-c4.txt')

    x1, y1 = get_can(m1)
    h1 = calhy(x1, y1)
    x2, y2 = get_can(m2)
    h2 = calhy(x2, y2)
    x3, y3 = get_can(m3)
    h3 = calhy(x3, y3)
    x4, y4 = get_can(m4)
    h4 = calhy(x4, y4)
    x5, y5 = get_can(m5)
    h5 = calhy(x5, y5)
    x6, y6 = get_can(m6)
    h6 = calhy(x6, y6)
    x7, y7 = get_can(m7)
    h7 = calhy(x7, y7)
    l1 = plt.plot(x1, y1, 'r--', label=f'Overlapping Ratio = 0.1 h={h1}')
    l2 = plt.plot(x2, y2, 'g--', label=f'Overlapping Ratio = 0.2 h={h2}')
    l3 = plt.plot(x3, y3, 'b--', label=f'Overlapping Ratio = 0.3 h={h3}')
    l4 = plt.plot(x4, y4, 'r-*', label=f'Overlapping Ratio = 0.4 h={h4}')
    l5 = plt.plot(x5, y5, 'b-+', label=f'Overlapping Ratio = 0.5 h={h5}')
    l6 = plt.plot(x6, y6, 'g:', label=f'MOEAD h={h6}')
    l7 = plt.plot(x7, y7, 'r-.', label=f'PMOEAD h={h7}')

    plt.plot(x1, y1, 'r--', x2, y2, 'g--', x3, y3, 'b--', x4, y4, 'r-*', x5, y5, 'b-+', x6, y6, 'g:', x7, y7, 'r-.')
    plt.title('Wine 120s')
    plt.xlabel('chosen features ratio')
    plt.ylabel('error rate')
    plt.legend()
    plt.savefig('result/Wine_Ratio.png')
    plt.show()


def get_can(m1):
    index = np.argsort(m1, axis=0)
    x1 = []
    y1 = []
    r = len(index)
    for i in range(r):
        a = index[i][0]
        x1.append(m1[a][0])
        y1.append(m1[a][1])
    return x1, y1


if __name__ == '__main__':
    draw_pic()
