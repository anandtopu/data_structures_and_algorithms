class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def get_heap(self):
        return self.heap


def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    elements = list(map(int, input[ptr:ptr + N]))
    ptr += N

    heap = MinHeap()
    for num in elements:
        heap.insert(num)
        print(' '.join(map(str, heap.get_heap())))


if __name__ == "__main__":
    main()