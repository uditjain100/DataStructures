from queue import deque


def reverse(q):
    if q.isEmpty():
        return

    re = q.dequeue()
    reverse(q)
    q.enqueue(re)


def reverseK(q, k):
    if q.isEmpty() or k == 0:
        return

    re = q.dequeue()
    reverseK(q, k-1)
    q.enqueue(re)

#  ***** Interleave the first half of the queue with second half
#  ***** Input: 11 12 13 14 15 16 17 18 19 20
#  ***** Output: 11 16 12 17 13 18 14 19 15 20


def interleave(q):
    interleave(q, stack, q.size()/2)


def interleave(q, stack, k):
    if q.isEmpty():
        return

    re = queue.dequeue()
    if k > 0:
        stack.push(re)
        interleave(q, stack, k - 1)
    else:
        interleave(q, stack, k - 1)

    if k <= 0:
        queue.enqueue(re)
        queue.enqueue(stack.pop())


def firstNonRepeatingCharacterFromStream(s):
    ans = ""
    q = deque()
    dict = {}

    for ch in s:
        if ch not in dict.keys():
            dict[ch] = 0
        dict[ch] += 1
        q.append(ch)

        while len(q) != 0:
            rc = q.popleft()
            if dict[rc] == 1:
                q.appendleft(rc)
                ans += rc
                break

        if len(q) == 0:
            ans += "#"
    return ans


def slidingWindowMax(arr, k):
    ans = []
    q = deque()

    n = len(arr)
    for i in range(0, k):
        while len(q) != 0 and arr[q[-1]] < arr[i]:
            q.pop()
        q.append(i)

    ans.append(arr[q[0]])

    for i in range(k, n):
        if q[0] == i-k:
            q.pop()
        while len(q) != 0 and arr[q[-1]] < arr[i]:
            q.pop()
        q.append(i)
        ans.append(q[0])

    return ans


def slidingWindowMin(arr, k):
    ans = []
    q = deque()

    n = len(arr)
    for i in range(0, k):
        while len(q) != 0 and arr[q[-1]] > arr[i]:
            q.pop()
        q.append(i)

    ans.append(arr[q[0]])

    for i in range(k, n):
        if q[0] == i-k:
            q.pop()
        while len(q) != 0 and arr[q[-1]] > arr[i]:
            q.pop()
        q.append(i)
        ans.append(q[0])

    return ans


def slidingWindowMin(arr, k):
    ans = []
    q = deque()

    n = len(arr)
    for i in range(0, k):
        if arr[i] < 0:
            q.append(i)

    ans.append(0 if len(q) == 0 else arr[q[0]])

    for i in range(k, n):
        if q[0] == i-k:
            q.pop()
        if arr[i] < 0:
            q.append(i)
        ans.append(0 if len(q) == 0 else arr[q[0]])

    return ans


class LRUCache1:

    def __init__(self, cap):
        self.q = deque()
        self.dict = {}
        self.capacity = cap

    def put(self, key, value):
        if key in self.dict.keys():
            self.q.remove(key)
        else:
            if len(self.q) == self.capacity:
                del self.dict[self.q.popleft()]
        self.dict[key] = [key, value]
        self.q.append(key)

    def get(self, key):
        if key not in self.dict.keys():
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.dict[self.q[-1]][1]


class LRUCache2:

    class Node:
        def __init__(self, key, value):
            self.prev = self.next = None
            self.key = key
            self.value = value

    def __init__(self, cap):
        self.head = self.tail = None
        self.map = {}
        self.capacity = cap

    def add(self, nn):
        if self.head == None:
            self.head = self.tail = nn
        else:
            self.tail.next = nn
            nn.prev = self.tail
            self.tail = nn

    def remove(self, node):

        if node.prev == None and node.next == None:
            self.head = self.tail = node = None
        elif node.prev == None:  # head
            newHead = node.next
            node.next = None
            newHead.prev = None
            self.head = newHead
        elif node.next == None:  # tail
            newTail = node.prev
            node.prev = None
            newTail.next = None
            self.tail = newTail
        else:
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p
            node.prev = node.next = None

    def put(self, key, value):
        nn = None
        if key in self.map.keys():
            nn = self.map[key]
            self.remove(nn)
            nn.value = value
        else:
            if self.capacity == len(self.map):
                del self.map[self.head.key]
                self.remove(self.head)
            nn = LRUCache.Node(key, value)
        self.add(nn)
        self.map[key] = nn

    def get(self, key):
        if key not in self.map.keys():
            return -1
        self.remove(self.map[key])
        self.add(self.map[key])
        return self.map[key].value
