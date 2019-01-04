import random


def shuffle(fileName):
    content = []
    with open(fileName, 'r+') as f:
        for line in f:
            content.append(line)
    random.shuffle(content)
    fw = open('clean2.txt', 'w')
    for line in content:
        fw.write(line)
    fw.close()


if __name__ == '__main__':
    shuffle('clean1.txt')
