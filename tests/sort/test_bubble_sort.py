#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   test_bubble_sort.py
@Time    :   2022/09/24 11:42:59
@Author  :   puffin jiang
@Version :   1.0
'''


import random

import pytest

from sort.bubble_sort import bubble_sort


def test_bubble_sort():
    arr = random.sample(range(1, 20), 8)
    assert sorted(arr) == bubble_sort(arr)
