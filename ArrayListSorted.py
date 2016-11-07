# Sorted List


class ArrayListSortedIterator:
    def __init__(self, array, length):
        self.array = array
        self.length = length
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.length:
            tmp = self.array[self.start]
            self.start += 1
            return tmp
        raise StopIteration


class ArrayListSorted:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.count = 0  # next empty position

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def add(self, item):
        assert not self.is_full(), "Array full"
        for i in range(self.count):
            if self.array[i] > item:
                for j in range(self.count, i, -1):
                    self.array[j] = self.array[j - 1]
                self.array[i] = item
                self.count += 1
                return True
        self.array[self.count] = item
        self.count += 1
        return True

    def delete(self, index):
        assert 0 <= index < self.count, "Index out of range"
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.count -= 1
        return True

    def __contains__(self, item):
        for i in range(self.count):
            if self.array[i] == item:
                return i
        return -1

    def get_position(self, item):
        index = self.__contains__(item)
        return index

    def __len__(self):
        return self.count

    def __iter__(self):
        return ArrayListSortedIterator(self.array, self.count)
