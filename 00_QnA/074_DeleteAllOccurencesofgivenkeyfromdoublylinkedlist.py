"""
Naukri Code 360: Delete all occurrences of a given key in a doubly linked list
https://www.naukri.com/code360/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461
"""


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    if not head:
        return
    if head.data == k and not head.next:
        return None
    current = head
    previous = None
    while current:
        if current.data == k:
            if not previous:
                head = head.next
                if not head:
                    return None
                head.previous = previous
            else:
                previous.next = current.next
                if current.next:
                    current.next.prev = previous
        else:
            previous = current
        current = current.next
    return head
