# This is a Max heap
class Heap:
    def __init__(self):
        self.array = [None]
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def largest_child(self, k):
        # 2*k == self.count means that no right child
        if 2*k == self.count or self.array[2*k] > self.array[2*k + 1]:
            return 2*k
        else:
            return 2*k + 1

    def sink(self, k):
        # it must have left child. Left child has two situation: less than or equal to
        while 2 * k <= self.count:  # if 2k is greater than count, then it exceeds the bound
            child = self.largest_child(k)
            if self.array[k] >= self.array[child]:
                break
            else:
                self.swap(k, child)
                k = child

    def rise(self, k):  # no matter how, child // 2 is always the parent
        while k//2 != 0 and self.array[k] > self.array[k//2]:
            self.swap(k, k//2)
            k //= 2

    def add(self, item):
        # when we get max, there will be empty positions in the array
        # note that self.count is the length of the self.array
        if self.count + 1 < len(self.array):
            self.array[self.count+1] = item
        else:
            self.array.append(item)
        self.count += 1
        self.rise(self.count)

    def get_max(self):
        self.swap(1, self.count)
        max_item = self.array.pop()
        self.count -= 1
        self.sink(1)
        return max_item


def heap_sort(lst):
    a_heap = Heap()
    for item in lst:
        a_heap.add(item)
    tmp = []
    while not a_heap.is_empty():
        tmp.append(a_heap.get_max())
    return tmp

