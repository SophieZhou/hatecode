# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:35:13 2022

@author: Administrator
"""

"""
二叉树的最大深度
"""
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)+1
        right = self.maxDepth(root.right)+1
        
        return max(left, right)                                        

