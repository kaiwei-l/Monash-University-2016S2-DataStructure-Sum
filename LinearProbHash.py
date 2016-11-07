# Linear probing hash table
class LinearProb:
    def __init__(self, table_size=250727, base_num=27183):
        self.table = [None] * table_size
        self.table_size = len(self.table)
        self.b = base_num
        self.count = 0

    def __len__(self):
        return self.count

    def hash(self, key):
        a = 31415
        value = 0
        for i in range(len(key)):
            value = (a*value + ord(key[i])) % self.table_size
            a = a * self.b % (self.table_size - 1)
        return value

    def get_index(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return -1
        elif self.table[index][0] == key:
            return index
        else:
            for i in range(self.table_size):
                index = (index + 1) % self.table_size
                if self.table[index][0] == key:
                    return index
            return -1

    def __setitem__(self, key, item):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = (key, item)
            self.count += 1
            return True
        elif self.table[index][0] == key:
            self.table[index] = (key, item)
            self.count += 1
            return True
        else:
            for i in range(self.table_size):
                index = (index + 1) % self.table_size
                if self.table[index] is None:
                    self.table[index] = (key, item)
                    self.count += 1
                    return True
            raise ValueError("Table is full")

    def __getitem__(self, key):
        index = self.get_index(key)
        if index != -1:
            return self.table[index][1]
        else:
            raise KeyError("Item is not in the table")

    def delete(self, key):
        index = self.get_index(key)
        if index != -1:
            self.table[index] = None
            self.count -= 1
            for i in range(self.table_size):
                index = (index + 1) % self.table_size
                if self.table[index] is None:
                    return
                else:
                    tmp_key = self.table[index][0]
                    tmp_item = self.table[index][1]
                    self.table[index] = None
                    self[tmp_key] = tmp_item
        else:
            raise KeyError("Key is not in the table")
