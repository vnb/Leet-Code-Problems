#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head

        dummy = {}
        i = 1
        while current:
            dummy[i] = current
            if current.next:
                current = current.next
                i += 1
            else:
                break
        
        j = 1
        i = i-1
        while i > 0 :
            if dummy[i].next.val == dummy[j].val:
                i = i - 1
                j = j + 1
            else:
                return False
        return True
        