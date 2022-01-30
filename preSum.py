# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 12:48:12 2022

@author: Administrator
"""

# In[]
"""
前缀和
one-dimension
"""
class Solution():
    def preSum(self,nums):
        y=nums[:]
        for i in range(len(nums)):
            if i==0:
                y[i]=nums[i]
            else:
                y[i] = y[i-1]+nums[i]
        return y

sl = Solution()
nums = [1,2,3]
print(sl.preSum(nums))

# In[]
"""
前缀和
two-dimensions
"""
class Solution():
    def preSum(self,nums):
        y=[]
        for i in range(len(nums)):
            y.append([0 for j in range(len(nums[0]))])
        
        print(y)
        print(len(y),len(y[0]))
        print(len(nums),len(nums[0]))
        for i in range(len(nums)):# row
            for j in range(len(nums[0])): # col
                if i==0 and j==0:
                    y[i][j]=nums[i][j]
                elif i==0:
                    y[i][j]=y[i][j-1]+nums[i][j]
                elif j==0:
                    y[i][j]=y[i-1][j]+nums[i][j]
                else:
                    y[i][j]=y[i][j-1]+y[i-1][j]+y[i-1][j-1]+nums[i][j]
                
        return y

sl = Solution()
nums = [[1,2],[3,4],[5,6]]
print(sl.preSum(nums)) 