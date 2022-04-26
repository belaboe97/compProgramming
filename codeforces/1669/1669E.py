from functools import reduce
with open("inputs/1669E","r") as r:
    inp = list(reduce(lambda x,y : x+y, list(map(lambda x: x.replace("\n","").split(),r.readlines()))[1:]))[1:]     
    s=0
    for i in range(len(inp)): 
        #print(i)
        if inp[i].isdigit() or i == len(inp)-1: print(s);s=0;continue
        for j in range(i+1,len(inp)): 
            #print(inp[i],inp[j])
            if inp[j].isdigit(): break; 
            elif (inp[i][0] == inp[j][0] and inp[i][1] != inp[j][1]) or (inp[i][0] != inp[j][0] and inp[i][1] == inp[j][1]): 
                s+=1#;print(inp[i],inp[j])
    """ 
    #create this struc: 
    #['cb', 'db', 'aa', 'cc', 'ef'], ['aa', 'bb', 'cc', 'ac', 'ca', 'bb', 'aa'], ['kk', 'kk', 'ab', 'ab']]
    #not needed
    p = list(); h=list()
    for ii, i in enumerate(inp):
        if i.isdigit() or ii == len(inp)-1: p.append(h);h = list()
        else: h.append(i) 
    """
    
    