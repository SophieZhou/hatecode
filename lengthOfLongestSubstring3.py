# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:34:31 2022

@author: Administrator
"""

"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        # the start of the substr,if i>0, the new substr start
        i = 0
        # the length of the substr
        ans = 0
        # j is the end of the substr
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans
sl = Solution()
s= 'abcabcde'
print(sl.lengthOfLongestSubstring(s))  
