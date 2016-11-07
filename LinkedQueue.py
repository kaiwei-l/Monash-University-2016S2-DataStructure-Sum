from Node import Node


class LinkedQueue:
    def __init__(self):
        self.count = 0
        self.front = None
        self.rear = None

    def __len__(self):
        return self.count

    def reset(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.rear is None and self.front is None

    def push(self, item):
        if self.is_empty():
            self.front = Node(item)
            self.rear = self.front
        else:
            self.rear.next = Node(item)
            self.rear = self.rear.next

            self.count += 1

    def serve(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            tmp = self.front
            if self.front.next is None:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            self.count -= 1
            return tmp.val

test = LinkedQueue()
test.push(0)
for i in range(5):
    test.push(i)

