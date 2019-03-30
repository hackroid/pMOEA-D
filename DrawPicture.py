import matplotlib.pyplot as plt
import numpy as np


def draw_pic():
    m1 = np.loadtxt('Wine-single-1000.txt')
    m2 = np.loadtxt('Wine-pararllel-1000.txt')
    m3 = np.loadtxt('Wine-navie-1000.txt')
    x1, y1 = get_can(m1)
    x2, y2 = get_can(m2)
    x3, y3 = get_can(m3)
    l1 = plt.plot(x1,y1,'r--',label='MOEA/D')
    l2 = plt.plot(x2,y2,'g--',label='PMOEA/D')
    l3 = plt.plot(x3,y3,'b--',label='naive parallel')
    plt.plot(x1,y1,'ro-',x2,y2,'g+-',x3,y3,'b^-')
    plt.title('Wine-1000-iteration')
    plt.xlabel('chosen features ratio')
    plt.ylabel('error rate')
    plt.legend()
    plt.show()


def get_can(m1):
    index = np.argsort(m1,axis=0)
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