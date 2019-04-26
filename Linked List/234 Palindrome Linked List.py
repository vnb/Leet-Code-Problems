#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.initial = None
    def helper(self, so_far):
        if not so_far:
            return True
        ans = self.helper(so_far.next)
        equal = (so_far.val == self.initial.val)
        self.intitial = self.initial.next
        return ans and equal
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.initial = head
        return self.helper(head)
        