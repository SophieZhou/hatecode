# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:17:49 2022

@author: Administrator
"""
"""
selection sort
O(n^2)
"""

def findSmallest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind
    
def selectionSort(arr):
    newarr = []
    while len(arr)>0:
        newsamll = findSmallest(arr)
        newarr.append(arr.pop(newsamll))
    return newarr
    
print(selectionSort([5,3,6,2,10]))