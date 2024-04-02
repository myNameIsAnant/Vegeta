"""
Naukri Code 360: Longest Subarray With Zero Sum
https://www.naukri.com/code360/problems/longest-subarray-with-zero-sum_6783450
"""

from typing import List


def getLongestZeroSumSubarrayLength(arr: List[int]) -> int:
    sum_map = dict()
    Sum = 0
    max_length = 0
    for i in range(0, len(arr)):
        Sum += arr[i]
        if Sum == 0:
            max_length = i + 1

        rem = Sum - 0
        if rem in sum_map:
            l = i - sum_map[rem]
            max_length = max(max_length, l)

        if Sum not in sum_map:
            sum_map[Sum] = i

    return max_length


array = [-5, 5, -5, 5, -5]
print(getLongestZeroSumSubarrayLength(array))
