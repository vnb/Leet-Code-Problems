#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def invertTree(root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            if not root:
                return 
            root.left, root.right = root.right, root.left
            invertTree(root.left)
            invertTree(root.right)
            return root        
        def isSameTree(p, q):
            """
            :type p: TreeNode
            :type q: TreeNode
            :rtype: bool
            """
            
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
        if not root:
            return True
        return isSameTree(root.left, invertTree(root.right))
        
        