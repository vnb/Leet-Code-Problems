#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

 



 

Return its postorder traversal as: [5,6,3,2,4,1].

 
Note:

Recursive solution is trivial, could you do it iteratively?
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        sol = self.helper(root, [])
        if root:
            sol.append(root.val)
        return sol
        
    def helper(self, root, traversal):
        if root:
            for i in root.children:
                self.helper(i, traversal)
                traversal.append(i.val)   
            return traversal
        
        return traversal
        
