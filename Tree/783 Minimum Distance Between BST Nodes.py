#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    def minDiffInBST(self, root):
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
        if len(nodes) > 2:
            min_diff = abs(nodes[-1] - nodes[0])
        for i in range(len(nodes)-1):
            if abs(nodes[i]-nodes[i+1]) < min_diff:
                min_diff = abs(nodes[i]-nodes[i+1])
                
        return min_diff
    

                
            