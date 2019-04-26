#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def mean(ans_list):
            sum_list = 0
            for i in ans_list:
                sum_list += i
            return sum_list*1.0/len(ans_list)
        def levelOrderBottom(root):
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
        
        ans_list = levelOrderBottom(root)
        ans = []
        for i in ans_list:
            ans.append(mean(i))
            
        return ans