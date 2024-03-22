"""
LeetCode: 485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/description/
"""

from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    el = ct = 0
    for i in nums:
        if i == 1:
            ct += 1
        else:
            if ct > el:
                el = ct
            ct = 0
    return max(el, ct)


array = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(array))
