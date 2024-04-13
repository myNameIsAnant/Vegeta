"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def revll(head) -> ListNode:
            previous = None
            current = head
            while current:
                cur = current.next
                current.next = previous
                previous = current
                current = cur
            return previous

        if not head or not head.next:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        revhead = revll(slow.next)
        sechead = revhead
        current = head
        while revhead:
            if current.val != revhead.val:
                return False
            current = current.next
            revhead = revhead.next
        revll(sechead)
        return True
