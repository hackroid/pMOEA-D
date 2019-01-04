import matplotlib.pyplot as plt


def get_pf(obj, file_name, population_size, iteration_num):
    result = {}
    for i in range(len(obj)):
        frate = obj[i][0]
        erate = obj[i][1]
        for j in range(len(obj)):
            if obj[j][0] > frate and obj[j][1] > erate:
                obj[j][0] = frate
                obj[j][1] = erate
    x = []
    y = []
    for i in range(len(obj)):
        frate = obj[i][0]
        erate = obj[i][1]
        result[frate] = erate
    for key in result:
        if key!=0:
            x.append(key)
            y.append(result[key])
    print(result)
    title = '{}-{}-{}'.format(file_name,population_size,iteration_num)
    plt.title(title)

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
