basefile = './2022_tiles.csv'
fixedfile = './2022_tiles_fix.csv'


def FixData(f1, f2):
    with open(f1) as fr:
        with open(f2, 'w') as fw:
            fw.write(fr.readline())
            line = fr.readline()
            # count = 10
            while line != '':  # and count > 0:
                ######## TimeStamp ms ########
                ims = 19  # index ms
                # print('Checking the "." :', line)
                if line[ims] != '.':
                    line = line[:ims] + '.' + line[ims:]
                    # print('Adding the .')

                ims += 1
                for i in range(3):
                    # print(
                    # f'Checking the {i}th ms which is : {line[ims+i]} :', line)
                    if line[ims + i] == ' ':
                        line = line[:ims + i] + '0' + line[ims+i:]
                        # print('Adding a 0')

                ######## Duplicate lines ########
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

                line = fr.readline()
                #count -= 1


# print('Fixing Data')

# FixData('./sample 100.csv', './sample 100fix.csv')
# FixData(basefile, fixedfile)


def areSimilar(name1, name2):
    with open(name1) as f1:
        with open(name2) as f2:
            l1, l2 = f1.readline(), f2.readline()
            while l1 != '' and l2 != '':
                if l1 != l2:
                    print(l1, l2)
                l1, l2 = f1.readline(), f2.readline()

            if l1 != l2:
                print(l1, l2)


# print('Checking Similarity')
# areSimilar(fixedfile, './2022_tilesfix3.csv')

def checkData(name):
    with open(name) as f:
        l = f.readline()
        l = f.readline()
        while l != '':
            spl = l.split(',')
            if len(spl) != 5:  # 4 ','
                print('Number of "," not good :')
                print(l)

            if len(spl[0]) != 27:
                print('TimeStamp Error')
                print(l)

            l = f.readline()


# print('Checking Data')
# checkData(fixedfile)
# checkData('./sample 100fix.csv')


def smaller(ts1, ts2):
    if ts1[9] != ts2[9]:  # Check day
        return int(ts1[9]) < int(ts2[9])

    if ts1[11:13] != ts2[11:13]:  # Check hour
        return int(ts1[11:13]) < int(ts2[11:13])

    if ts1[14:16] != ts2[14:16]:  # Check minute
        return int(ts1[14:16]) < int(ts2[14:16])

    if ts1[17:19] != ts2[17:19]:  # Check second
        return int(ts1[17:19]) < int(ts2[17:19])

    if ts1[20:23] != ts2[20:23]:  # Check ms
        return int(ts1[20:23]) < int(ts2[20:23])

    return True

# 2022-04-04 01:47:31.567 UTC
# 012345678901234567890123456


# print(smaller('2022-04-03 00:46:30.566 UTC', '2022-04-04 01:47:31.567 UTC'))
# 2022-04-04 00:55:40.375 UTC  >  2022-04-04 00:55:57.168 UTC
# print(smaller('2022-04-04 00:55:40.375 UTC', '2022-04-04 00:55:57.168 UTC'))


def copyFile(namer, namew):
    with open(namer) as fr:
        with open(namew, 'w') as fw:
            l = fr.readline()
            while l != '':
                fw.write(l)
                l = fr.readline()


def sort(namer, namew):
    ntemp1, ntemp2 = './temp1.txt', './temp2.txt'

    copyFile(namer, ntemp1)
    print('Temp file created')

    sorted = False
    while not sorted:
        sorted = True
        with open(ntemp2, 'w') as fw:
            with open(ntemp1) as fr:
                fw.write(fr.readline())
                s = fr.readline()
                maxi = fr.readline()

                while s != '':
                    if smaller(maxi, s):
                        sorted = False
                        print('not sorted, ', maxi.split(
                            ',')[0], ' < ', s.split(',')[0])
                        maxi, s = s, maxi

                    fw.write(s)
                    s = fr.readline()
                fw.write(maxi)
        print('One pass done')
        ntemp1, ntemp2 = ntemp2, ntemp1

    print('Copying to final file')
    copyFile(ntemp1, namew)


sort('./sample 10.csv', './sample 10sort.csv')
