"""
LeetCode: 148. Sort List
https://leetcode.com/problems/sort-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        mylist = []
        current = head
        while current:
            mylist.append(current.val)
            current = current.next
        mylist.sort()
        head = ListNode(mylist[0])
        current = head
        for i in mylist[1:]:
            current.next = ListNode(i)
            current = current.next
        return head
