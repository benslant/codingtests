
from typing import List


class LinkedListNode():

    def __init__(self, value: object, next: 'LinkedListNode') -> None:
        self.value = value
        self.next = next


class LinkedList():

    def __init__(self) -> None:
        self.head: LinkedListNode = None
        self.tail: LinkedListNode = None

    def prepend(self, value: object):
        new_node = LinkedListNode(value, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def append(self, value: object):
        new_node = LinkedListNode(value, None)
        if not self.head:
            self.head = new_node
        if self.tail: 
            self.tail.next = new_node
        self.tail = new_node

    def __repr__(self) -> str:
        current_node = self.head
        result: List[object] = []
        while True:
            result.append(current_node.value)
            current_node = current_node.next
            if not current_node: break
        return str(result)


def linked_list():
    pass