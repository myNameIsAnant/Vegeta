"""
LeetCode: 1283. Find the Smallest Divisor Given a Threshold
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
"""

from typing import List
from math import ceil


def smallestDivisor(nums: List[int], threshold: int) -> int:
    def calcThreshold(nums: List[int], mid: int) -> int:
        tot = 0
        for i in nums:
            tot += ceil(i / mid)
        return tot

    low = 1
    high = max(nums)
    ans = max(nums)
    while low <= high:
        mid = low + ((high - low) // 2)
        if calcThreshold(nums, mid) <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


array = [21212, 10101, 12121]
threshold = 1000000
print(smallestDivisor(array, threshold))
