import sys

class Node:
    def __init__(self, data, color="R"):
        self.data = data
        self.color = color  # 'R' for Red, 'B' for Black
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color="B")
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root
        
        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        new_node.color = "R"
        self.fix_insert(new_node)
    
    def fix_insert(self, node):
        while node.parent and node.parent.color == "R":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "R":
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "R":
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self.left_rotate(node.parent.parent)
        self.root.color = "B"
    
    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def search(self, data):
        current = self.root
        while current != self.NIL and data != current.data:
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return current if current != self.NIL else None
    
    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result
