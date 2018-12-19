import random


def shuffle(file_name):
    content = []
    with open(file_name, 'r+') as f:
        for line in f:
            content.append(line)
    random.shuffle(content)
    fw = open('clean2.txt', 'w')
    for line in content:
        fw.write(line)
    fw.close()


if __name__ == '__main__':
    shuffle('clean1.txt')
