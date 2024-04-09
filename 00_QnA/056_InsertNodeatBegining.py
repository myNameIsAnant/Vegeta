"""
Naukri Code 360: Insert Node At The Beginning
https://www.naukri.com/code360/problems/insert-node-at-the-beginning_8144739
"""


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Do not change code above.
def insertAtFirst(list: Node, newValue: int) -> Node:
    new_node = Node(newValue)
    new_node.next = list
    list = new_node
    return list
