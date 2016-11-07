class ArrayQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def __len__(self):
        return self.count

    def reset(self):
        self.count = 0
        self.front = 0
        self.rear = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def push(self, item):
        if self.is_empty():
            self.queue[self.front] = item
        else:
            self.rear = (self.rear + 1) % self.size
            if self.rear == self.front:
                raise IndexError("Queue is full")
            self.queue[self.rear] = item
        self.count += 1

    def serve(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        tmp = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return tmp

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            index = self.front
            for _ in range(self.count):
                print(str(self.queue[index]))
                index = (index + 1) % self.size

