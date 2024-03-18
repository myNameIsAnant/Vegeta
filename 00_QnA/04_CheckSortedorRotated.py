"""
Leet Code: 1752. Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
"""

from typing import List


def check(nums: List[int]) -> bool:
    newlist = []
    for i in range(len(nums) - 1):
        if nums[i + 1] < nums[i]:
            newlist = nums[i + 1 :] + nums[: i + 1]
            break
    if not newlist:
        return True
    else:
        for i in range(len(newlist) - 1):
            if newlist[i + 1] < newlist[i]:
                return False
        return True


print(check([3, 4, 5, 1, 2]))
