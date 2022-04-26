##Better solution: 
#Idea -> all i and i+1 has to be of the same type odd or even to be true
#reduce with lambda 2 to zero and 1 
with open("inputs/1669C","r") as r:
    inp = list(map(lambda x: x.replace("\n","").split(),r.readlines()))[1:] 
    #inp = for 
    #s[word for sentence in text for word in sentence]
    for i in inp[1::2]: 
        l = list(map(lambda x: int(x)%2,i)) 
        if(len(set([x for x in l[::2]]))+len(set([x for x in l[1::2]])))<=2:print('YES')
        else:print('NO')


#My solution: 
#If each list gots computed
"""
def checkNumbers(a :list) -> bool: 
    n = int(a[0])%2
    #print(a)
    for al in a[1:]:
        al=int(al)
        #print(al%2,n)
        if al%2!=n: 
            return False
    return True  

with open("inputs/1669C","r") as r:
    inp = list(map(lambda x: x.replace("\n","").split(),r.readlines()))[1:] 
    #inp = for 
    #s[word for sentence in text for word in sentence]
    for i in inp[1::2]: 
        print(i)
        b= 'YES' if checkNumbers(i) else 'NO'
        if b == 'YES':
            print(b)
            continue
        b= 'YES' if checkNumbers([int(le)+1 if li%2==0 else le for li,le in enumerate(i)]) else 'NO'
        if b == 'YES':
            print(b)
            continue
        b= 'YES' if checkNumbers([int(le)+1 if li%2!=0 else le for li,le in enumerate(i)]) else 'NO'
        print(b)
"""
