import time


def read_file(file_name):
    with open(file_name, 'r') as f:
        s = f.readline()
        while s:
            s = f.readline()


def write_empty_file(file_name, n):
    with open(file_name, 'w') as f:
        for _ in range(n):
            f.write('\n')


def write_full_file(file_name, n, line):
    with open(file_name, 'w') as f:
        for _ in range(n):
            f.write(line + '\n')


nblines, line = 1000000, 1000*'8'

start = time.time()
write_full_file('test.txt', nblines, line)
print('Full file', time.time() - start)

line *= 3

start = time.time()
write_full_file('test.txt', nblines, line)
print('Long Full file', time.time() - start)

start = time.time()
write_empty_file('test.txt', nblines)
print('Empty file', time.time() - start)

start = time.time()
read_file('test.txt')
print('Read file', time.time() - start)
