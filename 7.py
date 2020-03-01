#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date   : 2019-04-28 14:50:43
# @Author : Fei Jie (hfut_jf@aliyun.com)
# @Link   : https://flycser.github.io
# @Desc   : 


class Solution:
    def reverse(self, x):
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0

        s = []
        y = x if x > 0 else -x
        while True:
            z = y % 10
            s.append(z)
            y -= y % 10
            y = y / 10
            if y == 0:
                break
        
        w = 0
        for i, c in enumerate(s):
            w = w * 10 + c
        if x < 0:
            w = -w

        if w > 2 ** 31 - 1 or w < -2 ** 31:
            return 0

        return int(w)


if __name__ == '__main__':
     
     x = 1534236469
     solution = Solution()
     x = solution.reverse(x)
     print(x)

        
