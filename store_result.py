def store_result(obj, file_name, poplation_size, argv_i, argv_p, argv_t):
    title = '{}-{}-{}-POP{}-{}'.format(argv_t, argv_p, argv_i, poplation_size, file_name)
    direct = './src/output/' + title
    result = open(direct, 'w')
    for i in range(len(obj)):
        result.write(str(obj[i][0]))
        result.write(' ')
        result.write(str(obj[i][1]))
        result.write('\n')
    result.close()
