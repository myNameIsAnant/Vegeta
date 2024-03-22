"""
CodingNinjas: Merge 2 Sorted Array
https://www.codingninjas.com/studio/problems/sorted-array_6613259
"""

from typing import List


def sortedArray(a: List[int], b: List[int]) -> List[int]:
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1
        elif b[j] < a[i]:
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j += 1
    while i < len(a) and result[-1] != a[i]:
        if result[-1] != a[i]:
            result.append(a[i])
        i += 1
    while j < len(b):
        if result[-1] != b[j]:
            result.append(b[j])
        j += 1
    return result


a = [1, 2, 3, 4, 4, 4, 7]
b = [2, 3, 3, 4, 4, 5, 6]
print(sortedArray(a, b))
