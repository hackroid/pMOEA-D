from PMOEAD import PMOEAD

if __name__ == '__main__':
    population, obj = PMOEAD('data.txt', 3, 100, 100, 0, 100)
    print(population)
    print(obj)
