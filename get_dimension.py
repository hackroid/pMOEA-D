if __name__ == '__main__':
    f = open('clean1.txt')
    for line in f:
        a = line.split()
        print(len(a))
        break
    f.close()