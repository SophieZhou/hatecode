# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:18:54 2022

@author: Administrator
"""

"""
给定一个字符串，验证它是否是回文串，
只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
"""        
class Solution(object):
    def isPalindrome(self,string):
        str_lst = []
        for item in string:
            if item.isalpha() or item.isdigit():
                str_lst.append(item)
 
        new_string = "".join(str_lst).lower()
        for i in range(len(new_string)//2):
            if new_string[i] != new_string[len(new_string)-1-i]:
                return False
        return True
        
string = "123Aman, a plan, a canal: Panama321"
sl = Solution()

print(sl.isPalindrome(string)) 




# In[]
"""

"""

class Solution:
    def isPalindrome(self, s):
        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]
    
if __name__=='__main__':
    s = "123Aman, a plan, a canal: Panama321"
    sl = Solution()
    print(sl.isPalindrome(s))
    