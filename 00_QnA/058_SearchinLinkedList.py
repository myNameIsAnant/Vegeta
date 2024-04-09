"""
Naukri Code 360: Search in a Linked List
https://www.naukri.com/code360/problems/search-in-a-linked-list_975381
"""

"""
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
"""


def searchInLinkedList(head, k):
    current = head
    while current:
        if current.data == k:
            return 1
        current = current.next
    return 0
