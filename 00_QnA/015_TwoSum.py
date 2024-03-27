"""
LeetCode: 1. Two Sum
https://leetcode.com/problems/two-sum/description/
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for x in range(len(nums)):
        rem = target - nums[x]
        if rem in num_map:
            return [num_map.get(rem), x]
        else:
            num_map[nums[x]] = x
