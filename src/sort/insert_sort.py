#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : insert_sort.py
@Datetime   : 2021/9/30
@Site       :
@Software   : PyCharm

"""


def insert_sort(arr: list):
    """
        插入排序：
        将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
        从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and current < arr[pre_index]:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr
