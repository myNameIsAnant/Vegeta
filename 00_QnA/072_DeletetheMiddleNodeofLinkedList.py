"""
LeetCode: 2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            head = None
            return head
        if not head.next.next:
            head.next = None
            return head
        previous = None
        slow = fast = head
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        previous.next = slow.next
        return head
