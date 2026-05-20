class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._traverse_inorder(self.root, [])

    def _traverse_inorder(self, node, result):
        if node:
            self._traverse_inorder(node.left, result)
            result.append(node.key)
            self._traverse_inorder(node.right, result)
        return result

    def preorder(self):
        return self._traverse_preorder(self.root, [])

    def _traverse_preorder(self, node, result):
        if node:
            result.append(node.key)
            self._traverse_preorder(node.left, result)
            self._traverse_preorder(node.right, result)
        return result

    def postorder(self):
        return self._traverse_postorder(self.root, [])

    def _traverse_postorder(self, node, result):
        if node:
            self._traverse_postorder(node.left, result)
            self._traverse_postorder(node.right, result)
            result.append(node.key)
        return result

    def find_min(self):
        if self.root is None:
            return None
        return self._min_value_node(self.root).key

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.key

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

