"""
LeetCode: 2149. Rearrange Array Elements by Sign
https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""

from typing import List


# def rearrangeArray(nums: List[int]) -> List[int]:
#     pos_lst = []
#     neg_lst = []
#     result = []
#     for i in nums:
#         if i > 0:
#             pos_lst.append(i)
#         else:
#             neg_lst.append(i)
#     i = j = k = 0
#     while k < len(nums):
#         if k % 2 == 0:
#             result.append(pos_lst[i])
#             i += 1
#         else:
#             result.append(neg_lst[j])
#             j += 1
#         k += 1
#     return result

def rearrangeArray(nums: List[int]) -> List[int]:
    result = [0] * len(nums)
    pos = 0
    neg = 1
    for i in range(len(nums)):
        if nums[i] > 0:
            result[pos] = nums[i]
            pos += 2
        else:
            result[neg] = nums[i]
            neg += 2
    return result


nums = [28, -41, 22, -8, -37, 46, 35, -9, 18, -6, 19, -26, -37, -10, -9, 15, 14, 31]
print(rearrangeArray(nums))
