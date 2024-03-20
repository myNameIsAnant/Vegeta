"""
CodingNinjas: Largest Element in the Array
https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279
"""

from typing import List


def largestElement(arr: List[int], n: int) -> int:
    maxvalue = float("-inf")
    for i in range(n):
        if arr[i] > maxvalue:
            maxvalue = arr[i]
    return maxvalue


array = [4, 16, 9, 64, 25, 1, 36, 49]
print(largestElement(array, len(array)))
