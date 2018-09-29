# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : Two_Sum.py
# @Author: Frank
# @Date  : 2018-09-26

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    '''以下是原答案'''
    nums1 = [x  for x in nums if x< target+1]
    print(nums1)
    a=0
    b=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                a=i
                b=j
                print(a,b)
            else:
                pass
    if a==b:
        return []
    else:
        return [a,b]

print(twoSum([0,4,3,0],0))
