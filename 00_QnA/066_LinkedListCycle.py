"""
LeetCode: 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        hash_map = {}
        current = head
        count = 0
        while current:
            count += 1
            if current in hash_map:
                return True
            else:
                hash_map[current] = count
            current = current.next
        return False
