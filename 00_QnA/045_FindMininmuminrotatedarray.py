"""
LeetCode: 153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

from typing import List


def findMin(nums: List[int]) -> int:
    # low = 0
    # high = len(nums) - 1
    # while low < high:
    #     mid = low + ((high - low) // 2)
    #     if nums[mid] < nums[high]:
    #         high = mid
    #     else:
    #         low = mid + 1
    # return nums[low]

    low = 0
    high = len(nums) - 1
    if nums[high] >= nums[low]:
        return nums[0]
    while low <= high:
        mid = low + ((high - low) // 2)
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        else:
            if nums[mid] < nums[0]:
                high = mid - 1
            else:
                low = mid + 1

    # low = 0
    # high = len(nums) - 1
    # while low <= high:
    #     mid = low + ((high - low) // 2)
    #     if nums[mid] < nums[mid - 1]:
    #         return nums[mid]
    #     else:
    #         if nums[mid] < nums[0]:
    #             high = mid - 1
    #         else:
    #             low = mid + 1
    # return nums[0]


array = [11, 13, 15, 17]
print(findMin(array))
