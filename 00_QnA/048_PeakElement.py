"""
LeetCode: 162. Find Peak Element
https://leetcode.com/problems/find-peak-element/description/
"""

from typing import List


def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 1 or nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums) - 1
    low = 1
    high = len(nums) - 2
    while low <= high:
        mid = low + ((high - low) // 2)
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid] > nums[mid + 1]:
            high = mid - 1
        else:
            low = mid + 1


array = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(array))
