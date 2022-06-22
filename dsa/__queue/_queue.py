from linkedlist import linkedList
from stack import stack


class Queue:

    def __init__(self, size):
        self.arr = [-1 for x in range(0, size)]
        self.front = 0
        self.rare = 0
        self.size = size

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.front + 1 == self.rare

    def enqueue(self, ele):
        if self.isFull():
            return
        self.front = (self.front + 1) % self.size
        self.arr[self.front] = ele

    def dequeue(self):
        if self.isEmpty():
            return
        rn = self.arr[self.rare]
        self.arr[self.rare] = -1
        self.rare = (self.rare + 1) % self.size
        return rn

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]


class QueueLinkedList:

    def __init__(self):
        self.arr = linkedList.LinkedList()

    def isEmpty(self):
        return self.arr.isEmpty()

    def size(self):
        return self.arr.size

    def enqueue(self, ele):
        self.arr.addLast(ele)

    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.arr.removeFirst()

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr.getFirst()


class QueueStack:

    def __init__(self):
        self.stack = stack.Stack()

    def isEmpty(self):
        return self.stack.isEmpty()

    def enqueue(self, ele):
        self.stack.push(ele)

    def dequeue(self):
        if self.isEmpty():
            return
        helper = stack.Stack()
        while self.stack.isEmpty() == False:
            helper.push(self.stack.pop())
        rn = helper.pop()
        while helper.isEmpty() == False:
            self.stack.push(helper.pop())
        return rn

    def getFront(self):
        if self.isEmpty():
            return -1
        helper = stack.Stack()
        while self.stack.isEmpty() == False:
            helper.push(self.stack.pop())
        rn = helper.pop()
        self.stack.push(rn)
        while helper.isEmpty() == False:
            self.stack.push(helper.pop())
        return rn
