
s=input()

#Input cant have a combination ab,ba 
#Otherwise all combinations can be made just by combining 2 and 3. eg. 4,5,6,7

print('NO' if 'b' in s.split("a") or 'a' in  s.split("b") else 'YES')
    
