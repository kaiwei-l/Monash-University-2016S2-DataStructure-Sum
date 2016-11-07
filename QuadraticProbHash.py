class QuadraticProb:
    def __init__(self, size=250727, base_num=27183):
        self.table = [None] * size
        self.table_size = len(self.table)
        self.b = base_num
        self.count = 0

    def hash(self, key):
        value = 0
        a = 31415
        for i in range(len(key)):
            value = (a*value + ord(key[i])) % self.table_size
            a = a * self.b % (self.table_size - 1)
        return value

    def __len__(self):
        return self.count

    def get_index(self, key):
        index = self.hash(key)
        a = 1
        b = 1
        for _ in range(self.table_size):
            if self.table[index] is None:
                return -1
            elif self.table[index][0] == key:
                return key
            else:
                index = (index + a) % self.table_size
                b += 1
                a = b**2
        return -1

    def __getitem__(self, key):
        index = self.get_index(key)
        if index != -1:
            return self.table[index][1]
        else:
            raise KeyError("Key is not in the table")

    def __setitem__(self, key, item):
        a = 1
        b = 1
        index = self.hash(key)
        for _ in range(self.table_size):
            if self.table[index] is None:
                self.table[index] = (key, item)
                self.count += 1
                return True
            elif self.table[index][0] == key:
                self.table[index] = (key, item)
                return True
            else:
                index = (index + a) % self.table_size
                b += 1
                a = b**2
        raise KeyError("Table is full")

    def delete(self, key):
        index = self.hash(key)
        a = 1
        b = 1
        for _ in range(self.table_size):
            if self.table[index] is None:
                raise KeyError("Key is not in the table")
            elif self.table[index][0] == key:
                self.table[index] = None
                break
            else:
                index = (index + a) % self.table_size
                b += 1
                a = b**2
        if b == self.table_size:
            raise KeyError("Key is not in the table")
        else:
            for _ in range(self.table_size):
                index = (index + a) % self.table_size
                b += 1
                a = b**2
                if self.table[index] is None:
                    return
                else:
                    tmp_key = self.table[index][0]
                    tmp_item = self.table[index][1]
                    self.table[index] = None
                    self[tmp_key] = tmp_item


