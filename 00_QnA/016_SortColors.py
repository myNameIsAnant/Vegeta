"""
LeetCode: 75. Sort Colors
https://leetcode.com/problems/sort-colors/description/
"""

from typing import List


def sortColors(nums: List[int]) -> None:
    ### **** Dutch National Flag Algorithms **** ###
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


### **** Method 1**** ###
# def sortColors(nums: List[int]) -> None:
#     i = 0
#     while i < len(nums):
#         if nums[i] == 2:
#             break
#         i += 1
#     j = i + 1
#     while j < len(nums):
#         if nums[j] != 2:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#         j += 1
#     i = 0
#     while i < len(nums):
#         if nums[i] == 1:
#             break
#         i += 1
#     else:
#         return
#     j = i + 1
#     while j < len(nums) and nums[j] != 2:
#         if nums[j] != 1:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#         j += 1


array = [1, 0, 2, 1, 2, 2, 2, 0, 1, 2]
sortColors(array)
print(array)
