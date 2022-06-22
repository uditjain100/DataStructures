from __queue._queue import *
from linkedlist import linkedList
from queue import *
import sys
sys.path.insert(0, 'D:\Python\simp\dsa\__queue')


class Stack:

    def __init__(self):
        self.arr = []
        self.tos = -1

    def isEmpty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

    def push(self, ele):
        self.arr.append(ele)
        self.tos += 1

    def pop(self):
        if self.isEmpty():
            return -1
        self.tos -= 1
        return self.arr.pop(self.tos + 1)

    def peek(self):
        if self.isEmpty():
            return -1
        return self.arr.pop(self.tos)


class StackLinkedList:

    def __init__(self):
        self.arr = linkedList.LinkedList()

    def isEmpty(self):
        return self.arr.isEmpty()

    def size(self):
        return self.arr.size

    def push(self, ele):
        self.arr.addLast(ele)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.arr.removeLast().value

    def peek(self):
        if self.isEmpty():
            return -1
        return self.arr.getLast().value

    def reverse(self):
        return self.arr.reverse()


class StackQueue:

    def __init__(self, size):
        self.queue = _queue.Queue(size)

    def isEmpty(self):
        return self.queue.isEmpty()

    def isFull(self):
        return self.queue.isFull()

    def size(self):
        return self.queue.size

    def push(self, ele):
        if self.isFull():
            return
        helper = _queue.Queue(self.size())
        while self.queue.isEmpty() == False:
            helper.enqueue(self.queue.dequeue())
        helper.enqueue(ele)
        while helper.isEmpty() == False:
            self.queue.enqueue(helper.dequeue())

    def pop(self):
        if self.isEmpty():
            return -1
        return self.queue.dequeue()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.queue.getFront()


class StackPriorityQueue:

    def __init__(self):
        self.pq = PriorityQueue()

    def isEmpty(self):
        return self.pq.empty()

    def isFull(self):
        return self.pq.full()

    def size(self):
        return self.pq.qsize()

    def push(self, ele):
        if self.isFull():
            return
        helper = PriorityQueue()
        while self.pq.empty() == False:
            helper.put(self.pq.get())
        helper.put(ele)
        while helper.empty() == False:
            self.pq.put(helper.get())

    def pop(self):
        if self.isEmpty():
            return -1
        return self.pq.get()

    def peek(self):
        if self.isEmpty():
            return -1
        rn = self.pq.get()
        self.pq.put(rn)
        return rn


class TwoStacks:

    def __init__(self, size):
        self.arr = [-1 for x in range(0, size)]
        self.tos1 = -1
        self.tos2 = size

    def isEmpty1(self):
        return self.tos1 == -1

    def isEmpty2(self):
        return self.tos2 == len(self.arr)

    def isFull(self):
        return self.tos1 + 1 == self.tos2

    def push1(self, ele):
        if self.isFull():
            return
        self.tos1 += 1
        self.arr[self.tos1] = ele

    def push2(self, ele):
        if self.isFull():
            return
        self.tos2 -= 1
        self.arr[self.tos2] = ele

    def pop1(self):
        if self.isEmpty1():
            return -1

        rn = self.arr[self.tos1]
        self.arr[self.tos1] = -1
        self.tos1 -= 1
        return rn

    def pop2(self):
        if self.isEmpty2():
            return -1

        rn = self.arr[self.tos2]
        self.arr[self.tos2] = -1
        self.tos2 += 1
        return rn

    def peek1(self):
        if self.isEmpty1():
            return -1
        return self.arr[self.tos1]

    def peek2(self):
        if self.isEmpty2():
            return -1
        return self.arr[self.tos2]

# ? Important


class kStacks:

    def __init__(self, k,  size):
        self.freeIdx = 0
        self.arr = [0 for x in range(0, size)]
        self.tos = [-1 for x in range(0, k)]
        self.next = [x+1 for x in range(0, size - 1)]
        self.next.append(-1)

    def isEmpty(self, k):
        return self.tos[k - 1] == -1

    def isFull(self):
        return self.freeIdx == -1

    def push(self, k, ele):
        if self.isFull():
            return

        idx = self.freeIdx
        self.freeIdx = self.next[idx]
        self.arr[idx] = ele
        self.next[idx] = self.top[k - 1]
        self.tos[k - 1] = idx

    def pop(self, k):
        if self.isEmpty(k):
            return -1

        idx = self.tos[k - 1]
        rn = self.arr[idx]
        self.arr[idx] = 0
        self.tos[k - 1] = self.next[idx]
        self.next[idx] = self.freeIdx
        self.freeIdx = idx
        return rn

    def peek(self, k):
        if self.isEmpty(k):
            return -1
        return self.arr[self.tos[k-1]]


class StackMiddle:

    def __init__(self):
        self.arr = linkedList.DoublyLinkedList()
        self.middle = None

    def isEmpty(self):
        return self.arr.isEmpty()

    def size(self):
        return self.arr.size

    def push(self, ele):
        self.arr.addLast(ele)

        if self.size() == 1:
            self.middle = self.arr.head
        elif (self.size() & 1) != 0:
            self.middle = self.middle.next

    def pop(self):
        if self.isEmpty():
            return -1
        rn = self.arr.removeLast().value

        if (self.size() & 1) == 0:
            self.middle = self.middle.prev
        return rn

    def peek(self):
        if self.isEmpty():
            return -1
        return self.arr.getLast()

    def middle(self):
        return self.middle.value


# ***** Using Extra Stack can be Done
# ***** By storing min upto that instant
class StackMinimum:

    def __init__(self):
        self.arr = []
        self.tos = -1
        self.min = -1

    def isEmpty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

    def push(self, ele):
        self.tos += 1
        if self.isEmpty():
            self.arr[self.tos] = ele
            self.min = ele
        else:
            if ele < min:
                self.arr[self.tos] = 2 * ele - min  # **** y = 2x-min
                self.min = ele
            else:
                self.arr[self.tos] = ele

    def pop(self):
        if self.isEmpty():
            return -1
        rn = self.arr[self.tos]
        self.arr[self.tos] = -1
        self.tos -= 1
        if rn < self.min:
            rn = self.min
            self.min = 2 * min - rn  # ****** x = 2min-y
        return rn

    def peek(self):
        if self.isEmpty():
            return -1
        rn = self.arr[self.tos]
        if rn < self.min:
            rn = self.min
        return rn

    def getMin(self):
        if self.isEmpty():
            return -1
        return self.min
