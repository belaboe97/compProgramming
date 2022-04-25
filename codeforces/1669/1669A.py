
with open("inputs/1669A","r") as r:
    inp = list(map(lambda x: int(x.replace("\n","")),r.readlines()))[1:]
    for i in inp: 
        d = 1 if i > 1899 else 2 if i > 1600 else 3 if i > 1400 else 4
        print(f"Division {d}") 