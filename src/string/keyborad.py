#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : keyborad.py
@Datetime   : 2021/10/31
@Site       :
@Software   : PyCharm

"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyword_set1 = {'w', 'r', 'p', 't', 'u', 'y', 'e', 'o', 'q', 'i'}
        keyword_set2 = {'s', 'k', 'g', 'h', 'd', 'l', 'j', 'a', 'f'}
        keyword_set3 = {'n', 'z', 'v', 'm', 'c', 'x', 'b'}
        res = []
        for word in words:
            word_set = set(list(word.lower()))
            if word and (not word_set.difference(keyword_set1) or not word_set.difference(
                    keyword_set2) or not word_set.difference(keyword_set3)):
                res.append(word)
        return res


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(Solution().findWords(words))
