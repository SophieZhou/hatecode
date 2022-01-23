# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:32:31 2022

@author: Administrator
"""

# In[]
"""
给定一个数组 nums，
编写一个函数将所有 0 移动到数组的末尾，
同时保持非零元素的相对顺序。
"""
def moveZeroes( nums):
    zero_count = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            zero_count += 1
            del nums[i]
    for i in range(zero_count):
        nums.append(0)

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)