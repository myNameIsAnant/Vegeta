"""
LeetCode: 35. Search Insert Position
https://leetcode.com/problems/search-insert-position/description/
"""

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low


array = [1, 3, 5, 6]
print(searchInsert(array, 5))
