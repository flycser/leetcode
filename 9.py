#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date   : 2019-04-29 16:41:01
# @Author : Fei Jie (hfut_jf@aliyun.com)
# @Link   : https://flycser.github.io
# @Desc   : 


class Solution:
    def isPalindrome(self, x):

        if x < 0:
            return False

        y = []
        while True:
            z = int(x / 10)
            w = x % 10
            print(z, w)
            if 0 == z:
                y.append(w)
                break
            else:
                x -= w
                x = int(x / 10)
                y.append(w)

        print(y)
        start = 0
        end = len(y) - 1
        tag = True
        while not start == end and not end - start == -1:
            print(start, y[start], end, y[end])
            if not y[start] == y[end]:
                tag = False
                break

            start += 1
            end -= 1

        return tag

        
if __name__ == '__main__':
    
    x = 1312131

    solution = Solution()
    tag = solution.isPalindrome(x)
    print(tag)