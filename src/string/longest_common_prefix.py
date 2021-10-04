#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : longest_common_prefix.py
@Datetime   : 2021/10/4
@Site       :
@Software   : PyCharm

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            编写一个函数来查找字符串数组中的最长公共前缀。

            如果不存在公共前缀，返回空字符串 ""。

            示例 1：

                输入：strs = ["flower","flow","flight"]
                输出："fl"

            示例 2：

                输入：strs = ["dog","racecar","car"]
                输出：""
                解释：输入不存在公共前缀。

        :param strs:
        :return:
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        commonPrefix = strs[0]
        index = 1
        while index < len(strs):
            pre_len = min(len(commonPrefix), len(strs[index]))
            count = 0
            for i in range(pre_len):
                if commonPrefix[i] != strs[index][i]:
                    break
                count += 1
            commonPrefix = commonPrefix[:count]
            index += 1
        return commonPrefix


def test_longest_common_prefix():
    strs = ["flower", "flow", "flight"]
    assert "fl" == Solution().longestCommonPrefix(strs)
    strs1 = ["dog", "racecar", "car"]
    assert "" == Solution().longestCommonPrefix(strs1)
