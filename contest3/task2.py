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
        return min_elem
    
    def __len__(self):
        return len(self.heap)'''



def minimal_dead_ends(arr, n):
    min_heap = Min_Heap()
    max_counts = 0

    for time in arr:
        while min_heap and min_heap.get_min() < time[0]:
            min_heap.pop_heap()

        min_heap.push_heap(time[1])

        max_counts = max(max_counts, len(min_heap))

    return max_counts


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

print(minimal_dead_ends(arr, n))