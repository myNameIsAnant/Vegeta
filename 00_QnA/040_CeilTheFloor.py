"""
Naukri Code 360: Ceil The Floor
https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401
"""

from typing import List


def getFloorAndCeil(a: List[int], n: int, x: int) -> List[int]:
    f = c = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return [a[mid], a[mid]]
        elif a[mid] > x:
            c = a[mid]
            high = mid - 1
        else:
            f = a[mid]
            low = mid + 1
    return [f, c]


array = [3, 4, 4, 7, 8, 10]
print(getFloorAndCeil(array, len(array), 5))
