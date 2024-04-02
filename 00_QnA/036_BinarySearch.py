"""
LeetCode: 704. Binary Search
https://leetcode.com/problems/binary-search/description/
"""

from typing import List


def search(nums: List[int], target: int) -> int:
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
    return -1


array = [-1, 0, 3, 5, 9, 12]
print(search(array, 9))
