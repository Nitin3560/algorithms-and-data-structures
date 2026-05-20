class Stack:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size
        self.top = -1

    def PUSH(self, value):
        if self.top >= self.size - 1:
            raise OverflowError("Stack overflow")
        self.top += 1
        self.array[self.top] = value

    def POP(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        value = self.array[self.top]
        self.top -= 1
        return value

    def is_empty(self):
        return self.top == -1


class Queue:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def ENQUEUE(self, value):
        if self.count == self.size:
            raise OverflowError("Queue overflow")
        self.array[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def DEQUEUE(self):
        if self.count == 0:
            raise IndexError("Queue underflow")
        value = self.array[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return value

    def is_empty(self):
        return self.count == 0


class SinglyLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, size):
        self.size = size
        self.array = [self.Node(None) for _ in range(size)]
        self.head = None
        self.free_list = list(range(size)) 

    def INSERT(self, value):
        if not self.free_list:
            raise OverflowError("List is full")
        new_index = self.free_list.pop(0)
        self.array[new_index].value = value
        self.array[new_index].next = self.head
        self.head = new_index

    def DELETE(self, value):
        prev_index = None
        current_index = self.head

        while current_index is not None:
            if self.array[current_index].value == value:
                if prev_index is None:
                    self.head = self.array[current_index].next
                else:
                    self.array[prev_index].next = self.array[current_index].next

                self.free_list.insert(0, current_index)
                return

            prev_index = current_index
            current_index = self.array[current_index].next

        raise ValueError("Value not found")

    def SEARCH(self, value):
        current_index = self.head
        while current_index is not None:
            if self.array[current_index].value == value:
                return current_index
            current_index = self.array[current_index].next
        return None
