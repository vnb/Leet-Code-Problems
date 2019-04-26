#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        next_ll = head 
        list_ll = []
        while next_ll:
            list_ll.append(next_ll.val)
            next_ll = next_ll.next
        i = len(list_ll)-1
        while i >= 0:
            current.val = list_ll[i]
            current = current.next
            i -= 1
        return head
        