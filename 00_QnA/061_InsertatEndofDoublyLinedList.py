"""
Naukri Code 360: Insert at end of Doubly Linked List
https://www.naukri.com/code360/problems/insert-at-end-of-doubly-linked-list_8160464
"""


class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# Please do not change code above.


def insertAtTail(head: Node, k: int) -> Node:
    new_node = Node(k)
    if not head:
        head = new_node
        return head
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head
