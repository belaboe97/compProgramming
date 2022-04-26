#Idea: 
#Before or after every R must be a B or multipe B's | if W check cond 3
#Before or after every B must be a R or multipe R's | if w check cond 3
#Before or after W must be W or (BR,RB)

##Conclusion every sequence of mutliple  B or R can be adjusted to 1x(BR)
#Sequence of 3 
#Multiple Combinations can occur as BRBRBRBR or RBRBRBRB, just look for R 
#

with open("inputs/1669D","r") as r:
    inp = list(map(lambda x: x.replace("\n","").split(),r.readlines()))[1:]     
    for [i] in inp[1::2]: 
        a=list(map(set,i.split('W'))); o="YES"
        for b in a: 
            if len(b)==1:o='NO';break
        print(o)  



#My soultion, possible faster
"""
with open("inputs/1669D","r") as r:
    inp = list(map(lambda x: x.replace("\n","").split(),r.readlines()))[1:]     
    for [i] in inp[1::2]:
        ns = i[0]
        for l in range(1,len(i)):
            if i[l] != i[l-1]: ns+=(i[l])
        x= [x for x in ns.split("W") if not x==""]                
        #print(i,ns,x)
        print('YES') if ('R' not in x and 'B' not in x) else print('NO')
        #print(i[0],i[0].split("R"),i[0].split("B"))
        
        print("NOTHING?",i,{*i})

"""


