"""
Naukri Code 360: Introduction To Doubly Linked List
https://www.naukri.com/code360/problems/introduction-to-doubly-linked-list_8160413
"""

from typing import List

class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def constructDLL(arr: List[int]) -> Node:
    head = None
    for i in range(len(arr)):
        curr_node = Node(arr[i])
        if not head:
            head = curr_node
            current = head
        else:
            prev_node = current
            cur = curr_node
            current.prev = current
            prev_node.next = cur
            current = cur
            
    return head