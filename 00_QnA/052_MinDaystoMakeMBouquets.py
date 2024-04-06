"""
LeetCode: 1482. Minimum Number of Days to Make m Bouquets
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
"""

from typing import List


def minDays(bloomDay: List[int], m: int, k: int) -> int:
    nosflower = m * k
    if nosflower > len(bloomDay):
        return -1
    ans = -1
    low = min(bloomDay)
    high = max(bloomDay)
    while low <= high:
        mid = low + ((high - low) // 2)
        bq = 0
        ct = 0
        for i in bloomDay:
            if i <= mid:
                ct += 1
                if ct >= k:
                    bq += 1
                    ct = 0
            else:
                ct = 0
        if bq >= m:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


array = [1, 10, 3, 10, 2]
nbq = 3
nfl = 1
print(minDays(array, nbq, nfl))
