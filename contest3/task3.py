'''class Element:
    def __init__(self, value, index):
        self.value = value
        self.index = index

class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def get_max(self):
        return self.heap[0].value if self.heap else None
    
    def push_heap(self, elem):
        self.heap.append(elem)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, index):
        while index != 0 and self.heap[self.parent(index)].value < self.heap[index].value:
                self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
                index = self.parent(index)
    
    def sift_down(self, i):
        while self.left_child(i) < len(self.heap):
            largest = self.left_child(i)
            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)].value > self.heap[self.left_child(i)].value:
                largest = self.right_child(i)
            if self.heap[i].value > self.heap[largest].value:
                return
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def pop_heap(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_elem = self.heap.pop()
        if self.heap:
            self.sift_down(0)
        return max_elem
    
    def remote_outdated(self, min_index):
        while self.heap[0].index < min_index:
            self.pop_heap()'''


def find_maxes(n, arr, k):
    moving_window = Heap()
    ans = []
    for i in range(k): 
        moving_window.push_heap(Element(arr[i], i))
    ans.append(str(moving_window.get_max()))

    for i in range(k, n):
        moving_window.remote_outdated(i - k + 1)
        moving_window.push_heap(Element(arr[i], i))
        ans.append(str(moving_window.get_max()))
    
    return ' '.join(ans)
    

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(find_maxes(n, arr, k))