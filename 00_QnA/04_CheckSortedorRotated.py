"""
Leet Code: 1752. Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
"""

from typing import List


def check(nums: List[int]) -> bool:

    rt = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i + 1) % len(nums)]:
            rt += 1
        if rt > 1:
            return False
    return True


print(check([3, 4, 5, 1, 2]))
