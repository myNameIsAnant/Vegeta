"""
Naukri Code 360: Rotation
https://www.naukri.com/code360/problems/rotation_7449070
"""

from typing import List


def findKRotation(arr: List[int]) -> int:
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + ((high - low) // 2)
        if arr[mid] < arr[high]:
            high = mid
        else:
            low = mid + 1
    return low
