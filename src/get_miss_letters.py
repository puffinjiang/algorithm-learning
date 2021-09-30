#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : get_miss_letters.py
@Datetime   : 2021/9/19
@Site       :
@Software   : PyCharm

"""


def getMissingLetters(sentence: str) -> str:
    """

    :param sentence:
    :return:
    """
    default_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in sentence:
        low_case_letter = letter.lower()
        if low_case_letter in default_letters:
            default_letters.remove(low_case_letter)
    return "".join(default_letters)


def test_get_missing_letters():
    first_letter = "A quick brown fox jumps over the lazy dog"
    assert "" == getMissingLetters(first_letter)
    second_letter = "A slow yellow fox crawls under the proactive dog"
    assert "bjkmqz" == getMissingLetters(second_letter)
    third_letter = "Lions, and tigers, and bears, oh my!"
    assert "cfjkpquvwxz" == getMissingLetters(third_letter)
    forth_letter = ""
    assert "abcdefghijklmnopqrstuvwxyz" == getMissingLetters(forth_letter)
