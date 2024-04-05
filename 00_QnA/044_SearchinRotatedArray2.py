"""
LeetCode: 81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
"""

from typing import List


def search(nums: List[int], target: int) -> bool:

    ### ***** Approach 1 ***** ###

    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return True
    # return False

    ### ***** Approach 2 ***** ###
    return target in nums

    ### ***** Approach 3 ***** ###
    pass


array = [2, 5, 6, 0, 0, 1, 2]
target = 0
print(search(array, target))
