import os


def store_result(obj, file_name):
    path = './result' + os.path.sep
    title = path + '{}.txt'.format(file_name)
    result = open(title, 'w')
    for i in range(len(obj)):
        result.write(str(obj[i][0]))
        result.write(' ')
        result.write(str(obj[i][1]))
        result.write('\n')
    result.close()
