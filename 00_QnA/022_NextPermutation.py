"""
LeetCode: 31. Next Permutation
https://leetcode.com/problems/next-permutation/
"""

from typing import List


def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    ind = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            ind = i
            break
    if ind == -1:
        nums.reverse()
        return nums
    for i in range(n - 1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break
    nums[ind + 1 :] = reversed(nums[ind + 1 :])


array = [1, 5, 4, 3, 2]
nextPermutation(array)
print(array)

nums = [1, 2, 3, 4, 5]
nums[-2:] = nums[-1:-3:-1]
print(nums)
