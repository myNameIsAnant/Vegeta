"""
Naukri Code 360: Find length of Loop
https://www.naukri.com/code360/problems/find-length-of-loop_8160455
"""


class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            lenloop = 1
            while slow != fast:
                slow = slow.next
                lenloop += 1
            return lenloop
    return 0
