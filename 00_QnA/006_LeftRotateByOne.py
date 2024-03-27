"""
Naukri Code 360: Left Rotate an Array by One
https://www.naukri.com/code360/problems/left-rotate-an-array-by-one_5026278
"""

from typing import List


def rotateArray(arr: List[int], n: int) -> List[int]:
    el = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[-1] = el
    return array


array = [1, 2, 3, 4, 5]
a = len(array)
print(rotateArray(array, a))
