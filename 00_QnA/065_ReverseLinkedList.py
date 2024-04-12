"""
LeetCode: 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return
    if not head.next:
        return head
    tail = head
    current = head.next
    tail.next = None
    previous = tail
    while current.next:
        cur = current.next
        current.next = previous
        previous = current
        current = cur
    current.next = previous
    head = current
    return head
