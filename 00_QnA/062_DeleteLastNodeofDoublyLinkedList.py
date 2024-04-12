"""
Naukri Code 360: Delete Last Node of a Doubly Linked List
https://www.naukri.com/code360/problems/delete-last-node-of-a-doubly-linked-list_8160469
"""


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node:
    if not head:
        return
    if not head.next:
        return None
    current = head
    while current.next:
        previous = current
        current = current.next
    previous.next = None
    return head
