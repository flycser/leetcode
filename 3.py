#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 22:26:02
# @Author  : Fei Jie (hfut_jf@aliyun.com)
# @Link    : https://flycser.github.io
# @Version : $Id$

class Solutoin:
    def lengthOfLongestSubstring(self, s):
        x = ''
        sublen = 0
        start = 0
        len_list = []
        for i, c in enumerate(s):
            ind = x.find(c)
            if ind < 0:
                sublen += 1
                x += c
            else:
                len_list.append(sublen)
                sublen = len(x) - ind
                x = x[x.find(c)+1:] + c
                print(i, ind, x, len_list)

        len_list.append(len(x))

        if len_list:
            return max(len_list)
        else:
            return 0

 
if __name__ == '__main__':
    solution = Solutoin()
    x = solution.lengthOfLongestSubstring(" ")
    print(x)




