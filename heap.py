class heap:
    def __init__(self):
        self.heap = []
        self.size = 0
        
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.siftUp(self.size - 1)
        
    def siftUp(self, index):
        if index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] < self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                self.siftUp(parent)
    
    def siftDown(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.siftDown(largest)
        
    def extractMax(self):
        if self.size > 0:
            max = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.heap.pop()
            self.size -= 1
            self.siftDown(0)
            return max
        else:
            return None
        
    def heapSort(self):
        for i in range(self.size - 1, -1, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.siftDown(0)
            
    def printHeap(self):
        print(self.heap)
        
    def heapify(self, arr):
        self.heap = arr
        self.size = len(arr)
        for i in range(self.size - 1, -1, -1):
            self.siftDown(i)
            

heap = heap()
heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(40)
heap.insert(50)
heap.insert(60)

heap.printHeap()
print("=====================================")
heap.extractMax()
print("=====================================")
heap.printHeap()
print("=====================================")
heap.heapSort()
heap.printHeap()
print("=====================================")

heap.heapify([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("=====================================")
heap.printHeap()