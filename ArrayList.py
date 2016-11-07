# unsorted array-based list


class ArrayListIterator:
    def __init__(self, array, head):
        self.array = array
        self.head = head
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.head:
            tmp = self.array[self.start]
            self.start += 1
            return tmp
        raise StopIteration


class ArrayList:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.head = -1
        self.array = [None] * size

    def append(self, item):
        if self.count + 1 > self.size:
            raise ValueError("Array full")
        else:
            self.head += 1
            self.array[self.head] = item
            self.count += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        else:
            for i in range(index, self.head + 1):
                self.array[i] = self.array[i + 1]
            self.count -= 1
            self.head -= 1

    def insert(self, item, index):
        assert self.head + 1 < self.size, "Array full"
        if index < 0:
            index = 0
        elif index > self.head:
            index = self.head
        for i in range(self.head + 1, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.count += 1
        self.head += 1

    def __len__(self):
        return self.count

    def __iter__(self):
        return ArrayListIterator(self.array, self.head)

    def __getitem__(self, index):
        assert index >= 0 or index <= self.head, "Index out of range"
        return self.array[index]

    def __contains__(self, item):
        for element in self:
            if element == item:
                return True
        return False

    def get_position(self, item):
        for i in range(0, self.head + 1):
            if self.array[i] == item:
                return i
        raise IndexError("Item is not in the array")

test = ArrayList(100)
for i in range(10):
    test.append(i)

test.delete(-8)
