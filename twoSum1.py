# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 17:47:28 2022

@author: Administrator
"""

"""
1. 两数之和

"""
class Solution():
    def twoSum(self,nums,target):
        print((target))
        for i in range(len(nums)):
            for j in range(i,len(nums)-1):
                if nums[j+1]==target-nums[i]:
                    print(i,j+1)
                    return i,j+1
                
    

sl = Solution()
nums = [1,2,3,4,5,6]
print(sl.twoSum(nums,6))      