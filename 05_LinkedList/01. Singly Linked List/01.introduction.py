class Node:
    def __init__(self, val=None) -> None:
        self.value = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None


n1 = Node(100)
n2 = Node(92)
n3 = Node(45)

sll = SinglyLinkedList()
sll.head = n1
n1.next = n2
n2.next = n3

## 100 -> 92 -> 45
print(sll.head)
print(sll.head.value)
print(sll.head.next)
print(sll.head.next.next)
print(n3)
print(sll.head.next.next.value)


# class Xyz:
#     def __init__(self) -> None:
#         self.obj = None


# class Abc:
#     def __init__(self) -> None:
#         self.value = None


# x = Abc()
# x.value = 100

# o = Xyz()
# o.obj = x

# print(x)
# print(o.obj)
