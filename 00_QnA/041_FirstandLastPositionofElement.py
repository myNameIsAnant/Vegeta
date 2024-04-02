"""
LeetCode: 34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
### ***** Approach 1 ***** ###
    # low = 0
    # high = len(nums) - 1
    # st = sp = 0
    # while low <= high:
    #     mid = (low + high) // 2
    #     if nums[mid] == target:
    #         i = mid - 1
    #         j = mid + 1
    #         st = sp = mid
    #         while i >= 0 and nums[i] == target:
    #             if nums[i] == target:
    #                 st -= 1
    #             i -= 1
    #         while j < len(nums) and nums[j] == target:
    #             if nums[j] == target:
    #                 sp += 1
    #             j += 1
    #         return [st, sp]
    #     elif nums[mid] > target:
    #         high = mid - 1
    #     else:
    #         low = mid + 1
    # return [-1, -1]

### ***** Approach 2 ***** ###
    def binarySearch(nums, target, searching_left):
        low = 0
        high = len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                if searching_left:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index

    left = binarySearch(nums, target, True)
    if left == -1:
        return [-1,-1]
    right = binarySearch(nums, target, False)
    return [left, right]

array = [5, 7, 7, 8, 8, 10]
print(searchRange(array, 8))
