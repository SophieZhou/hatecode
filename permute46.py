# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 13:02:42 2022

@author: Administrator
"""
"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。
你可以 按任意顺序 返回答案。
"""

class Solution:
    def permute(self, nums):
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
    
if __name__=='__main__':
    arr = [2,3,1]
    sl = Solution()
    print(sl.permute(arr))