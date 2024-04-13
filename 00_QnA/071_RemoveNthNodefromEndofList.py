"""
LeetCode: 19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None
        cntnode = delnode = head
        while n != 0:
            cntnode = cntnode.next
            n -= 1
        if not cntnode:
            head = head.next
            return head
        while cntnode:
            previous = delnode
            delnode = delnode.next
            cntnode = cntnode.next
        if not delnode.next:
            previous.next = None
        else:
            previous.next = delnode.next
        return head
