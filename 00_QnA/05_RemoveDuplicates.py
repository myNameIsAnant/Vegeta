"""
LeetCode: 26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 1:
        return 1
    i = 0
    j = 1
    k = []
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            nums[i + 1] = nums[j]
            i += 1
            j += 1
    return len(set(nums))


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
