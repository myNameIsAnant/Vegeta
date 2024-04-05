"""
LeetCode: 540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if low == high:
            return nums[low]
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        if nums[mid] == nums[mid - 1]:
            if mid % 2 == 1:
                low = mid + 1
            else:
                high = mid - 1
        elif nums[mid] == nums[mid + 1]:
            if mid % 2 == 1:
                high = mid - 1
            else:
                low = mid + 1

    ### ***** Approach 2 ***** ###

    # curel = nums[0]
    # ct = 1
    # for i in range(1,len(nums)-1):
    #     if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
    #         return nums[i]

    ### ***** Approach 1 ***** ###

    # curel = nums[0]
    # ct = 1
    # for i in range(1,len(nums)):
    #     if nums[i] == curel:
    #         ct += 1
    #         if ct == 2:
    #             curel = nums[i + 1]
    #             ct = 0
    # return curel


array = [0, 1, 1, 2, 2, 5, 5]
print(singleNonDuplicate(array))
