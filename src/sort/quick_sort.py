#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : quick_sort.py
@Datetime   : 2021/10/9
@Site       :
@Software   : PyCharm

"""


def partition(arr, low, high):
    index = low
    pivot = arr[low]  # 选择第一个数作为基数
    for i in range(low + 1, high + 1):
        if arr[i] < pivot:  # 比较当前数和基数的大小，小的放前面，大的放后面
            index += 1
            arr[i], arr[index] = arr[index], arr[i]
    arr[low], arr[index] = arr[index], arr[low]
    return index


def quick_sort(arr, low, high):
    if low < high:
        index = partition(arr, low, high)
        quick_sort(arr, low, index - 1)
        quick_sort(arr, index + 1, high)


def test_quick_sort():
    arr = [1, 5, 7, 3, 9, 2, 4]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
