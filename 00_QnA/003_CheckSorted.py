"""
Naukri Code 360: Check Sorted Array
https://www.naukri.com/code360/problems/ninja-and-the-sorted-check_6581957
"""

from typing import List


def isSorted(n: int, a: List[int]) -> int:
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            return 0
    return 1


print(isSorted(5, [1, 2, 3, 4, 5]))
