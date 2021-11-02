#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : my_atoi.py
@Datetime   : 2021/10/2
@Site       :
@Software   : PyCharm

"""
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = "^\s*([+-]?\d+)"
        match = re.findall(pattern, s)
        if not match:
            return 0
        number = int(match[0])
        if number < 0:
            return max(number, -2147483648)
        return min(number, 2147483647)


def test_my_atoi():
    s = "   -91283472332"
    assert -2147483647 == Solution().myAtoi(s)
