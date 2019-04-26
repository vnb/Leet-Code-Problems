#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note: There are at least two nodes in this BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if root.left and root.right:
                    return [root.left.val, root.right.val]+helper(root.left)+helper(root.right)
            elif root.left:
                    return [root.left.val]+helper(root.left)
            elif root.right:
                    return [root.right.val]+helper(root.right)
            else:
                return []

        nodes = sorted([root.val]+helper(root))
        if len(nodes) >= 2:
            min_diff = abs(nodes[-1] - nodes[0])
            for i in range(len(nodes)-1):
                if abs(nodes[i]-nodes[i+1]) < min_diff:
                    min_diff = abs(nodes[i]-nodes[i+1])
            return min_diff
        else:
            return None
    

                
                   