
#Conditions 
"""
Numbers are points on their X-achsis.
Conditions:
numbers cant range more then 3 units 
numbers cant range more than 2 units in opposite directions
"""
inp = [2,5,6]
count = 0
possible = "YES"
for i in range(len(inp)-1):
    if count > 1:
        possible = "NO"
        break 
    if inp[i+1] - inp[i] > 3: 
        possible = "NO"
        break
    if inp[i+1] - inp[i] > 2:
        count += 1

print(possible)

"""
Alternative style for solution: 
So the total space all numbers in the list are occuping around x cant be higher as the endterm - startterm + 1.
Otherwise they are to widespread around X. 
"""

print('YES' if  inp[0]+1 <= inp[len(inp)-1] else 'NO')