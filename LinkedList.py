class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        self.head:Node = Node(value)
        self.end:Node = self.head

    def __str__(self) -> str:
        string = ""
        actual_node = self.head
        while actual_node.next is not None:
            string += f"{actual_node.value}--"
            actual_node = actual_node.next
        string += f"{actual_node.value}\n"
        return string

    def _get_node(self, index:int) -> Node:
        if index == 0:
            return self.head

        node:Node = self.head
        index_node:int = 0
        while index_node != index:
            node = node.next
            index_node += 1
        return node


    def add_to_end(self, value) -> None:
        self.end.next = Node(value)
        self.end = self.end.next

    def add_to_start(self, value) -> None:
        new_node:Node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_at_index(self, index, value) -> None:
        if not index:
            self.add_to_start(value)
            return

        node:Node = self._get_node(index-1)
        new_node:Node = Node(value)
        new_node.next = node.next
        node.next = new_node


    def remove_start(self) -> None:
        self.head = self.head.next

    def remove_end(self) -> None:
        node:Node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None

    def remove_at_index(self, index:int) -> None:
        if index == 0:
            self.remove_start()
            return

        node:Node = self._get_node(index-1)
        node.next = node.next.next


    def set(self, index:int, value) -> None:
        node:Node = self._get_node(index)
        node.value = value


    def get(self, index:int):
        node:Node = self._get_node(index)
        return node.value