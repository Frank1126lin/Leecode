# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : Longest_substring.py
# @Author: Frank
# @Date  : 2018-09-27

'''Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.'''


def lengthofLongestSubstring(s):
    '''
    :type s: str
    :rtype: int
    '''
    if s == '':
        return 0
    else:
        num=0
        for i in range(len(s)):
            cnt = 0
            j = 0

            while j < len(s)-i:
                if s[i+j] not in s[i:i+j]:
                    cnt = j
                    j+=1
                    print(i,j,cnt)
                else:
                    break
            if cnt>num:
                num = cnt
        return num+1

s = "abcabcbb"
print(lengthofLongestSubstring(s))


