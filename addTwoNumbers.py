# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : addTwoNumbers.py
# @Author: Frank
# @Date  : 2018-09-26

'''给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
'''tips:object of type 'ListNode' has no len()'''

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    i = 0
    l3 = []
    while l1[i]!=None and l2[i]!=None:
        l3.append(l1[i] + l2[i] + carry)
        if l3[i]>9:
            l3[i] = l3[i]%10
            carry = 1
        else:
            carry = 0
        i+=1
        print(l3)
    return l3
addTwoNumbers([2,4,3],[5,6,4])


