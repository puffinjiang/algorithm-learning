#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : bubble_sort.py
@Datetime   : 2021/9/17
@Site       :
@Software   : PyCharm

"""


def bubble_sort(arr: list):
    """
        冒泡排序：比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    a = [5, 4, 3, 2, 78, 85]
    assert [2, 3, 4, 5, 78, 85] == bubble_sort(a)