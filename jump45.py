# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 22:43:25 2022

@author: Administrator
"""

"""
45. 跳跃游戏 II
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。
"""

class Solution:
    def jump(self, nums):
        if len(nums)<=1:
            return 0
        # All the elements are 1.
        if nums.count(1)==len(nums): return len(nums)-1
        
        length=len(nums)
        ind=length-1
        n=0
        i = ind - 1
        far_ind = i
        while ind>0:
            if i+nums[i]>=ind:
                far_ind=i
            i-=1
            if i==-1:
                ind=far_ind
                i = ind - 1
                far_ind = i
                n+=1
        return n
        
		# 下为leetcode官方代码（正向）：
        # n, step, end, maxPosition = len(nums), 0, 0, 0
        # for i in range(n-1):
        #     maxPosition = max(maxPosition, nums[i] + i)
        #     if i == end:
        #         end = maxPosition
        #         step += 1
        # return step
if __name__=='__main__':
    arr = [2,3,1,1,4,5,6,9]
    sl = Solution()
    print(sl.jump(arr))