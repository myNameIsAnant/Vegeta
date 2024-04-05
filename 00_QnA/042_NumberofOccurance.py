"""
Naukri Code 360: Number of Occurrence
https://www.naukri.com/code360/problems/occurrence-of-x-in-a-sorted-array_630456
"""

from typing import List


def count(arr: List[int], n: int, x: int) -> int:
    def binsearch(arr, target, srchleft):
        l = 0
        h = n - 1
        ind = -1
        while l <= h:
            m = l + ((h - l) // 2)
            if arr[m] == target:
                ind = m
                if srchleft:
                    h = m - 1
                else:
                    l = m + 1
            elif arr[m] > target:
                h = m - 1
            else:
                l = m + 1
        return ind

    st = binsearch(arr, x, True)
    if st == -1:
        return 0
    sp = binsearch(arr, x, False)
    return sp - st + 1


array = [2, 4, 10, 10, 10, 10, 10, 10, 11, 12, 14, 14, 17, 19, 19]
print(count(array, len(array), 10))
