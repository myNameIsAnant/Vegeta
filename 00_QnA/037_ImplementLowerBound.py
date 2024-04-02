"""
Naukri Code 360: Implement Lower Bound
https://www.naukri.com/code360/problems/lower-bound_8165382
"""

from typing import List


def lowerBound(arr: List[int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    lb = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb


array = [1663, 3695, 5862, 7359, 12010, 17384, 20121, 20281, 22749, 24935, 29258, 30967]
target = 6209
print(lowerBound(array, len(array), target))
