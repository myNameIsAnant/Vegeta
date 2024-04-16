"""
Naukri Code 360: Remove duplicates from a sorted Doubly Linked List
https://www.naukri.com/code360/problems/remove-duplicates-from-a-sorted-doubly-linked-list_2420283
"""


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    if not head:
        return
    if not head.next:
        return head
    current = head.next
    previous = head
    while current:
        if current.data == previous.data:
            if not current.next:
                previous.next = None
            else:
                previous.next = current.next
                current.next.prev = previous
        else:
            previous = current
        current = current.next
    return head
