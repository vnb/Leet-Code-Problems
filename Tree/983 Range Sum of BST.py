#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
link: https://leetcode.com/problems/range-sum-of-bst/
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def helper(root, L, R):
            sum_ = 0
            if root:
                if root.val >= L and root.val <= R:
                    sum_ = root.val
                    
            if root.left and root.right:
                    return sum_+helper(root.left, L, R)+helper(root.right, L, R)
            elif root.left:
                return sum_+helper(root.left, L, R)
            elif root.right:
                return sum_+helper(root.right, L, R)
            else:
                return sum_
            
        return helper(root, L, R)       