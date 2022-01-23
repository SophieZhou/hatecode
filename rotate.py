# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:33:33 2022

@author: Administrator
"""

"""
给你一个数组，将数组中的元素向右轮转 k 个位置，
其中 k 是非负数。
"""
def rotate(nums, k):
    a = nums[:len(nums) - k]
    print(a)
    nums = nums[len(nums) - k:] + nums[:len(nums) - k]

    
def rotate2(nums, k): 
    nums = nums[len(nums) - k:].extend(nums[:len(nums) - k])
    
nums = [0,1,2,3,4]
rotate(nums,1)
print(nums)