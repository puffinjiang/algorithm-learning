#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   three_sum.py
@Time    :   2023/10/22 14:54:59
@Author  :   puffin jiang
@Version :   1.0
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        result = []
        for i in range(length):
            if nums[i] > 0:
                break
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            left = i + 1
            right = length - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while (left < right and nums[left + 1] == nums[left]):
                        left += 1
                    while (left < right and nums[right -1] == nums[right]):
                        right -= 1
                    left +=1
                    right -= 1
                elif (nums[i] + nums[left] + nums[right]) < 0:
                    left +=1
                else:
                    right -= 1
            print(f"i is: {i}, result: {result}")
        return result

soultion = Solution()
soultion.threeSum([1,-1,-1,0])