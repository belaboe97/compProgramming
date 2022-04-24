
#1) calculate seq d = [x for x in range(n1,n2)]

from cmath import inf

#Inputs
""" 
n1 = 1
n2 = 5
x = [10]
"""
n1 = 10
n2 = 2


#### Needs rework !!


#diff adjacent elements
d = [x for x in range(2,10+1)]
print(d)
s = d[len(d)-1]-d[0]
x = [6,1,5,7,3,3,9,10,10,1]

totDist = s
for i in x:
    tmp = inf
    for j in d: 
        tmp = min(abs(j-i),tmp)
    totDist+=tmp

print(totDist)