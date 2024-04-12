"""
LeetCode: 876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ### ***** Method 1 ***** ###
        # if not head.next:
        #     return head
        # current = head
        # count = 0
        # while current:
        #     count += 1
        #     current = current.next
        # mid = count // 2 + 1
        # current = head
        # count = 0
        # while current:
        #     count += 1
        #     if count == mid:
        #         head = current
        #     current = current.next
        # return head

        ### ***** Method 2 ***** ###
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
