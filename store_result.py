import os


def store_result(obj, file_name):
    path = './src/result' + os.path.sep
    title = path + '{}.txt'.format(file_name)
    for i in range(len(obj)):
        frate = obj[i][0]
        erate = obj[i][1]
        for j in range(len(obj)):
            if obj[j][0] > frate and obj[j][1] > erate:
                obj[j][0] = frate
                obj[j][1] = erate
    x = []
    y = []
    result = {}
    for i in range(len(obj)):
        frate = obj[i][0]
        erate = obj[i][1]
        result[frate] = erate
    f = open(title, 'w')
    for key in result:
        if key != 0:
            f.write(str(key))
            f.write(' ')
            f.write(str(result[key]))
            f.write('\n')
    f.close()
