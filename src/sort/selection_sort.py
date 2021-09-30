#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : selection_sort.py
@Datetime   : 2021/9/30
@Site       :
@Software   : PyCharm

"""


def selection_sort(arr: list):
    """
        选择排序：
        首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
        再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    :param arr:
    :return:
    """
    for i in range(len(arr) - 1):
        print("i: {}, arr: {}".format(i, arr))
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
