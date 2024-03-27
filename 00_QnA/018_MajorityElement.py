"""
LeetCode: 169. Majority Element
https://leetcode.com/problems/majority-element/description/
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    ### *****Moore's Algorithm***** ###
    ct = 0
    element = nums[0]
    for i in nums:
        if i == element:
            ct += 1
        else:
            ct -= 1
        if ct == 0:
            element = nums[i]
            ct = 1
    return element


### ***** Method 1 **** ###
# def majorityElement(self, nums: List[int]) -> int:
#     num_map = {}
#     k = len(nums) // 2
#     for i in nums:
#         num_map[i] = num_map.get(i, 0) + 1
#         if num_map.get(i) > k:
#             return i


### ***** Method 2 **** ###
# def majorityElement(self, nums: List[int]) -> int:
#     for i in nums:
#         if nums.count(i) > len(nums)//2:
#             return i


### ***** Method 3 **** ###
# def majorityElement(self, nums: List[int]) -> int:
#     nums.sort()
#     return nums[len(nums) // 2]


array = [1, 3, 3, 1, 3, 1, 3, 2, 2, 3]
print(majorityElement(array))
