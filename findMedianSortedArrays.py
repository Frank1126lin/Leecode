# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : findMedianSortedArrays.py
# @Author: Frank
# @Date  : 2018-09-27

'''here are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.



Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5'''


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums = nums1+nums2
    #print(nums)
    nums = sorted(nums)
    mid = len(nums)//2
    #print(nums,mid)
    if len(nums)%2 == 0:
        return (nums[mid]+nums[mid-1])/2
    else:
        return nums[mid]

print(findMedianSortedArrays([],[2,3]))