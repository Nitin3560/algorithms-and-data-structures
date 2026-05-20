import math

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity
        self.load_factor = 0.75
        self.shrink_factor = 0.25
        self.A = (math.sqrt(5) - 1) / 2  

    def hash(self, key):
        fractional_part = (key * self.A) - math.floor(key * self.A)
        primary_hash = math.floor(self.capacity * fractional_part)
        return primary_hash % self.capacity  

    def resize(self, new_capacity):
        old_table = self.table
        old_capacity = self.capacity
        self.table = [None] * new_capacity
        self.capacity = new_capacity
        self.size = 0

        for i in range(old_capacity):
            current = old_table[i]
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        index = self.hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self.resize(self.capacity * 2)

    def remove(self, key):
        index = self.hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                del current
                self.size -= 1

                if self.capacity > 8 and self.size / self.capacity < self.shrink_factor:
                    self.resize(self.capacity // 2)
                return
            prev = current
            current = current.next

    def find(self, key):
        index = self.hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError("Key not found")

    def display(self):
        for i in range(self.capacity):
            print(f"Bucket {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"({current.key}, {current.value}) ", end="")
                current = current.next
            print()

