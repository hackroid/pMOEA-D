import numpy


def kNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]  # shape[0]表示行数

    # # step 1: 计算距离[
    # 假如：
    # Newinput：[1,0,2]
    # Dataset:
    # [1,0,1]
    # [2,1,3]
    # [1,0,2]
    # 计算过程即为：
    # 1、求差
    # [1,0,1]       [1,0,2]
    # [2,1,3]   --   [1,0,2]
    # [1,0,2]       [1,0,2]
    # =
    # [0,0,-1]
    # [1,1,1]
    # [0,0,-1]
    # 2、对差值平方
    # [0,0,1]
    # [1,1,1]
    # [0,0,1]
    # 3、将平方后的差值累加
    # [1]
    # [3]
    # [1]
    # 4、将上一步骤的值求开方，即得距离
    # [1]
    # [1.73]
    # [1]
    #
    # ]
    # tile(A, reps): 构造一个矩阵，通过A重复reps次得到
    # the following copy numSamples rows for dataSet
    diff = numpy.tile(newInput, (numSamples, 1)) - dataSet  # 按元素求差值
    squaredDiff = diff ** 2  # 将差值平方
    squaredDist = numpy.sum(squaredDiff, axis=1)  # 按行累加
    distance = squaredDist ** 0.5  # 将差值平方和求开方，即得距离

    # # step 2: 对距离排序
    # argsort() 返回排序后的索引值
    sortedDistIndices = numpy.argsort(distance)
    classCount = {}  # define a dictionary (can be append element)
    for i in range(k):
        # # step 3: 选择k个最近邻
        voteLabel = labels[sortedDistIndices[i]]

        # # step 4: 计算k个最近邻中各类别出现的次数
        # when the key voteLabel is not in dictionary classCount, get()
        # will return 0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    # # step 5: 返回出现次数最多的类别标签
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex
