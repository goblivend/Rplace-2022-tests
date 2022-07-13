base_file = '2022_tiles_fix.csv'


def createSample(length):
    with open(base_file, 'r') as fr:
        with open('sample ' + str(length) + '.csv', 'w') as fw:
            for _ in range(length):
                fw.write(fr.readline())


def nblines():
    print(sum(1 for _ in open(base_file)))
    return


# createSample(10)
# createSample(50)
# createSample(100)
# createSample(500)
# createSample(1000)
# createSample(5000)
# createSample(10000)
# createSample(100000000)


nblines()
# 160 353 124
