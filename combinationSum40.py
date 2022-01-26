# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:28:58 2022

@author: Administrator
"""
"""
40. 组合总和 II
给定一个候选人编号的集合 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 
ref:
https://blog.csdn.net/weixin_45642918/article/details/108520138
"""

class Solution:
    def combinationSum2(self, candidates, target):
        # 将数组进行升序排序
        candidates.sort()
        ans = []
        tmp = []
        
        def dfs(idx, total):
            if total == target:
                ans.append(tmp[::])
                return
            if total > target:
                return

            for i in range(idx, len(candidates)):
                if candidates[i-1] == candidates[i] and i-1 >= idx:
                    continue
                
                total += candidates[i]
                tmp.append(candidates[i])
                dfs(i+1, total)
                # 回溯
                tmp.pop()
                total -= candidates[i]
            
        total = 0
        dfs(0, total)
        return ans
