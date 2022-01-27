# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:15:12 2022

@author: Administrator
"""
"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，
它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
"""       
    
class Solution:
  
    def multiply(self, num1, num2):
        num1=num1[::-1]
        num2=num2[::-1]
        result=[]
        for i in num2:
            flag=0
            raw=''
            k=0
            for j in num1:
                k+=1
                temp=int(i)*int(j)
                raw += str((temp%10+flag)%10)  
           #     print(raw)
                if temp+flag>9:
                    flag=int((temp+flag)/10)
                    
                else:
                    flag=0
                if k==len(num1):
                    
                    raw+=str(flag)
                
            result.append(raw)
            
        finall_result=0
        print(result)
        for i in range(len(result)):
                
            result[i]=result[i][::-1]  
            
            result[i]=int(result[i])*(10**i)
            finall_result+=result[i]
                
        return str(finall_result)
        
if __name__=='__main__':
    sl = Solution()
    print(sl.multiply('19','19'))
#    print(19*19)