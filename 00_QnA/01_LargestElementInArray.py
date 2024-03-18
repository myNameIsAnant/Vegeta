"""
 Largest Element in the Array
https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279
"""

from typing import List


def largestElement(arr: List[int], n: int) -> int:
    i = 0
    j = n - 1
    maxvalue = float("-inf")
    for i in range(n):
        if arr[i] > maxvalue:
            maxvalue = arr[i]
    return maxvalue


print(largestElement([4, 7, 8, 6, 7, 6], 6))
