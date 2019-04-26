#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def maxDepth(root):
            return 0 if not root else 1+max(maxDepth(root.left),maxDepth(root.right))
        if not root:
            return True
        lh = maxDepth(root.left)
        rh = maxDepth(root.right)
        if (abs(lh - rh) <= 1) and self.isBalanced( root.left) is True and self.isBalanced( root.right) is True: 
            return True