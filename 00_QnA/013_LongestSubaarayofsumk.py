"""
CodingNinjas: Longest Subarray With Sum K
https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399
"""


from typing import List


def longestSubarrayWithSumK(a: List[int], k: int) -> int:
    n = len(a)
    left = 0
    right = 0
    max_length = 0
    Sum = a[0]
    while right < n:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1
        if Sum == k:
            max_length = max(max_length, right - left + 1)

        right += 1
        if right < n:
            Sum += a[right]
    return max_length


array = [1, 2, 3, 1, 1, 1, 1, 1]
k = 3
print(longestSubarrayWithSumK(array, k))
