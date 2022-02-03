# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:56:30 2022

@author: Administrator
"""

"""
recurrence
base case to return
the recursicve case to call itself



"""

def countdown(i):
    if i<1:
        return
    print(i)
    countdown(i-1)

countdown(10)        
        
# In[]
"""
call stack

"""

def factorial(n):
    
    if n==1:
        return 1    
    res = n*factorial(n-1)
    return res
    

print(factorial(6))





