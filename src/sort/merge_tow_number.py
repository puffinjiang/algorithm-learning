#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : merge_tow_number.py
@Datetime   : 2021/10/9
@Site       :
@Software   : PyCharm

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]  # 处理m==0，n > 0的情况
        return nums1

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n - 1
        while start < end:
            mid = start + (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start


def test_merge():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    assert [1] == Solution().merge(nums1, m, nums2, n)
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    assert [1, 2, 2, 3, 5, 6] == Solution().merge(nums1, m, nums2, n)
