# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : longestPalindrome.py
# @Author: Frank
# @Date  : 2018-09-30

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

#定义回文字串函数:

def palindrome(s):
    if len(s) <2:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    the O() of this kind of the function is too large for a long string.
    still need to improve.
    """
    # if we use the def of palindrom():
    #p_s = [s[i:i+j] for i in range(len(s)) for j in range(len(s)-i+1) if palindrome(s[i:i+j])]

    # and if we donot use the def:
    p_s = [s[i:i + j] for i in range(len(s)) for j in range(len(s) - i + 1) if s[i:i+j] == s[i:i+j][::-1]]
    '''equal to the code next:
    p_s = []
    for i in range(len(s)):
        for j in range(len(s)-i):
            if palindrome(s[i:i+j+1]):
                p_s.append(s[i:i+j+1])
                '''
    # print(p_s)
    n_s = [len(item) for item in p_s]
    # print(n_s)

    for i in range(len(n_s)):
        if n_s[i] == max(n_s):
            return p_s[i]
    return ''


s = ''
print(longestPalindrome(s))


