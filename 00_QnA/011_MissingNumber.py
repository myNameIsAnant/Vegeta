"""
LeetCode: 268. Missing Number
https://leetcode.com/problems/missing-number/description/
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
    tot = 0
    l = len(nums)
    for i in nums:
        tot += i
    soe = (l * (l + 1)) // 2
    return soe - tot


array = [0, 1, 2, 4, 5, 6]
print(missingNumber(array))
