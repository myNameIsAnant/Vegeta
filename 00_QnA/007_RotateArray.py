"""
LeetCode: 189. Rotate Array
https://leetcode.com/problems/rotate-array/description/
"""

from typing import List


def rotate(nums: List[int], k: int) -> None:
    
    def reverse(l, r):
        while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
    n = len(nums)
    
    k %= n  # Handle cases where k > n
    reverse(0, n - 1)  # Reverse the entire array
    reverse(0, k - 1)  # Reverse the first k elements
    reverse(k, n - 1)