from Node import Node


class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def __len__(self):
        return self.count

    def reset(self):
        self.count = 0
        self.top = None

    def push(self, item):
        if self.top is None:
            self.top = Node(item)
            self.count += 1
        else:
            self.top = Node(item, self.top)
            self.count += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        else:
            tmp = self.top
            self.top = self.top.next
            self.count -= 1
            return tmp.val

