"""
LeetCode: 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

from typing import List


def search(nums: List[int], target: int) -> int:

    ### ***** Approach 1 ***** ###
    # for i in range(len(nums)):
    #         if nums[i] == target:
    #             return i
    # return -1

    ### ***** Approach 2 ***** ###
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


array = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(array, target))
