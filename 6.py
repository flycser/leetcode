#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date   : 2019-04-27 23:25:00
# @Author : Fei Jie (hfut_jf@aliyun.com)
# @Link   : https://flycser.github.io
# @Desc   : 


class Solution:
    def convert(self, s, numRows):

        new_sub_strs = []
        numBlock = 2 * numRows - 2
        if numBlock <= 0:
            return s
        x = int(len(s) / numBlock)

        for i in range(x):
            cur_sub_str = s[i*numBlock:(i+1)*numBlock]
            new_sub_strs.append(cur_sub_str[:numRows])
            for j, z in enumerate(cur_sub_str[numRows:]):
                k = numRows - len(z + (j + 1) * ' ')
                cur_sub_str = ' ' * k + z + (j + 1) * ' '
                new_sub_strs.append(cur_sub_str)

        if len(s) % numBlock <= numRows:
            new_sub_strs.append(s[x*numBlock:] + ' ' * (numRows - len(s) % numBlock))
        else:
            cur_sub_str = s[x*numBlock:]
            new_sub_strs.append(cur_sub_str[:numRows])
            for j, z in enumerate(cur_sub_str[numRows:]):
                k = numRows - len(z + (j+1) * ' ')
                cur_sub_str = ' ' * k + z + (j+1) * ' '
                new_sub_strs.append(cur_sub_str)

        new_str = ''
        for i in range(numRows):
            for sub_str in new_sub_strs:
                c = sub_str[i]
                if not c == ' ':
                    new_str += c

        return new_str


if __name__ == '__main__':

    s = 'A'
    numRows = 1

    solution = Solution()
    new_str = solution.convert(s, numRows)
    print(new_str)
    