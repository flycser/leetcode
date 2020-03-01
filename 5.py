#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date   : 2019-04-19 12:56:37
# @Author : Fei Jie (hfut_jf@aliyun.com)
# @Link   : https://flycser.github.io
# @Desc   : 

class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        x = s[0]
        i = start = end = 0
        while True:
            if i == len(s):
                break

            print(i, s[i])
            # find median character
            if i-1 >= 0 and i+1 < len(s) and s[i-1] == s[i+1]: # odd
                start = i - 1
                end = i + 1
                k = 2
                while True:
                    if i-k >= 0 and i+k < len(s) and s[i-k] == s[i+k]:
                        start = i - k
                        end = i + k
                        k += 1
                    else:
                        break

                if len(s[start:end+1]) > len(x):
                    x = s[start:end+1]
                    print('odd', i, start, end, x)

            if i+1 < len(s) and s[i] == s[i+1]: # even
                start = i
                end = i + 1
                k = 2
                while True:
                    if i-k+1 >= 0 and i+k < len(s) and s[i-k+1] == s[i+k]:
                        start = i - k + 1
                        end = i + k
                        k += 1
                    else:
                        break
                
                if len(s[start:end+1]) > len(x):
                    x = s[start:end+1]
                    print('even', i, start, end, x)
                
            i += 1

        return x


if __name__ == '__main__':

    # babad - bab, cbbd - bb
    solution = Solution()
    x = solution.longestPalindrome('')
    print(x)
