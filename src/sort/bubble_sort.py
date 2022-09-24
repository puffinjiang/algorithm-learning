#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   bubble_sort.py
@Time    :   2022/09/24 11:32:29
@Author  :   puffin jiang
@Version :   1.0
'''

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    
    return arr