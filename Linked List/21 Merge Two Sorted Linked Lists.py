#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def helper_merge(l1, l2):
            
            # init step
            start1 = l1
            start2 = l2
            newList = None
            if start1.val > start2.val:
                newList = start2
                start2 = start2.next
            else:
                newList = start1
                start1 = start1.next
                
            # running algorithm
            runner = newList
            while start1 and start2:
                x = start1.val
                y = start2.val
                if x > y:
                    runner.next = start2
                    start2 = start2.next
                else:
                    runner.next = start1
                    start1 = start1.next
                runner = runner.next
        
            if start1:
                runner.next = start1
            if start2:
                runner.next = start2
        
            return newList
            
        # basic checks
        if not l1:
            return l2
        if not l2:
            return l1
        return helper_merge(l1, l2)

            
            
            