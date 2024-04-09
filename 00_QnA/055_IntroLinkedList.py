"""
Naukri Code 360: Introduction To Linked List
https://www.naukri.com/code360/problems/introduction-to-linked-list_8144737
"""

from typing import List


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def constructLL(arr: List[int]) -> Node:
    head = None
    for i in arr:
        new_node = Node(i)
        if not head:
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
    return head


array = [30, 6, 50, 2, 3, 4, 8, 7, 34, 40, 29, 19, 12, 35, 6]
print(constructLL(array).val)
