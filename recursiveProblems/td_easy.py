#https://www.techiedelight.com/find-combinations-of-elements-satisfies-given-constraints/


"""
Write a recursive program to efficiently reverse a given string
"""

def reverseString(s : str) -> str:
    if len(s) == 0:
        return s
    else:
        return  reverseString(s[1:]) + s[0] 

#print(reverseString("Let me test bro"))

"""
Write an efficient algorithm to implement the strstr function in Java, which returns the index of the first occurrence of a string in another string.
"""

def strstr(s1 : str, s2 : str) -> str:
    if s1[0:len(s2)] == s2:
        return True
    if len(s1) == 0:
        return False 
    else: 
        return strstr(s1[1:],s2)

"""
print(strstr("This is a test","test"))

print(strstr("This is a test","fail"))
"""


""" 
Maximum Product Subset Problem
Given an integer array, find the maximum product of its elements among all its subsets.

"""

def multiplicateList(numbers : list):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0]*multiplicateList(numbers[1:])

def findMaxProd(subset : list) -> str:
    negValues = [x for x in subset if x < 0]
    if len(negValues) % 2 != 0: 
        subset.remove(sorted(negValues,reverse=True)[0])
    if subset.count(0) > 0:
        subset.remove(0)
    return f"subset: {subset} with sum: {multiplicateList(subset)}"

print(findMaxProd([-6, 4, -5, 8, -10, 0, 8]))