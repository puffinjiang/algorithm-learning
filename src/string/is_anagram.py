#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : is_anagram.py
@Datetime   : 2021/10/2
@Site       :
@Software   : PyCharm

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

            注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

            示例 1:
            输入: s = "anagram", t = "nagaram"
            输出: true

            示例 2:
            输入: s = "rat", t = "car"
            输出: false

            提示:
                1 <= s.length, t.length <= 5 * 104
                s 和 t 仅包含小写字母

        :param s:
        :param t:
        :return:
        """
        str_dict1 = {}
        if len(s) != len(t):
            return False
        for i in t:
            str_dict1[i] = str_dict1.get(i, 0) + 1
        for i in s:
            count = str_dict1.get(i, 0) - 1
            if count < 0:
                return False
            str_dict1[i] = count
        return True


def test_is_anagram():
    s = "anagram"
    t = "nagaram"
    assert True == Solution().isAnagram(s, t)
    s1 = "rat"
    t2 = "car"
    assert False == Solution().isAnagram(s1, t2)
