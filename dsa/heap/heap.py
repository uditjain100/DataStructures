class heap:

    def __init__(self, is_Min: True):
        self.isMin = is_Min
        self.arr = []

    def size(self):
        return len(self.arr)

    def isEmpty(self):
        return len(self.arr)

    def constructHeap(self, arr):
        self.arr = arr
        n = len(self.arr)
        for i in range(n / 2, -1, -1):
            downHeapify(i)

    def downHeapify(self, idx):
        if idx < 0 or idx >= n:
            return

        lci = 2*idx + 1
        rci = 2*idx + 2

        ni = idx
        if self.compare(ni, lci) < 0:
            ni = lci
        if self.compare(ni, rci) < 0:
            ni = rci

        if ni != idx:
            self.swap(ni, idx)
            self.downHeapify(ni)

    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def compare(self, idx1, idx2):
        if self.isMin:
            return self.arr[idx2] - self.arr[idx1]
        else:
            return self.arr[idx1] - self.arr[idx2]

    def remove(self):
        self.swap(0, self.size() - 1)
        re = self.arr.pop()
        self.downHeapify(0)
        return re

    def remove(self, ele):
        i = 0
        for idx, element in enumerate(self.arr):
            if element == ele:
                i = idx
                break

        self.swap(i, self.size() - 1)
        re = self.arr.pop()
        self.downHeapify(i)
        return re

    def upHeapify(self, idx):
        pi = (idx-1)/2
        ni = idx

        if self.compare(ni, pi) < 0:
            ni = pi

        if ni != idx:
            self.swap(ni, idx)
            self.upHeapify(ni)

    def add(self, ele):
        self.arr.append(ele)
        self.upHeapify(self.size() - 1)

    def peek(self):
        return self.arr[0]

    def getOppositePeek(self):
        if self.isMin:
            return max(self.arr)
        else:
            return min(self.arr)

    def merge2Heaps(self, h1, h2):
        for ele in h1:
            self.arr.append(ele)
        for ele in h2:
            self.arr.append(ele)
        for i in range(len(self.arr) / 2, -1, -1):
            self.upHeapify(i)


class heapWithMedian:

    def __init__(self, is_Min):
        self.h = heap(is_Min)
        self.minHeap = heap(True)
        self.maxHeap = heap(False)
        self.size = 0

    def isEmpty(self):
        return self.h.isEmpty()

    def __sizeOfMinHeap(self):  # private methods => declared with double underscore
        return self.minHeap.size()

    def __sizeOfMaxHeap(self):
        return self.maxHeap.size()

    def add(self, ele):
        self.h.add(ele)
        if self.maxHeap.isEmpty():
            self.maxHeap.add(ele)
        elif self.minHeap.isEmpty() or self.maxHeap.size() == self.minHeap.size():
            if self.maxHeap.peek() < ele:
                self.maxHeap.add(ele)
                self.minHeap.add(self.maxHeap.remove())
            else:
                self.minHeap.add(ele)
        else:
            if self.maxHeap.peek() < ele:
                self.maxHeap.add(ele)
                self.minHeap.add(self.maxHeap.remove())
                self.minHeap.add(self.maxHeap.remove())
            else:
                self.minHeap.add(ele)

    def getMedian(self):
        if self.maxHeap.isEmpty():
            return -1

        if self.minHeap.size() == self.maxHeap.size():
            return (self.minHeap.peek() + self.maxHeap.peek()) / 2
        return self.maxHeap.peek()

    def remove(self):
        re = self.h.remove()

        if re <= self.maxHeap.peek():
            self.maxHeap.remove(re)
            if self.maxHeap.size() < self.minHeap.size():
                self.maxHeap.add(self.minHeap.remove())
        else:
            self.minHeap.remove(re)
            if self.maxHeap.size() - 1 < self.minHeap.size():
                self.minHeap.add(self.maxHeap.remove())

    def peek(self):
        return self.h.peek()
