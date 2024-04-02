"""
Naukri Code 360: Implement Upper Bound
https://www.naukri.com/code360/problems/implement-upper-bound_8165383
"""

from typing import List


def upperBound(arr: List[int], x: int, n: int) -> int:
    low = 0
    high = n - 1
    ub = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub


array = [9, 9, 12, 12, 14, 19, 19, 28, 36, 38, 41, 45]
target = 28
print(upperBound(array, target, len(array)))
