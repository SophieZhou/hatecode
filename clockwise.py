# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:09:00 2022

@author: Administrator
"""
"""
clockwise print the element of an array with two-dims
"""
class Solution(object):
    def clockwiseIter(self,arr):
        # 行、列指针
        row = 0
        col = 0        
        # 列的左右边界
        xLeft = 0
        xRight = len(arr[0]) - 1   
        # 行的上下边界
        yUp = 0
        yDown = len(arr) - 1
        # 已遍历输出的元素个数
        count = 0
        totalCount = len(arr[0]) * len(arr)

        #遍历方向：0 表示从左往右，1 表示从上往下，2 表示从右往左，3 表示从下往下
        direction = 0
        while (count < totalCount):
            if direction == 0:
#                print('dir',direction)
                for col  in range(xLeft,xRight+1):
                    count = count+1
                    print(arr[row][col])
                print()
                yUp += 1  # 上边界
                direction = 1 # 变换方向                
            elif direction == 1:
#                print('dir',direction)
                for row in range(yUp,yDown+1):
                    count=count+1
                    print(arr[row][col])
                
                print()
                xRight -= 1   # 右边界
                direction = 2  # 变换方向
            elif direction == 2:
#                print('dir',direction)
                for col in range(xRight,xLeft-1,-1):  
                    count=count+1
                    print(arr[row][col])
                
                print()
                yDown -= 1  #下边界
                direction = 3   # 变换方向
            elif direction == 3:
#                print('dir',direction)
                for row in range(yDown,yUp-1,-1):
                    count=count+1
                    print(arr[row][col])
                print()
                xLeft += 1   # 左边界
                direction = 0  #变换方向

    
    
if __name__=='__main__':
    arr = [[1, 2, 3, 4, 5],
                [12, 13, 14, 15, 6],
                [11, 10, 9, 8, 7]]
    sl = Solution()
    sl.clockwiseIter(arr)
    