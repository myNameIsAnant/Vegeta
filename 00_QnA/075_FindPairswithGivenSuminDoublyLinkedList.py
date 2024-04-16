"""
Naukri Code 360: Find pairs with given sum in doubly linked list
https://www.naukri.com/code360/problems/find-pairs-with-given-sum-in-doubly-linked-list_1164172
"""

from typing import List


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int) -> List[int]:
    r = l = head
    result = []
    while r.next:
        r = r.next
    while l.data < r.data:
        if l.data + r.data == k:
            result.append([l.data, r.data])
            l = l.next
            r = r.prev
        elif l.data + r.data < k:
            l = l.next
        else:
            r = r.prev
    return result
