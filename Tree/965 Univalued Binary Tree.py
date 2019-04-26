#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
 

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#class Solution(object):
#    def isUnivalTree(self, root):
#        left_correct = (not root.left or root.val == root.left.val
#                and self.isUnivalTree(root.left))
#        right_correct = (not root.right or root.val == root.right.val
#                and self.isUnivalTree(root.right))
#        return left_correct and right_correct
    
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        find_val = root.val
        list_nodes = self.preorder_print(root, [])
        for i in list_nodes:
            if i != find_val:
                return False
        return True
        
    def preorder_print(self, start, traversal):
        if start.val
        traversal.append(start.val)
        if start.left:
            self.preorder_print(start.left, traversal)
        if start.right:
            self.preorder_print(start.right, traversal)
        return traversal

            
        