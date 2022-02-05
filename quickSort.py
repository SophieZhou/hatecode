# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:29:13 2022

@author: Administrator
"""

# In[]
"""
4-1
sum function
"""
def sum_fun(arr):
    if arr==[]:
        return 0
    else:
        return arr[0]+sum_fun(arr[1:])
    
arr=[1]
print(sum_fun(arr))

# In[]
"""
4-2
length function
"""
def count(arr):
    if arr==[]:
        return 0
    else:
        return 1 + count(arr[1:])


arr=[1,2,3,4]
print(count(arr))
# In[]
"""
4-3 
max function
"""
def findmax(arr=[]):
    print(arr)
    if arr==[]:
        return None
    elif len(arr)==1:
        return arr[0]
    elif len(arr)==2:
        maxarr = arr[0] if arr[0]>arr[1] else arr[1]
        return maxarr
    else:
        return findmax([arr[0],findmax(arr[1:])]) # pay attention
    
arr=[1,2,3,4]
print(findmax(arr))

# In[]
"""
quicksort 

"""
def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [item for item in arr[1:] if item<=pivot ]
        greater = [item for item in arr[1:] if item>pivot ]
        return quickSort(less)+[pivot] +quickSort(greater)
        
arr=[10,5,3,4]
print(quickSort(arr))  

# In[]

"""
random select an item as the base value.
"""
import random
def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        num = random.randint(0,len(arr)-1)
        pivot = arr[num]
        less = [item for item in arr if item<=pivot ]
        greater = [item for item in arr if item>pivot ]
        return quickSort(less) + quickSort(greater)
        
arr=[10,50,30,40]
print(quickSort(arr))        
    