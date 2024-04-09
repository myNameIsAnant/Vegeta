"""
Naukri Code 360: Delete Node Of Linked List
https://www.naukri.com/code360/problems/delete-node-of-linked-list_8160463
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Please do not change code above.


def deleteLast(list: Node) -> Node:
    current = list
    while current:
        if not current.next:
            previous.next = None
        previous = current
        current = current.next
    return list
