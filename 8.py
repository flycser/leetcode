#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date   : 2019-04-29 12:26:01
# @Author : Fei Jie (hfut_jf@aliyun.com)
# @Link   : https://flycser.github.io
# @Desc   : 


class Solution:
    def myAtoi(self, str):

        i = 0
        tag = False
        new_str = ''
        z = '0123456789'
        while True:
            if i >= len(str):
                break

            if str[i] in z + '-+' and not tag:
                tag = True
                new_str += str[i]
            elif str[i] not in z + '-+ ' and not tag:
                return 0
            elif str[i] in z and tag:
                new_str += str[i]
            elif str[i] not in z and tag:
                break

            i+= 1

            print(i, new_str)

        x = 1

        if new_str == '':
            return 0
        elif new_str[0] == '+':
            x = 1
            new_str = new_str[1:]
        elif new_str[0] == '-':
            x = -1
            new_str = new_str[1:]
        
        y = 0
        for c in new_str:
            y = y * 10 + int(c)

        y = x * y
        if y > 2 ** 31 - 1:
            y = 2 ** 31 - 1
        elif  y < -2 ** 31:
            y = -2 ** 31

        print(y)
        return y


if __name__ == '__main__':

    x = ' + 0 123'
    solution = Solution()
    solution.myAtoi(x)