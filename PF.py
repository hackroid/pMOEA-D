import matplotlib.pyplot as plt

def get_pf(obj):
    result = {}
    for i in range(len(obj)):
        frate = obj[i][0]
        erate = obj[i][1]
        if frate not in result:
            result[frate] = erate
        elif result[frate] > erate:
            result[frate] = erate
    print(result)
    x=[]
    y=[]
    for key in result:
        y.append(result[key])
        x.append(key)
    plt.title(u'PF for clean1')

    plt.xlabel('fratio')
    plt.ylabel('erate')
    # plt.scatter(x, y, s, c, marker)
    # x: x轴坐标
    # y：y轴坐标
    # s：点的大小/粗细 标量或array_like 默认是 rcParams['lines.markersize'] ** 2
    # c: 点的颜色
    # marker: 标记的样式 默认是 'o'
    plt.legend()

    plt.scatter(x, y, s=20, c="#ff1212", marker='o')
    plt.show()
