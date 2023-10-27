from entrenos import *




def test_lee_entrenos():
    info_entrenos = lee_entrenos("./data/entrenos.csv")
    info_entrenos_3p = info_entrenos[:3]
    for e in info_entrenos_3p:
        print(e)
    info_entrenos_3u = [info_entrenos[-3],info_entrenos[-2],info_entrenos[-1]]
    for e in info_entrenos_3u:
        print(e)



test_lee_entrenos()
