"""
LeetCode: 229. Majority Element II
https://leetcode.com/problems/majority-element-ii/description/
"""

from typing import List


def majorityElement(self, nums: List[int]) -> List[int]:
    n = len(nums) // 3 + 1
    hash_map = {}
    for i in nums:
        hash_map[i] = hash_map.get(i, 0) + 1
    result = []
    for k, v in hash_map.items():
        if v >= n:
            result.append(k)
    return result


array = [1, 2]
print(majorityElement(array))
