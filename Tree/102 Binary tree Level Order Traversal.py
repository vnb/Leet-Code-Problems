#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        queue.append(root)
        result = []
        while queue:
            result.append([node.val for node in queue])
            temp = []
            for node in queue:
                temp.extend([node.left, node.right])
            queue = [leaf for leaf in temp if leaf]
        return result
                
            