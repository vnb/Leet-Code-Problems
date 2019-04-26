#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def binaryTreePaths(root):
            """
            :type root: TreeNode
            :rtype: List[str]
            """
            if not root:
                return []
            else:
                return [[root.val]+ path for kid in (root.left, root.right) if kid
                       for path in binaryTreePaths(kid)] or [[root.val]]
        all_paths = binaryTreePaths(root)
        vals_index = {}
        for i in all_paths:
            if x in i:
                vals_index[x] = [i.index(x), i]
            if y in i:
                vals_index[y] = [i.index(y), i]
        
        if vals_index[y][0] != vals_index[x][0]:
            return False
        if vals_index[y][1][vals_index[y][0]-1] != vals_index[x][1][vals_index[x][0]-1]:
            return True