# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:36:08 2022

@author: zhoujy
"""

# In[]
'''
insert sorting, nondecreasing
'''
def fun_isort(alst):
    for i in range(len(alst)):
        key = alst[i]
        j = i-1
        while j>=0 and alst[j]>key:
            alst[j+1] = alst[j]
            j=j-1
        alst[j+1] = key
    
if __name__=='__main__':
    alst = [6,5,4,3,2,1]
    fun_isort(alst)
    print(alst)


# In[]
'''
insert sorting, nonincreasing
'''
def fun_isort(alst):
    for i in range(len(alst)):
        key = alst[i]
        j = i-1
        while j>=0 and alst[j]<key:
            alst[j+1] = alst[j]
            j=j-1
        alst[j+1] = key
    
if __name__=='__main__':
    alst = [6,5,4,3,2,1,7,6,8,9,10]
    fun_isort(alst)
    print(alst)


# In[]
'''
selection sort, nondecreasing
'''
def fun_ssort(alst):
    for i in range(len(alst)-1):
        m_n = i
        for j in range(i,len(alst)):
            if alst[j]<alst[m_n]:
                m_n = j
        tmp = alst[i] 
        alst[i]=alst[m_n]
        alst[m_n] = tmp
    
if __name__=='__main__':
    alst = [6,5,4,3,2,1,7,9,8,9,10]
    fun_ssort(alst)
    print(alst)

# In[]
'''
mergesort
'''
def merge(left,right):
    result=[]
    print('left',left,'right',right)
    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result = result + left
    result = result + right
    return result


def mergeSort(alst):
    print('mergesort')
    if len(alst)==1:
        return alst
    mid = int(len(alst)/2)
    left = alst[0:mid]
    right = alst[mid:]
    
    return merge(mergeSort(left),mergeSort(right))
    

if __name__=='__main__':
    alst = [6,5,4,3,2,1,7,9,8,9,10]
    result = mergeSort(alst)
    print(result)

# In[]
    
    
def marge(left, right):
    """排序合并两个数列"""
    result = []
    print(left)
    # 两个数列都有值
    while len(left) > 0 and len(right) > 0:
        # 左右两个数列第一个最小放前面
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只有一个数列中还有值，直接添加
    result += left
    result += right
    return result    
    
def merge_sort(arr):
    """归并排序"""
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 使用递归运算
    return marge(merge_sort(left), merge_sort(right))




merge_sort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22])

# 返回结果[11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]    