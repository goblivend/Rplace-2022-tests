import time
# import psutil
import os


def free_mem():
    tot_m, used_m, free_m = map(int, os.popen(
        'free -t -m').readlines()[-1].split()[1:])
    return free_m


print(free_mem() < 20000)
#  print(psutil.virtual_memory().total/1024**3)
# """

file = './2022_tiles_fix.csv'
"""
mymap = []


def sort(file, newf):
    print(free_mem())
    with open(file) as fr:
        with open(newf, 'w') as fw:
            fw.write(fr.readline())
        line = fr.readline()
        i = 1
        while line != '':
            mymap.append((line[:27], i))
            line = fr.readline()
            i += 1

    print('File read')
    mymap.sort(key=lambda obj: obj[0], reverse=True)
    print(free_mem())
    print('File sorted')
    with open(newf, 'a') as fw:
        length = len(mymap)
        print(length)
        i = 0
        while i < length:
            current = 0
            while True:
                _, line_nb = mymap[-1]
                with open(file) as fr:
                    for _ in range(line_nb-current):
                        fr.readline()
                        if free_mem() < 20000:
                            print('Memory is low')
                            time.sleep(1)
                            print('Memory is back')
                    fw.write(fr.readline())
                    # print(mymap)
                mymap.pop()
                # if i %100 == 0 :
                print(i)
                i += 1
                current = line_nb
                if i == length or current > mymap[-1][1]:
                    print(f'Breaking with {length-i} elements at {current}')
                    break

    print('New file written')
# """


def sortme(file, newf):
    with open(file) as fr:
        lines = fr.readlines()
    print(len(lines))
    lines.sort()
    with open(newf, 'w') as fw:
        fw.writelines(lines)


sortme(file, './filesorted.txt')
# """

"""
file = './test.txt'
mymap = []


def time_benchmark(file) :
    with open(file) as fr :
        lines = fr.readlines()
    start= time.time()
    first = [line[:27] for line in lines]
    first_time = time.time()- start
    start = time.time()
    second = [line.split(',')[0] for line in lines]
    second_time = time.time() - start
    print( int(round(first_time*1000000)),'µs')
    print( int(round(second_time*1000000)), 'µs')
    print(first == second)

    print(first.__sizeof__())


time_benchmark(file)
# """
# 2022-04-03 17:38:22.252 UTC,yTrYCd4LUpBn4rIyNXkkW2+Fac5cQHK2lsDpNghkq0oPu9o//8oPZPlLM4CXQeEIId7l011MbHcAaLyqfhSRoA==,#FF3881,"0000,0000"
# 012345678901234567890123456,0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567,0123456,01234567890
# 27 + 1 + 98 + 1 + 7 + 1 + 11 = 146

# https://psutil.readthedocs.io/en/latest/
# pip install psutil

# import psutil
# mem = psutil.virtual_memory()
# THRESHOLD = 4 * 1024 * 1024 * 1024  # 4GB
# if mem.available <= THRESHOLD:
#     print("warning")

# svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712, active=4748992512, inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304, slab=199348224)
