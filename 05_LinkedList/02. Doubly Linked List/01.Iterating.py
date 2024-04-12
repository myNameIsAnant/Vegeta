class Node:
    def __init__(self, val=None) -> None:
        self.value = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_atHead(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_atTail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_position(self, position, data):
        new_node = Node(data)
        if not self.head:
            print("Linked List is Empty")
            return
        if position <= 0:
            self.insert_atHead()
            return
        current = self.head.next
        previous = self.head
        pos = 1
        while current:
            if pos == position or not current.next:
                if not current.next:
                    cur = new_node
                    cur.previous = current
                    current.next = cur
                    cur.next = None
                else:
                    cur = new_node
                    cur.previous = previous
                    previous.next = cur
                    cur.next = current
                    current.prev = cur
                return
            pos += 1
            previous = current
            current = current.next

    def traverse(self):
        if not self.head:
            print("Linked List is Empty")
        else:
            current = self.head
            while current:
                if current.next:
                    print(current.value, end="<->")
                else:
                    print(current.value, end="")
                current = current.next
            print()

    def delete_head(self):
        if not self.head:
            print("Linked List is Empty")
            return
        if not self.head.next:
            self.head = None
            return
        self.head.next.prev = None
        self.head = self.head.next

    def delete_tail(self):
        if not self.head:
            print("Linked List is Empty")
            return
        if not self.head.next:
            self.head = None
            return
        self.tail.prev.next = None
        self.tail = self.tail.prev

    def delete_value(self, target):
        if not self.head:
            print("Linked List is Empty")
            return
        if self.head.value == target:
            self.delete_head()
            return
        if self.tail.value == target:
            self.delete_tail()
            return
        current = self.head.next
        previous = self.head
        while current:
            if current.value == target:
                if not current.next:
                    previous.next = None
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        print("Value Not Found")


dll = DoublyLinkedList()
dll.insert_atHead(90)
dll.insert_atHead(80)
dll.insert_atHead(70)
dll.insert_atHead(60)
dll.insert_atHead(50)
dll.insert_atTail(100)
dll.traverse()
dll.delete_head()
dll.traverse()
dll.delete_tail()
dll.traverse()
dll.delete_value(100)
dll.traverse()
dll.insert_position(50, 110)
dll.traverse()
