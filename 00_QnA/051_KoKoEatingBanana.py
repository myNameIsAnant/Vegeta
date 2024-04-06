"""
LeetCode: 875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/
"""

from typing import List
from math import ceil


def minEatingSpeed(piles: List[int], h: int) -> int:
    low = 1
    high = max(piles)
    minban = float("inf")
    while low <= high:
        mid = low + ((high - low) // 2)
        tot = 0
        for i in piles:
            tot += ceil(i / mid)
        if tot <= h and mid < minban:
            minban = mid
            high = mid - 1
        elif tot > h:
            low = mid + 1
        else:
            high = mid - 1
    return minban


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))
