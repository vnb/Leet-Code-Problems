#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []
        def levelOrder(root, res):
            if not root:
                return res
            levelOrder(root.left, res)
            res.append(root.val)
            levelOrder(root.right, res)
            return res
        all_nodes = levelOrder(root, [])
        print(all_nodes)
        for i in range(len(all_nodes)):
            ans = k - all_nodes[i]
            if ans in all_nodes[i:] and ans != all_nodes[i]:
                return True
        return False