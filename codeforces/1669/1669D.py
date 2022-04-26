with open("inputs/1669D","r") as r:
    inp = list(map(lambda x: x.replace("\n","").split(),r.readlines()))[1:]     
    for i in inp[1::2]:
        print(i)