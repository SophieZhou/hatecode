# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:14:51 2022

@author: Administrator
"""
"""
This code is from web, not by myself.
"""


class Solution(object):
    def minimumTotal(self, triangle):
     
        if not triangle:
            return 

        res = triangle[-1]   
		
		# 遍历依然是从倒数第二行开始
        for i in range(len(triangle) - 2, -1, -1):   # 行遍历
            for j in range(len(triangle[i])):    # 列遍历
                res[j] = min(res[j],res[j+1]) + triangle[i][j]
        return res[0]

if __name__=='__main__':
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    sl = Solution()
    print(sl.minimumTotal(triangle))
    
    
    
# In[]
"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 
相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，
那么下一步可以移动到下一行的下标 i 或 i + 1 。

"""
class Solution:
    def minimumTotal(self, triangle):
        if not triangle:   
            return 
        # 
        for i in range(len(triangle) - 2, -1, -1):   # 行遍历
            for j in range(len(triangle[i])):    # 列遍历
                print(triangle[i][j] )
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])   # 状态转移方程
                print(triangle[i][j] )
        
        return triangle[0][0]    


if __name__=='__main__':
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    sl = Solution()
    print(sl.minimumTotal(triangle))
       