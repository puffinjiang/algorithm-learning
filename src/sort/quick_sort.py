#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   quick_sort.py
@Time    :   2022/09/24 17:34:37
@Author  :   puffin jiang
@Version :   1.0
'''


def partition(arr, left, right):
    index = left
    for i in range(left + 1, right + 1):
        if arr[i] < arr[left]:
            index += 1
            arr[index], arr[i] = arr[i], arr[index]

    arr[index], arr[left] = arr[left], arr[index]
    return index


def quick_sort(arr, left, right):
    if left < right:
        index = partition(arr, left, right)
        quick_sort(arr, left, index-1)
        quick_sort(arr, index + 1, right)
    return arr
