"""
Linear Search
https://www.codingninjas.com/studio/problems/linear-search_6922070
"""

from typing import List


def linearSearch(n: int, num: int, arr: List[int]) -> int:
    for i in range(n):
        if arr[i] == num:
            return i
    return -1


array = [6, 7, 8, 4, 1]
n = len(array)
num = 4

print(linearSearch(n, num, array))
