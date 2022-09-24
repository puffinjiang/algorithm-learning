#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   test_qiuck_sort.py
@Time    :   2022/09/24 12:08:11
@Author  :   puffin jiang
@Version :   1.0
'''


import random

from sort.quick_sort import quick_sort


def test_quick_sort():
    arr = random.sample(range(1, 20), 8)
    assert sorted(arr) == quick_sort(arr, 0, len(arr)-1)
