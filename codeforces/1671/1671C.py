
#Input 
#number of shops
#budget 

s = 5
#3 #shops
bu = 9
#7 #budget
p = sorted([10,20,30,40,50])
    #sorted([2,1,2])
    #diffrent testcases: 
    #sorted([10,20,30,40,50]) #prices per shop
    #sorted([2,1,2])
    #sorted([1,1])
c = 0  #sugarpackages 

##Information: took the wrong approach, thought that testcases equals days. 
"""
for i in range(d): 
    b = bu
    print(i,c)
    for j in range(s):
        if(b>=(p[j]+(i))):
            b=b-(p[j]+(i-2))    
            c+=1

print("you can buy", c)
"""
br=True 
ct = 0
co = 0
while(br):
    b = bu
    #breaking condition
    if (c!=0 and co == c) or (ct>0 and co == c):
        break
    #print(co,c)
    co = c
    #print(ct,c)
    #buying conditions.
    for j in range(len(p)): 
        if(b>=(p[j]+(ct))):
            b=b-(p[j]+(ct))    
            c+=1
    ct+=1

print("you can buy", c,"packs of sugar")