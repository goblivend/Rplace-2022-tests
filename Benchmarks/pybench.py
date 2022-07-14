########### Benchmark Function between split and slice ###########
import time
# """
file = './test.txt'
mymap = []


def time_benchmark(file):
    with open(file) as fr:
        lines = fr.readlines()
    start = time.time()
    first = [line[:27] for line in lines]
    first_time = time.time() - start
    start = time.time()
    second = [line.split(',')[0] for line in lines]
    second_time = time.time() - start
    print(int(round(first_time*1000000)), 'µs')
    print(int(round(second_time*1000000)), 'µs')
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
