'''class Min_Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def get_min(self):
        return self.heap[0] if self.heap else None
    
    def push_heap(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, index):
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
                self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
                index = self.parent(index)
    
    def sift_down(self, i):
        while self.left_child(i) < len(self.heap):
            minimal_child = self.left_child(i)
            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] < self.heap[self.left_child(i)]:
                minimal_child = self.right_child(i)
            if self.heap[i] < self.heap[minimal_child]:
                return
            self.heap[i], self.heap[minimal_child] = self.heap[minimal_child], self.heap[i]
            i = minimal_child

    def pop_heap(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_elem = self.heap.pop()
        if self.heap:
            self.sift_down(0)
        return min_elem'''


def min_time(arr):
    min_heap = Min_Heap()
    for i in arr:
        min_heap.push_heap(i)

    total_time = 0
    
    while True:
        a = min_heap.pop_heap()
        b =  min_heap.pop_heap()
        
        if not b:
            break

        c = a + b
        total_time += c
        
        min_heap.push_heap(c)

    return total_time


n = int(input())
arr = list(map(int, input().split()))

print(min_time(arr))

