"""
Naukri Code 360: Count nodes of linked list
https://www.naukri.com/code360/problems/count-nodes-of-linked-list_5884
"""

"""
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
"""


def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
