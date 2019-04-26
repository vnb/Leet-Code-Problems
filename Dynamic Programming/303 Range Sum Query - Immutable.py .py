#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tot = [0] * (len(nums)+1)
        for i in range(0, len(nums)):
            self.tot[i+1] = self.tot[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tot[j+1] - self.tot[i]