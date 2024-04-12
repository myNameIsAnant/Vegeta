"""
Naukri Code 360: Reverse A Doubly Linked List
https://www.naukri.com/code360/problems/reverse-a-doubly-linked-list_1116098
"""

"""
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
"""


def reverseDLL(head):
    if not head:
        return
    if not head.next:
        return head
    tail = head
    current = head.next
    tail.next = None
    tail.prev = current
    previous = tail
    while current.next:
        cur = current.next
        current.next = previous
        current.prev = current.next
        previous = current
        current = cur
    head = current
    head.next = previous
    head.prev = None
    return head
