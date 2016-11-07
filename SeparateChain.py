from LinkedList import LinkedList


class SeparateChain:
    def __init__(self, size=250727, base_num=27183):
        self.table = [None] * size
        self.table_size = len(self.table)
        self.b = base_num
        self.count = 0

    def __len__(self):
        return self.count

    def hash(self, key):
        a = 31415
        value = 0
        for i in range(len(key)):
            value = (a * value + ord(key[i])) % self.table_size
            a = a * self.b % (self.table_size - 1)
        return value

    def __getitem__(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            raise KeyError("Key is not in the table")
        else:
            item = self.table[index][key]
            return item

    def __setitem__(self, key, item):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = LinkedList()
            self.table[index].add((key, item))
        else:
            self.table[index].add((key, item))

    def __contains__(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return False
        elif key in self.table[index]:
            return True
        else:
            return False

