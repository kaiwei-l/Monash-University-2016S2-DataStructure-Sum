class ArrayStack:
    def __init__(self):
        self.stack = [None] * 100
        self.size = 100
        self.count = 0
        self.top = -1

    def __len__(self):
        return self.count

    def reset(self):
        self.count = 0
        self.top = -1

    def resize(self):
        new_len = self.size * 100
        tmp = [None] * new_len
        for i in range(len(self.stack)):
            tmp[i] = self.stack[i]
        self.stack = tmp
        self.size = new_len

    def is_full(self):
        return self.count == self.size

    def push(self, item):
        if self.is_full():
            self.resize()
        self.top += 1
        self.stack[self.top] = item
        self.count += 1

    def pop(self):
        tmp = self.stack[self.top]
        self.count -= 1
        self.top -= 1
        return tmp

    def print_stack(self):
        for i in range(self.top + 1):
            print(self.stack[i])
