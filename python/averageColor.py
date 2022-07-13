"""
color = '#FF0000'
print(color)
integer = int(color.replace('#', ''), 16)
print(integer)
print(hex(integer))
"""
import time
file = 'sample 1000000.csv'


def average(file):
    nb = 0
    colors = 0
    with open(file, 'r') as f:
        f.readline()
        for line in f:
            nb += 1
            colors += int(line.split(',')[2].replace('#', ''), 16)
    print('Average color:', hex(colors // nb))


tStart = time.time()
average(file)
tEnd = time.time()

with open('averageColor.txt', 'a') as f:
    f.write(file + ' : python : ' + str(tEnd - tStart) + '\n')
