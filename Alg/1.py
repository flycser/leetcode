#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 23:51:02
# @Author  : Fei Jie (hfut_jf@aliyun.com)
# @Link    : https://flycser.github.io
# @Version : $Id$

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        buff_dict = {}
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            if nums[i] in buff_dict.keys():
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
