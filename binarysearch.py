# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 12:14:43 2022

@author: Administrator
"""

# In[]

def binary_search(nums, item):
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = int((low+high)/2)
        guess = nums[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    
    return None

if __name__=='__main__':
    nums = [1,2,3,4,5,6]
    print(binary_search(nums,3))
    print(binary_search(nums,8))

