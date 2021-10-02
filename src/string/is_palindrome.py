#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : is_palindrome.py
@Datetime   : 2021/10/2
@Site       :
@Software   : PyCharm

"""
import math
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
            给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

            说明：本题中，我们将空字符串定义为有效的回文串。

            示例 1:

            输入: "A man, a plan, a canal: Panama"
            输出: true
            解释："amanaplanacanalpanama" 是回文串

            示例 2:

            输入: "race a car"
            输出: false
            解释："raceacar" 不是回文串

            提示：

                1 <= s.length <= 2 * 105
                字符串 s 由 ASCII 字符组成

        :param s:
        :return:
        """
        result = re.sub(r'[^0-9a-zA-Z]+', '', s).lower()
        str_len = len(result)
        for i in range(math.floor(str_len / 2)):
            first, last = result[i], result[str_len - i - 1]
            if first != last:
                return False
        return True


def test_is_palindrome():
    s = "A man, a plan, a canal: Panama"
    assert True == Solution().isPalindrome(s)
    s2 = "race a car"
    assert False == Solution().isPalindrome(s2)
    s3 = "ab_a"
    assert True == Solution().isPalindrome(s3)
