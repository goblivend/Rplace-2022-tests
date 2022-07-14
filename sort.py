# timestamp,user_id,pixel_color,coordinate
#   27     ,   88  ,     7     , 5->11

# 2022-04-04 00:53:51.577 UTC,ovTZk4GyTS1mDQnTbV+vDOCu1f+u6w+CkIZ6445vD4XN8alFy/6GtNkYp5MSic6Tjo/fBCCGe6oZKMAN3rEZHw==,#00CCC0,"826,1048"
# 012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234
# 0         1         2         3         4         5         6         7         8         9         0         1         2         3
# 012345678901234567890123456 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567 0123456 0123456789
# 0         1         2      /0         1         2         3         4         5         6         7         8       /0      /0

import time
import os

width = os.get_terminal_size().columns * 90 // 100
nblines = 160_353_124
linesPerHash = nblines // width

"""
def free_mem():
    tot_m, used_m, free_m = map(int, os.popen(
        'free -t -m').readlines()[-1].split()[1:])
    return free_m

# """

########### Fixing data Function ###########


def FixData(file, newfile):
    with open(file) as fr:
        with open(newfile, 'w') as fw:
            fw.write(fr.readline())
            line = fr.readline()
            i = 1
            while line != '':
                ######## fixing the TimeStamp milliseconds ########
                ims = 19  # index milliseconds
                if line[ims] != '.':
                    line = line[:ims] + '.' + line[ims:]

                ims += 1
                for i in range(3):
                    if line[ims + i] == ' ':
                        line = line[:ims + i] + '0' + line[ims+i:]

                ########          Duplicate lines          ########
                if line.count(',') == 4:
                    fw.write(line)
                else:
                    splitLine = line.split(',', 3)
                    starter = ','.join(splitLine[:-1]) + ',"'

                    coos = splitLine[-1].replace('"',
                                                 '').replace('\n', '').split(',')
                    l1 = starter + ','.join(coos[:2]) + '"\n'
                    l2 = starter + ','.join(coos[2:]) + '"\n'
                    fw.write(l1)
                    fw.write(l2)
                i += 1
                if i % linesPerHash == 0:
                    print('#', end='')
                line = fr.readline()
    print()

# FixData(basefile, fixedfile)

########### Is Sorted Function ###########


"""
def isSorted(file):
    with open(file) as fr:
        head = fr.readline()
        line = fr.readline()
        i = 2
        while line != '':
            pline = line[:27]
            if pline > line[:27]:
                return False
            line = fr.readline()
            i += 1
            if i % linesPerHash == 0:
                print('#', end='')
        print()
    return True
# """

########### Splitting the File by days ###########

# """


def splitDays(file, names):
    files = {
        '1': open(names[0], 'w'),
        '2': open(names[1], 'w'),
        '3': open(names[2], 'w'),
        '4': open(names[3], 'w'),
    }

    with open(file) as fr:
        head = fr.readline()
        for file in files.values():
            file.write(head)
        i = 0
        for line in fr:
            if head != line:
                files[line[9]].write(line)
            i += 1
            if i % linesPerHash == 0:
                print('#', end='')
        print()

    for file in files.values():
        file.close()
# """

########### Sorting Function by loading the complete file ###########

# """


def sortme(files, newf):
    with open(newf, 'w') as fw:
        fw.write(open(files[0]).readline())
        for file in files:
            with open(file) as fr:
                fr.readline()
                lines = fr.readlines()
            print('Loaded ' + file)
            lines.sort()
            print('Sorted ' + file)
            fw.writelines(lines)
            print('Written ' + file)
# """

########### function calls to create the sorted files ###########


with open('./.log', 'w') as log:
    print('Fixing data...')
    start = time.time()

    FixData('./2022_tiles.csv', './2022_tiles_fix.csv')

    log.write('Fixing data: ' + str(time.time() - start) + '\n')
    print('Splitting the file to sort it')
    temp = time.time()

    splitDays('./2022_tiles_fix.csv', [
        './temp1.csv',
        './temp2.csv',
        './temp3.csv',
        './temp4.csv'])

    log.write('Splitting the file to sort it: ' +
              str(time.time() - temp) + '\n')
    print('Splitting the file to sort it in :', time.time() - start)

    temp = time.time()

    os.remove('./2022_tiles_fix.csv')
    log.write('Removing fixed file: ' + str(time.time() - temp) + '\n')
    print('Removing fixed file:', time.time() - start)

    print('Sorting the file')
    temp = time.time()
    sortme([
        './temp1.csv',
        './temp2.csv',
        './temp3.csv',
        './temp4.csv'], './2022_tiles_sorted.csv')

    log.write('Sorting the file: ' + str(time.time() - temp) + '\n')
    print('Sorted the file in :', time.time() - temp)

    print('Removing the temporary files')
    temp = time.time()
    os.remove('./temp1.csv')
    os.remove('./temp2.csv')
    os.remove('./temp3.csv')
    os.remove('./temp4.csv')

    log.write('Removing the temporary files: ' +
              str(time.time() - temp) + '\n')
    print('Removed the temporary files in :', time.time() - temp)

    print('Splitting the file for each day')
    temp = time.time()

    splitDays('./filesorted.txt', ['Day 1.csv',
                                   'Day 2.csv', 'Day 3.csv', 'Day 4.csv'])

    log.write('Splitting the file for each day: ' +
              str(time.time() - temp) + '\n')
    print('Splitted the file for each day in :', time.time() - temp)

    log.write('Total time: ' + str(time.time() - start) + '\n')
    print('Finished in :', time.time() - start)
