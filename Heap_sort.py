class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.heap_size = len(array)
        self.build_min_heap()

    def left(self, i):
        return 2 * i+1

    def right(self, i):
        return 2 * i+2

    def min_heapify(self, i):
        l=self.left(i)  
        r=self.right(i) 

        if l<self.heap_size and self.heap[l] < self.heap[i]:
            smallest=l
        else:
            smallest=i
            
        if r < self.heap_size and self.heap[r] < self.heap[smallest]:
            smallest=r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def build_min_heap(self):
        for i in range((self.heap_size // 2) - 1, -1, -1):
            self.min_heapify(i)

    def extract_min(self):
        if self.heap_size < 1:
            raise Exception("Heap underflow")
        min_element = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.heap.pop()  
        self.min_heapify(0)  
        return min_element

    def insert(self, key):
        self.heap.append(float('inf'))  
        self.heap_size += 1
        self.decrease_key(self.heap_size - 1, key)

    def decrease_key(self, i, key):
        if key > self.heap[i]:
            raise ValueError("New key is larger than the current key")
        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def parent(self, i):
        return (i-1) // 2

    def __str__(self):
        return str(self.heap)


# Example Usage
if __name__ == "__main__":
    # Input array to be turned into a MinHeap
    array = [9,4,7,1,-2,6,5]
    print("Input Array:", array)

    # Create MinHeap instance
    min_heap = MinHeap(array)
    print("MinHeap after building:", min_heap)

    # Extract the minimum element
    min_element = min_heap.extract_min()
    print("Extracted Minimum:", min_element)
    print("MinHeap after extraction:", min_heap)

    # Insert a new key
    min_heap.insert(0)
    print("MinHeap after inserting 0:", min_heap)

    # Insert another key
    min_heap.insert(-5)
    print("MinHeap after inserting -5:", min_heap)
