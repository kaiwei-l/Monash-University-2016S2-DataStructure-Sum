class BSTNode:
    def __init__(self, key, item, left=None, right=None):
        self.key = key
        self.val = item
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, node):
        self.node = node
        self.stack = []
        self._init_aux_(self.node)

    def _init_aux_(self, node):
        if node is not None:
            self.stack.insert(0, node)
            self._init_aux_(node.left)
            self._init_aux_(node.right)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.stack) == 0:
            raise StopIteration
        else:
            tmp = self.stack.pop()
            return tmp.val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, item):
        self.root = self.insert_aux(self.root, key, item)  # update self.root

    def insert_aux(self, node, key, item):
        if node is None:
            node = BSTNode(key, item)
        else:
            if node.key < key:
                node.right = self.insert_aux(node.right, key, item)
            elif node.key > key:
                node.left = self.insert_aux(node.left, key, item)
            else:
                raise ValueError
        return node

    def __contains__(self, key):
        return self._contains_aux(key, self.root)

    def _contains_aux(self, key, node):
        if node is None:
            raise KeyError
        else:
            if node.key == key:
                return True
            elif node.key < key:
                return self._contains_aux(key, node.right)
            else:
                return self._contains_aux(key, node.left)

    def __getitem__(self, key):
        return self._getitem_aux(key, self.root)

    def _getitem_aux(self, key, node):
        if node is None:
            raise KeyError
        else:
            if node.key == key:
                return node.val
            elif node.key < key:
                return self._getitem_aux(key, node.right)
            else:
                return self._getitem_aux(key, node.left)

    def find_min(self, node):
        if node.left is None:
            return node
        else:
            return self.find_min(node.left)

    def delete_min(self, node):
        if node.left is None:
            return node.right
        else:
            node.left = self.delete_min(node.left)
            return node

    def delete(self, key):
        self.root = self.delete_aux(key, self.root)

    def delete_aux(self, key, node):
        if node is None:
            raise ValueError
        else:
            if node.key < key:
                node.right = self.delete_aux(key, node.right)
            elif node.key > key:
                node.left = self.delete_aux(key, node.left)
            else:
                if node.right is None and node.left is None:
                    return None
                elif node.right is None:
                    return node.left
                elif node.left is None:
                    return node.right
                else:
                    tmp = self.find_min(node)
                    tmp.left = node.left
                    tmp.right = node.right
                    self.delete_min(node.right)
                    return tmp
            return node

    def print_preorder(self):
        self.print_pre_aux(self.root)

    def print_pre_aux(self, node):
        print(node.val, end=" ")
        if node.left is not None:
            self.print_pre_aux(node.left)
        if node.right is not None:
            self.print_pre_aux(node.right)

    def __iter__(self):
        return BSTIterator(self.root)


a = BinarySearchTree()
a.insert(3, "a")
a.insert(4, "c")
a.insert(2, "b")
a.insert(8, "s")
a.insert(1, "a")
