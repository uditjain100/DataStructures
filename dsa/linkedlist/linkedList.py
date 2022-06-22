from queue import deque


class LinkedList:

    class Node:
        def __init__(self, v):
            self.value = v
            self.next = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, ele):
        if self.head == None:
            self.head = self.tail = LinkedList.Node(ele)
        else:
            nn = LinkedList.Node(ele)
            nn.next = self.head
            self.head = nn
        return self.head

    def addLast(self, ele):
        if self.head == None:
            self.head = self.tail = LinkedList.Node(ele)
        else:
            nn = LinkedList.Node(ele)
            self.tail.next = nn
            self.tail = nn
        return self.head

    def addAt(self, ele, idx):
        if idx == 0:
            return self.addFirst(ele)
        elif idx >= self.size:
            return self.addLast(ele)
        else:
            nn = LinkedList.Node(ele)
            prevNode = getAt(idx-1)
            nextNode = prev.next

            prevNode.next = nn
            nn.next = nextNode
        return self.head

    def getFirst(self):
        return self.head

    def getLast(self):
        return self.tail

    def getAt(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr

    def removeFirst(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.head
            self.head = self.head.next
            rn.next = None
        return self.head

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.getAt(self.size - 2)
            self.tail = rn
            rn.next = None
        return self.head

    def removeAt(self, idx):
        if idx == 0:
            return self.removeFirst()
        elif idx >= self.size:
            return self.removeLast()
        else:
            prevNode = self.getAt(idx-1)
            prevNode.next = prevNode.next.next
        return self.head

    def __str__(self):
        ans = ""
        curr = self.head
        while curr != None:
            ans += str(curr.value) + ", "
            curr = curr.next
        return ans


class DoublyLinkedList:

    class Node:
        def __init__(self, v):
            self.value = v
            self.prev = self.next = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, ele):
        if self.head == None:
            self.head = self.tail = DoublyLinkedList.Node(ele)
        else:
            nn = DoublyLinkedList.Node(ele)
            nn.next = self.head
            self.head.prev = nn
            self.head = nn
        return self.head

    def addLast(self, ele):
        if self.head == None:
            self.head = self.tail = DoublyLinkedList.Node(ele)
        else:
            nn = DoublyLinkedList.Node(ele)
            self.tail.next = nn
            nn.prev = self.tail
            self.tail = nn
        return self.head

    def addAt(self, ele, idx):
        if idx == 0:
            return self.addFirst(ele)
        elif idx >= self.size:
            return self.addLast(ele)
        else:
            nn = DoublyLinkedList.Node(ele)
            prevNode = getAt(idx-1)
            nextNode = prev.next

            prevNode.next = nn
            nn.prev = prevNode
            nn.next = nextNode
            nextNode.prev = nn
        return self.head

    def getFirst(self):
        return self.head

    def getLast(self):
        return self.tail

    def getAt(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr

    def removeFirst(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.head
            self.head = self.head.next
            self.head.prev = None
            rn.next = None
        return self.head

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.getAt(self.size - 2)
            self.tail.prev = None
            self.tail = rn
            rn.next = None
        return self.head

    def removeAt(self, idx):
        if idx == 0:
            return self.removeFirst()
        elif idx >= self.size:
            return self.removeLast()
        else:
            prevNode = self.getAt(idx-1)
            prevNode.next = prevNode.next.next
            prevNode.next.prev = prevNode
        return self.head

    def __str__(self):
        ans = ""
        curr = self.head
        while curr != None:
            ans += str(curr.value) + ", "
            curr = curr.next
        return ans


class CircularLinkedList:

    class Node:
        def __init__(self, v):
            self.value = v
            self.next = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, ele):
        if self.head == None:
            self.head = self.tail = CircularLinkedList.Node(ele)
            self.tail.next = self.head
        else:
            nn = CircularLinkedList.Node(ele)
            nn.next = self.head
            self.head = nn
        return self.head

    def addLast(self, ele):
        if self.head == None:
            self.head = self.tail = CircularLinkedList.Node(ele)
            self.tail.next = self.head
        else:
            nn = CircularLinkedList.Node(ele)
            self.tail.next = nn
            self.tail = nn
        return self.head

    def addAt(self, ele, idx):
        if idx == 0:
            return self.addFirst(ele)
        elif idx >= self.size:
            return self.addLast(ele)
        else:
            nn = CircularLinkedList.Node(ele)
            prevNode = getAt(idx-1)
            nextNode = prev.next

            prevNode.next = nn
            nn.next = nextNode
        return self.head

    def getFirst(self):
        return self.head

    def getLast(self):
        return self.tail

    def getAt(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr

    def removeFirst(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head.next = self.tail.next = None
            self.head = self.tail = None
            return None
        else:
            rn = self.head
            self.head = self.head.next
            rn.next = None
        return self.head

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head.next = self.tail.next = None
            self.head = self.tail = None
            return None
        else:
            rn = self.getAt(self.size - 2)
            self.tail = rn
            rn.next = None
        return self.head

    def removeAt(self, idx):
        if idx == 0:
            return self.removeFirst()
        elif idx >= self.size:
            return self.removeLast()
        else:
            prevNode = self.getAt(idx-1)
            prevNode.next = prevNode.next.next
        return self.head

    def __str__(self):
        ans = ""
        curr = self.head
        while curr != None:
            ans += str(curr.value) + ", "
            curr = curr.next
        return ans


class CircularDoublyLinkedList:

    class Node:
        def __init__(self, v):
            self.value = v
            self.prev = self.next = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, ele):
        if self.head == None:
            self.head = self.tail = CircularDoublyLinkedList.Node(ele)
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            nn = CircularDoublyLinkedList.Node(ele)
            nn.next = self.head
            self.head.prev = nn
            self.head = nn
        return self.head

    def addLast(self, ele):
        if self.head == None:
            self.head = self.tail = CircularDoublyLinkedList.Node(ele)
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            nn = CircularDoublyLinkedList.Node(ele)
            self.tail.next = nn
            nn.prev = self.tail
            self.tail = nn
        return self.head

    def addAt(self, ele, idx):
        if idx == 0:
            return self.addFirst(ele)
        elif idx >= self.size:
            return self.addLast(ele)
        else:
            nn = CircularDoublyLinkedList.Node(ele)
            prevNode = getAt(idx-1)
            nextNode = prev.next

            prevNode.next = nn
            nn.prev = prevNode
            nn.next = nextNode
            nextNode.prev = nn
        return self.head

    def getFirst(self):
        return self.head

    def getLast(self):
        return self.tail

    def getAt(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr

    def removeFirst(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.tail.next = None
            self.head.prev = None
            self.head = self.tail = None
            return None
        else:
            rn = self.head
            self.head = self.head.next
            self.head.prev = None
            rn.next = None
        return self.head

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.tail.next = None
            self.head.prev = None
            self.head = self.tail = None
            return None
        else:
            rn = self.getAt(self.size - 2)
            self.tail.prev = None
            self.tail = rn
            rn.next = None
        return self.head

    def removeAt(self, idx):
        if idx == 0:
            return self.removeFirst()
        elif idx >= self.size:
            return self.removeLast()
        else:
            prevNode = self.getAt(idx-1)
            prevNode.next = prevNode.next.next
            prevNode.next.prev = prevNode
        return self.head

    def __str__(self):
        ans = ""
        curr = self.head
        while curr != None:
            ans += str(curr.value) + ", "
            curr = curr.next
        return ans


class LinkedListRandom:

    class Node:
        def __init__(self, v):
            self.value = v
            self.next = None
            self.random = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, ele):
        if self.head == None:
            self.head = self.tail = LinkedListRandom.Node(ele)
        else:
            nn = LinkedListRandom.Node(ele)
            nn.next = self.head
            self.head = nn
        return self.head

    def addLast(self, ele):
        if self.head == None:
            self.head = self.tail = LinkedListRandom.Node(ele)
        else:
            nn = LinkedListRandom.Node(ele)
            self.tail.next = nn
            self.tail = nn
        return self.head

    def addAt(self, ele, idx):
        if idx == 0:
            return self.addFirst(ele)
        elif idx >= self.size:
            return self.addLast(ele)
        else:
            nn = LinkedListRandom.Node(ele)
            prevNode = getAt(idx-1)
            nextNode = prev.next

            prevNode.next = nn
            nn.next = nextNode
        return self.head

    def getFirst(self):
        return self.head

    def getLast(self):
        return self.tail

    def getAt(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr

    def removeFirst(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.head
            self.head = self.head.next
            rn.next = None
        return self.head

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.getAt(self.size - 2)
            self.tail = rn
            rn.next = None
        return self.head

    def removeAt(self, idx):
        if idx == 0:
            return self.removeFirst()
        elif idx >= self.size:
            return self.removeLast()
        else:
            prevNode = self.getAt(idx-1)
            prevNode.next = prevNode.next.next
        return self.head

    def __str__(self):
        ans = ""
        curr = self.head
        while curr != None:
            ans += str(curr.value) + ", "
            curr = curr.next
        return ans

    # ? Using O(n) of space
    def clone1(self):
        newHead = LinkedListRandom.Node(-1)
        newCurr = newHead

        map = {}
        curr = self.head
        while curr != None:
            newCurr.next = LinkedListRandom.Node(curr.value)
            map[curr] = newCurr.next
            newCurr = newCurr.next
            curr = curr.next

        curr = self.head
        newCurr = newHead.next
        while curr != None:
            newCurr.random = map[curr.random]
            newCurr = newCurr.next
            curr = curr.next
        return newHead.next

    # ? Without Using any Space
    def clone2(self):
        newHead = LinkedListRandom.Node(-1)
        newCurr = newHead

        curr = self.head
        while curr != None:
            newCurr.next = LinkedListRandom.Node(curr.value)
            newCurr = newCurr.next
            curr = curr.next

        newHead = newHead.next

        newCurr = newHead
        curr = head

        nh = LinkedListRandom.Node(-1)
        nc = nh
        while curr != None:
            nh.next = curr
            nh = nh.next
            nh.next = newCurr
            nh = nh.next
            curr = curr.next
            newCurr = newCurr.next

        nh = nh.next
        nc = nh
        while nc != None:
            nc.next.random = nc.random.next if nc.random != None else None
            nc = nc.next.next

        curr = nh
        newCurr = nh.next

        while curr != None:
            curr.next = curr.next.next
            if newCurr.next != None:
                newCurr.next = newCurr.next.next
            curr = curr.next
            newCurr = newCurr.next
        return newHead


class Lists:

    class Node:
        def __init__(self, v):
            self.value = v
            self.next = None
            self.down = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, ele):
        if self.head == None:
            self.head = self.tail = Lists.Node(ele)
        else:
            nn = Lists.Node(ele)
            nn.next = self.head
            self.head = nn
        return self.head

    def addLast(self, ele):
        if self.head == None:
            self.head = self.tail = Lists.Node(ele)
        else:
            nn = Lists.Node(ele)
            self.tail.next = nn
            self.tail = nn
        return self.head

    def addAt(self, ele, idx):
        if idx == 0:
            return self.addFirst(ele)
        elif idx >= self.size:
            return self.addLast(ele)
        else:
            nn = Lists.Node(ele)
            prevNode = getAt(idx-1)
            nextNode = prev.next

            prevNode.next = nn
            nn.next = nextNode
        return self.head

    def getFirst(self):
        return self.head

    def getLast(self):
        return self.tail

    def getAt(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr

    def removeFirst(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.head
            self.head = self.head.next
            rn.next = None
        return self.head

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.getAt(self.size - 2)
            self.tail = rn
            rn.next = None
        return self.head

    def removeAt(self, idx):
        if idx == 0:
            return self.removeFirst()
        elif idx >= self.size:
            return self.removeLast()
        else:
            prevNode = self.getAt(idx-1)
            prevNode.next = prevNode.next.next
        return self.head

    def __str__(self):
        ans = ""
        curr = self.head
        while curr != None:
            ans += str(curr.value) + ", "
            curr = curr.next
        return ans

    def mergeTwoSortedList(a, b):
        if a == None:
            return b
        if b == None:
            return a

        na = a
        nb = b

        nh = Lists.Node(-1)
        nc = nh

        while na != None and nb != None:
            if na.value < nb.value:
                nc.next = na
                na = na.next
            elif na.value > nb.value:
                nc.next = nb
                nb = nb.next
            else:
                nc.next = na
                nc = nc.next
                nc.next = nb
                na = na.next
                nb = nb.next
            nc = nc.next

        if na != None:
            nc.next = na
        if nb != None:
            nc.next = nb

        return nh.next

    # *** All linked lists are sorted
    # *** The flattened linked list should also be sorted
    def flattenSorted(self):
        self.flattenSorted(self.head)

    def flattenSorted(self, node):
        if node == None:
            return node

        node.next = self.flatten(node.next)

        a = node
        b = node.down
        node.down = None

        return self.merge(a, b)

    # *https://www.geeksforgeeks.org/flattening-a-linked-list/
    def flatten(self):
        self.flatten(self.head)

    def flatten(self, node):
        if node == None:
            return node

        node.next = self.flatten(node.next)

        next = node.next
        node.next = node.down

        temp = node.next
        while temp.next != None:
            temp = temp.next
        temp.next = next

        return node.next


class MultiLevelLists:

    class Node:
        def __init__(self, v):
            self.value = v
            self.next = None
            self.child = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, ele):
        if self.head == None:
            self.head = self.tail = MultiLevelLists.Node(ele)
        else:
            nn = MultiLevelLists.Node(ele)
            nn.next = self.head
            self.head = nn
        return self.head

    def addLast(self, ele):
        if self.head == None:
            self.head = self.tail = MultiLevelLists.Node(ele)
        else:
            nn = MultiLevelLists.Node(ele)
            self.tail.next = nn
            self.tail = nn
        return self.head

    def addAt(self, ele, idx):
        if idx == 0:
            return self.addFirst(ele)
        elif idx >= self.size:
            return self.addLast(ele)
        else:
            nn = MultiLevelLists.Node(ele)
            prevNode = getAt(idx-1)
            nextNode = prev.next

            prevNode.next = nn
            nn.next = nextNode
        return self.head

    def getFirst(self):
        return self.head

    def getLast(self):
        return self.tail

    def getAt(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr

    def removeFirst(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.head
            self.head = self.head.next
            rn.next = None
        return self.head

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            return None
        else:
            rn = self.getAt(self.size - 2)
            self.tail = rn
            rn.next = None
        return self.head

    def removeAt(self, idx):
        if idx == 0:
            return self.removeFirst()
        elif idx >= self.size:
            return self.removeLast()
        else:
            prevNode = self.getAt(idx-1)
            prevNode.next = prevNode.next.next
        return self.head

    def __str__(self):
        ans = ""
        curr = self.head
        while curr != None:
            ans += str(curr.value) + ", "
            curr = curr.next
        return ans

    # **https://www.geeksforgeeks.org/flatten-a-multi-level-linked-list-set-2-depth-wise/
    def flattenDepthWise(self):
        self.flattenDepthWise(self.head)

    def flattenDepthWise(self, node):
        if node == None:
            return node

        node.child = self.flattenDepthWise(node.child)
        node.next = self.flattenDepthWise(node.next)

        next = node.next
        node.next = node.child

        temp = node.child
        while temp.next != None:
            temp = temp.next
        temp.next = next
        return node.next

    def flattenBreadthWise(self):
        self.flattenBreadthWise(self.head)

    def flattenBreadthWise(self, node):
        if node == None:
            return node

        node.next = self.flattenBreadthWise(node.next)
        node.child = self.flattenBreadthWise(node.child)

        child = node.child
        node.child = None

        temp = node.next
        while temp.next != None:
            temp = temp.next
        temp.next = child
        return node.next

    # ***https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/
    def flatten(self, node):
        q = deque()
        q.append(node)

        nh = MultiLevelLists.Node(-1)
        nc = nh

        while len(q) != 0:
            size = len(q)
            while size > 0:
                size -= 1

                rn = q.popleft()
                nc.next = rn

                while nc != None:
                    if nc.child != None:
                        q.append(nc.child)
                    nc.child = None
                    nc = nc.next
        return nh.next
