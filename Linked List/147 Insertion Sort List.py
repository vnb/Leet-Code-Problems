#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = head
        
        def ll_sort(current):
            c  = current
            while c.next:
                if c.next.val - c.val < 0:
                    c.val, c.next.val = c.next.val, c.val
                else:
                    c = c.next
            return current

        def check_sort(current):
            diff = 0
            c = current
            while diff <= 0:
                if not c.next:
                    if diff <= 0:
                        return True
                    else:
                        return False
                diff = c.val - c.next.val
                c = c.next
                                
        while c and c.next:
            if check_sort(c):
                return c
            else:
                c = ll_sort(c)
        return c