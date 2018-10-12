# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : reversenum.py
# @Author: Frank
# @Date  : 2018-10-12

def reversenum(x):
    """
    :type x: int
    :rtype: int
    """

    if x < 0 and x > -2**31 and int(str(-x)[::-1]) < 2**31-1:
        return -(int(str(-x)[::-1]))
    elif x >= 0 and x < 2**31-1 and int(str(x)[::-1])<2**31-1:
        return int(str(x)[::-1])
    else:
        return 0

print(reversenum(-123))