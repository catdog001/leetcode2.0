#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 8:28
# @Author  : LI Dongdong
# @FileName: 516. Longest Palindromic Subsequence.py
''''''
'''
https://www.geeksforgeeks.org/minimum-steps-to-delete-a-string-after-repeated-deletion-of-palindrome-substrings/
1.要求：Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
    Example 1:Input: "bbbab" Output: 4 One possible longest palindromic subsequence is "bbbb".
    Example 2: Input: "cbbd" Output: 2 One possible longest palindromic subsequence is "bb".
2.理解：寻找最长的，可以不连续，但有序的子序列，满足是回文要求
3.类型：string
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input:None? Y One? Y repeat? Y order? N
    output: 0/1...int
    focus on time or space? space
'''

'''
idea：DFS + judge/record
Method：
    use DFS to get all possible subsequence  # tO(2^N) sO(N)
    judge whether the subseq is the palindromic using hash table # tO(N) sO(N)
time complex: O(2^N)
space complex: O(N)
易错点：
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:  # inp:string, outp:int, find longestSubseq
        if len(s) == 0:  # edge case
            return 0
        if len(s) == 1:  # edge case
            return 1

        stack = []
        i = len(s)
        data = []  # all possible subsequence
        self.dfs(s, i, stack, data)  # store all possible subsequence

        length = 0
        for elem in stack:  # judge whether is palindromic and record its longest length
            if self.judge(elem):
                length = max(length, len(elem))
            else:
                pass
        return length

    def dfs(self, s, i, tmp, res):  # find all possible candidate
        if i == len(s):
            return

        tmp.append(s[i])
        res.append(tmp)
        self.dfs(s, i + 1, tmp, res)
        tmp.pop()
        self.dfs(s, i + 1, tmp, res)




