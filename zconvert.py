# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : zconvert.py
# @Author: Frank
# @Date  : 2018-10-05

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I



'''

# PAYP-00A0-0L00-ISHI-00R0-0I00-NG00
# P00I00N-A0LS0IG-YA0HR00-P00I000
#
# PAYPA-000L0-00I00-0S000-HIRIN-000G0
#
# [len(s)//8+1]*numRows

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    sl = list(s)
    try:
        while len(sl) % (2*(numRows-1)) != 0:
            sl.append(0)
        #print(sl)

        matrix = []
        cnt = (len(sl)//(2*numRows-2))*(numRows-1)
        #print(cnt)
        for i in range(cnt):
            matrix.append([])
            for k in range(numRows):
                matrix[i].append(0)
        #print(matrix)


        for i in range(cnt):
            t = i // (numRows - 1)
            n = i%(numRows-1)

            if n == 0:
                matrix[i] = sl[t*2*(numRows-1):t*2*(numRows-1)+numRows]
                #此部分仍存在问题,请注意检查
            else:
                matrix[i][-n-1] = sl[t*2*(numRows-1)+numRows+n-1]

        #print(matrix,len(matrix))

        textlist = [matrix[i][j] for j in range(numRows) for i in range(len(matrix)) if matrix[i][j] != 0]
        return ''.join(textlist)
    except ZeroDivisionError:
        return s
import time
start = time.time()
print(convert("pdhoozufbkgswhmwruzpdfgysycpvmwlrfzfevkhitagaoctiejnlrodpqskeqxvwzccwpkekmkmapgltryeimjzeblirjfpkksgzeljqxvsmddhueleswdxxrhrapgmzasaeflwdippmuxiykpthssgjzzlqgxrisrnxelanaszxrjxdyqmtiteksqaapsljlahqljdodeluniamzmhhhltcduevopebpnrdzwrcaczqmzelnlvvwozakdvyvbakptpoqgqskrixqmkezfbwwaygfthauhnlcczsjsnvjvsakdgjkjhglfpqawrxfeijiietcrplmhnymvixepfpvwivuzsbfdlnnpjpgyaufotslbrqsyhpvpnpohrvkclxtumzsptzfmtqpkgkjqzefmvwumteqeejaskuheumsndkalulbtrhimfczyirdmdffnaotwbmlgyltsyvnpevclxdjiuowxudnwsgsvufdsrwkrtahzvjkvoudikbiefvaxduuyaxqtvdkpdtqacbvqxabhclohiqgllcjnzciwfulkockqfgjcimlkxztfqbsddeqeiybnsozgsjzzrkdawpmtqiaglujrabxibyxwpwejgfjxpmzlboguwiahfmafpyorylpnitxqzipoupcyfisbtukyildyjtrhhgxpzwhyewpanrasbstupguxtavevmncsktui",
503))
end = time.time()
print(end-start)

