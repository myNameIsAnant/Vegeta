"""
Left Rotate an Array by One
https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278
"""

from typing import List


def rotateArray(arr: List[int], n: int) -> List[int]:
    arr[:-1], arr[-1] = arr[1:], arr[0]
    return arr


array = [1, 2, 3, 4, 5]
a = len(array)
print(rotateArray(array, a))
