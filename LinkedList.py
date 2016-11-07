from Node import Node


class LinkedListIterator:
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        while self.current is not None:
            tmp = self.current.val
            self.current = self.current.next
            return tmp
        raise StopIteration


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __len__(self):
        return self.count

    def reset(self):
        self.head = None

    def get_node(self, index):
        counter = 0
        tmp = self.head
        while counter != index:
            counter += 1
            tmp = tmp.next
        return tmp

    def __getitem__(self, key):  # this is for hash table
        for item in self:
            if item[0] == key:
                return item[1]
        raise KeyError("Key is not in the list")

    def __contains__(self, key):  # this is for hash table
        for item in self:
            if item[0] == key:
                return item[1]
        raise KeyError("Key is not in the list")

    def add(self, item):
        if self.head is None:
            self.head = Node(item)
            self.count += 1
            return True
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)
            self.count += 1
            return True

    def delete(self, index):  # boundary cases
        assert 0 <= index < self.count, "Index out of range"
        if self.count == 0:
            raise IndexError("List is empty")

        if index == 0:
            self.head = self.head.next
        else:
            parent = self.get_node(index - 1)  # if we want to delete the first element
            parent.next = parent.next.next     # then index - 1 would be negative
        self.count -= 1

    def insert(self, index, item):  # note the boundary cases
        if index < 0:
            index = 0
        elif index >= self.count:
            index = self.count - 1
        if index == 0:
            self.head = Node(item, self.head)
        else:
            node = self.get_node(index - 1)
            node.next = Node(item, node.next)
        self.count += 1

    def __iter__(self):
        return LinkedListIterator(self.head)

    def print(self):
        bound = 0
        print("[", end="")
        for item in self:
            if bound != self.count:
                print(item, end=", ")
                bound += 1
            else:
                print(item, end="")
        print("]")

