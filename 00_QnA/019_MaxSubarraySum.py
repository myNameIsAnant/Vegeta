"""
LeetCode: 53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/description/
"""
### Kadane's Algorithm
from typing import List


def maxSubArray(nums: List[int]) -> int:
### ***** Kadane's Algorithm ***** ###
    maxsum = float("-inf")
    sum = 0
    for i in nums:
        sum += i
        if sum > maxsum:
            maxsum = sum      
        if sum < 0:
            sum = 0
    return maxsum


nums = [-2, -5, -7, -9]
print(maxSubArray(nums))
