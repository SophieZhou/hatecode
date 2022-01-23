# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:22:47 2022

@author: Administrator
"""

"""
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。
如果不存在，则返回 -1。
"""      

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sSet = set(s)
        chaDic = {}
        for i in sSet:
            chaDic[i] = s.count(i)
        for i, j in enumerate(s):
            if chaDic.get(j) == 1:
                return i
        return -1
                    
if __name__=='__main__': 
    sl = Solution()
    s = 'abcdab'       
    print(sl.firstUniqChar(s))
    