from PMOEAD import PMOEAD
from PF import get_pf
if __name__ == '__main__':
    population, obj = PMOEAD('clean1.txt', 4, 1000, 100, 0, 100)
    result = open('result.txt','w')
    for i in range(len(obj)):
        result.write(str(obj[i][0]))
        result.write(' ')
    result.write('\n')
    for i in range(len(obj)):
        result.write(str(obj[i][1]))
        result.write(' ')
    result.close()
    # print(get_pf(obj))
