# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:32:32 2022

@author: Administrator
"""

"""
I do not like this problem.
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
 
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        for i, x in enumerate(nums):
            if x != i + 1:
                return i + 1
        
        return len(nums) + 1





