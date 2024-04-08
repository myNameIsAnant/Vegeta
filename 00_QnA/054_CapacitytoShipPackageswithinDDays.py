"""
LeetCode: 1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
"""

from typing import List


def shipWithinDays(weights: List[int], days: int) -> int:
    if days == len(weights):
        return max(weights)
    if days == 1:
        return sum(weights)

    def checkDays(weights: List[int], mid: int) -> int:
        dayct = 0
        capacity = 0
        for i in weights:
            capacity += i
            if capacity > mid:
                dayct += 1
                capacity = i
            elif capacity == mid:
                dayct += 1
                capacity = 0
        if capacity > 0:
            return dayct + 1
        else:
            return dayct

    low = max(weights)
    high = sum(weights)
    ans = sum(weights)
    while low <= high:
        mid = low + ((high - low) // 2)
        if checkDays(weights, mid) <= days:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


array = [1, 2, 3, 1, 1]
days = 4
print(shipWithinDays(array, days))
