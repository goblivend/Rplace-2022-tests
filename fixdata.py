basefile = './2022_tiles.csv'
fixedfile = './2022_tiles_fix.csv'


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
