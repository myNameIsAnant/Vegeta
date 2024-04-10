class Node:
    def __init__(self, val=None) -> None:
        self.value = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self) -> None:
        if not self.head:
            print("SLL is Empty")
        else:
            current = self.head
            while current:
                if current.next:
                    print(current.value, end="->")
                else:
                    print(current.value, end="")
                current = current.next
            print()

    def search(self, target) -> bool:
        if not self.head:
            return False
        else:
            current = self.head
            while current:
                if current.value == target:
                    return True
                current = current.next
            return False

    def insert(self, data, position) -> None:
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current and count < position:
                prev_node = current
                current = current.next
                count += 1
            new_node.next = current
            prev_node.next = new_node


sll = SinglyLinkedList()
sll.append(100)
sll.append(90)
sll.append(80)
sll.append(70)
sll.append(60)
sll.append(50)
sll.traverse()
print(sll.search(60))
print(sll.search(40))
