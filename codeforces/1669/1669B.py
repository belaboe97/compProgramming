import collections

with open("inputs/1669B","r") as r:
    inp = list(map(lambda x: x.replace("\n","").split(),r.readlines()))[1:]
    for i in range(0,len(inp)-1,2): 
        e = sorted(list(collections.Counter(inp[i+1]).items()), key=lambda x: x[1],reverse=True)
        print(e[0][0]) if e[0][1] > 2 else print("-1")
