def calcDist(e : list):
        sum = 0
        for n in range(len(e)-1):
            sum += abs(e[n+1] - e[n]) 
        return sum
#1) calculate seq d = [x for x in range(n1,n2)]
with open("inputs/1671D",'r') as r:
    inp = r.readlines()[1:]
    inp = list(map(lambda x: x.replace("\n",""),inp))
  
    for idx in range(0,len(inp)-1,2):
        #generate sequence
        #d = [x for x in range(inp[idx])]
        a,b = inp[idx].split(" ")
        a,b = int(a),int(b)
        #e.g[1,2,3,4,5]
        l = [x for x in range(1,b+1)] 
        #e.g[10]
        #[7,2,10]
        e = list(map(lambda x: int(x) ,inp[idx+1].split(" ")))
        s = calcDist(e)
        mi,ma = min(e),max(e)
        print("S",s,e)
        #print(min((2* mi-1), e[0]-1, e[len(e)-1]))
        #print(min((2* mi-1), e[0]-1, e[len(e)-1]),min(2*(b-ma), b- max(e[0], e[len(e)-1])))
        if(l[0] < mi):
            s += min(2*(mi-1), min(e[len(e)-1],e[0])-1)
        if(l[len(l)-1] > ma):
            s += min(2*(b-ma), b- max(e[0], e[len(e)-1]))
        #print(min(2*(b-ma), b- max(e[0], e[len(e)-1])))

        print("Res:",s)
#High Time Compelxity?

"""
4
1 5
10
3 8
7 2 10
10 2
6 1 5 7 3 3 9 10 10 1
4 10
1 3 1 2
"""
#optimizing on the all combinatorics based on the best score by inserting at the time
"""
for idx in range(0,len(inp)-1,2):
    #generate sequence
    #d = [x for x in range(inp[idx])]
    a,b = inp[idx].split(" ")
    a,b = int(a),int(b)
    #e.g[1,2,3,4,5]
    l = [x for x in range(1,b+1)]
    #e.g[10]
    #[7,2,10]
    e = list(map(lambda x: int(x) ,inp[idx+1].split(" ")))
    #s = sorted(l+e))

    for li,le in enumerate(l):
        pos = 0
        dis = 10**6
        for ei,el in enumerate(e): 


            h = e.copy()
            if len(e) == 1: 
                pos = 0 if l[li] < e[ei] else 1
                #e.insert(pos,le)
                #d = 0 # because no decision needed whe
                continue
            else: 
                ct = 0 if ei != len(e) else 1
                h.insert(ei,le) if ei != len(e) else h.insert(ei+1,le)
                d = calcDist(h)
                if d < dis: 
                    pos = ei+ct
                    dis = d
        #print(li,le)
        e.insert(pos,le)
        print(e)
        
    #e.insert(pos,le)
    #print(e)
        #
    print(e, calcDist(e),e.index()) 
"""

#Some positive hits  -> wrong approach
"""
if len(e) > 1: 
    pos = 0 if l[li] < e[ei] else 1    
    if ei == 0: 
        d = abs(e[ei] - l[li])
    if ei < len(e)-1:
        d = abs(e[ei] - l[li]) + abs(e[ei+1] - l[li])
    if ei == len(e)-1: 
        #print(dis)
        d = abs(l[li] - e[ei])
        ci += 1
    if d < dis: 
        #print(ci)
        dis = d
        pos = ei + ci

else: 
    #print("pos",l[li])

"""
#Old Try
