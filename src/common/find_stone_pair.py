#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   find_stone_pair.py
@Time    :   2022/09/26 10:02:35
@Author  :   puffin jiang
@Version :   1.0
'''


import time


def F(arr, weight_difference):
    """
        find one stone pair in arr with weight different
        both time complexity and space complexity is O(N)
    Args:
        arr (List): weight of stone list
        weight_difference (int): weight different

    Returns:
        tuple: the weight of stone pair
    """
    try:
        exist_stone = dict()
        for i in arr:
            lower_stone = i - weight_difference
            upper_stone = i + weight_difference
            if str(lower_stone) in exist_stone:
                return (lower_stone, i)
            if str(upper_stone) in exist_stone:
                return (upper_stone, i)
            exist_stone[str(i)] = i
    except Exception as e:
        print(f"Exception with F: {e}")
    return ()


def log_time(func):

    def wrapper(args, kwargs):
        start_time = time.time()
        result = func(args, kwargs)
        end_time = time.time()
        print(f"function {func.__name__} spent: {end_time-start_time}")
        return result
    return wrapper


@log_time
def get_all_stone_pair(arr, weight_difference):
    """
        this is the implementation of question c
    Args:
        arr (List): weight of sotne list
        weight_difference (int): weight difference

    Returns:
        set(tuple): all  weight of stone pair
    """
    result = set()
    try:
        exist_stone = dict()
        for i in arr:
            lower_stone = i - weight_difference
            upper_stone = i + weight_difference
            if str(lower_stone) in exist_stone:
                result.add((lower_stone, i))
            if str(upper_stone) in exist_stone:
                result.add((i, upper_stone))
            exist_stone[str(i)] = i
    except Exception as e:
        print(f"Exception when get all stone: {e}")
    return result
