"""
LeetCode: 152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
"""

from typing import List


def maxProduct(nums: List[int]) -> int:
    maxpd = pd = minpd = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            pd, minpd = minpd, pd
        pd = max(nums[i], pd * nums[i])
        minpd = min(nums[i], minpd * nums[i])
        maxpd = max(pd, maxpd)

    return maxpd


array = [2, 3, -2, 4]
print(maxProduct(array))
