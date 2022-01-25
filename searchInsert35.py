# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:31:38 2022

@author: Administrator
"""

""" 
35  
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
"""
class Solution:
    def searchInsert(self, nums,target):
        return len([ num for num in nums if num < target ])
    
if __name__=='__main__':
    test =  [1,3,5,6]
    sl = Solution()
    
    print(sl.searchInsert(test,7))