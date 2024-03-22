"""
CodingNinjas: Longest Subarray With Sum K
https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399
"""

from typing import List

### ***** Method 1 ***** ###
"""
TC => O(N)
SC => O(N)
"""


def longestSubarrayWithSumK(a: List[int], k: int) -> int:
    sum_map = dict()
    Sum = 0
    max_length = 0
    for i in range(0, len(a)):
        Sum += a[i]
        if Sum == k:
            max_length = i + 1

        rem = Sum - k
        if rem in sum_map:
            l = i - sum_map[rem]
            max_length = max(max_length, l)

        if Sum not in sum_map:
            sum_map[Sum] = i

    return max_length


### ***** Method 2 ***** ###
"""
TC => O(2N)
SC => O(1)
"""

# def longestSubarrayWithSumK(a: List[int], k: int) -> int:
#     n = len(a)
#     left = 0
#     right = 0
#     max_length = 0
#     Sum = a[0]
#     while right < n:
#         while left <= right and Sum > k:
#             Sum -= a[left]
#             left += 1
#         if Sum == k:
#             max_length = max(max_length, right - left + 1)

#         right += 1
#         if right < n:
#             Sum += a[right]
#     return max_length


array = [1, 2, 3, 1, 1, 1, 1, 1]
k = 3
print(longestSubarrayWithSumK(array, k))
