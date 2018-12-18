from PMOEAD import PMOEAD
from PF import get_pf
if __name__ == '__main__':
    population, obj = PMOEAD('clean1.txt', 166, 100, 100, 0, 100)
    print(get_pf(obj))
