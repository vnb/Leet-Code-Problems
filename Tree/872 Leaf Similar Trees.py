#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves= []
        def find_leaves(root,leaves):
            if root.left:
                find_leaves(root.left, leaves)
            if root.right:
                find_leaves(root.right, leaves)
            if not root.left and not root.right:
                leaves.append(root.val)
            return leaves
        
        def check_list(a, b):
            print(a,b)
            if len(a) != len(b):
                return False
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
            return True
        a = find_leaves(root1, [])
        b = find_leaves(root2, [])
        
        return(check_list(a, b))
