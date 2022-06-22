import sys
import queue
import heapq


class searchTree:

    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.leftMost = 0
        self.rightMost = 0
        self.idx = 0
        self.lca = None
        self.prev = self.first = self.second = self.third = None

    def display(self):
        self.__display(self.root)

    def __display(self, node):
        if node == None:
            return

        s = "" + node.value
        if node.left != None:
            s += " -> " + node.left.value
        if node.right != None:
            s += " -> " + node.right.value

        print(s)

        self.__display(node.left)
        self.__display(node.right)

    # ? Takes O(n) time

    def constructFromInOrder(self, inOrder):
        self.root = self.__constructFromInOrder(inOrder, 0, len(inOrder))

    def __constructFromInOrder(self, inOrder, si, ei):
        if si > ei:
            return None
        if si == ei:
            return searchTree.TreeNode(inOrder[si])

        mid = (si + ei) / 2
        nn = TreeNode(inOrder[si])

        nn.left = self.__constructFromInOrder(inOrder, si, mid - 1)
        nn.right = self.__constructFromInOrder(inOrder, mid + 1, ei)

        return nn

    # ? Similarly Height can be calculated from preorder
    def constructFromPreOrder(self, preOrder):
        self.idx = 0
        self.root = self.__constructFromPreOrder(
            preOrder, -sys.maxsize, sys.maxsize)

    def __constructFromPreOrder(self, preOrder, lb, ub):
        if idx == preOrder.length or preOrder[idx] < lb or preOrder[idx] > ub:
            return None

        ele = preOrder[idx]

        nn = searchTree.TreeNode(ele)
        idx += 1
        nn.left = self.__constructFromPreOrder(preOrder, lb, ele)
        nn.right = self.__constructFromPreOrder(preOrder, ele, ub)
        return nn

    def constructFromPostOrder(self, postOrder):
        self.idx = len(postOrder)
        self.root = self.__constructFromPostOrder(
            postOrder, -sys.maxsize, sys.maxsize)

    def __constructFromPostOrder(self, lb, ub):
        if idx == -1 or postOrder[idx] < lb or postOrder[idx] > ub:
            return None

        ele = postOrder[idx]

        nn = TreeNode(ele)
        idx += 1
        nn.right = self.__constructFromPostOrder(postOrder, ele, ub)
        nn.left = self.__constructFromPostOrder(postOrder, lb, ele)
        return nn

    def constructFromLevelOrder(self, levelOrder):
        self.root = searchTree.TreeNode(levelOrder[0])

        q = queue.deque([self.root, -sys.maxsize, sys.maxsize])
        idx = 1
        while len(q) != 0:
            rp = q.popleft()

            if idx >= len(levelOrder):
                break
            if levelOrder[idx] > rp[1] and levelOrder[idx] < rp[0].value:
                nn = searchTree.TreeNode(levelOrder[idx])
                idx += 1
                rp.node.left = nn
                q.append([nn, rp[1], rp[0].value])
            if idx >= len(levelOrder):
                break
            if levelOrder[idx] > rp[0].value and levelOrder[idx] < rp[2]:
                nn = searchTree.TreeNode(levelOrder[idx])
                idx += 1
                rp.node.right = nn
                q.append([nn, rp[0].value, rp[2]])

    def recoverBST(self):
        self.prev = self.first = self.second = self.third = None

        self.traversal(self.root)

        if self.third == None:
            self.swap(self.first, self.second)
        else:
            self.swap(self.second, self.third)

    def traversal(self, node):
        if node == None:
            return

        self.traversal(node.left)
        if self.prev == None or self.prev.value > node.value:
            if self.first == None:
                self.first = self.prev
                self.second = node
            else:
                self.third = node
        self.prev = node
        self.traversal(node.right)

    def isBST(self):
        return self.__isBST(self.root, -sys.maxsize, sys.maxsize)

    def __isBST(self, node, lb, ub):
        if node == None:
            return True
        if node.value < lb or node.value > ub:
            return False

        return self.__isBST(node.left, lb, node.value) and self.__isBST(node.right, node.value, ub)

    def add(self, v):
        self.root = self.__add(self.root, v)

    def __add(self, node, v):
        if node == None:
            return avlTree.TreeNode(v)

        if v < node.value:
            node.left = self.__add(node.left, v)
        else:
            node.right = self.__add(node.right, v)

        return node

    def rempve(self, v):
        self.__remove(self, self.root, v)

    def __remove(self, node, v):
        if node == None:
            return node

        if v < node.value:
            node.letf = self.__remove(node.left, v)
        elif v > node.value:
            node.right = self.__remove(node.right, v)
        else:
            if node.left == None or node.right == None:
                return node.right if node.left == None else node.left
            maxValue = self.__max(node.left)
            node.value = maxValue
            node.left = self.__remove(node.left, maxValue)
        return node

    def find(self, target):
        return self.__find(self.root, target)

    def __find(self, node, target):
        if node == None:
            return False

        if target < node.value:
            return self.__find(node.left, target)
        elif target > node.value:
            return self.__find(node.right, target)
        else:
            return True

    def maxValue(self):
        return self.__maxValue(self.root)

    def __maxValue(self, node):
        return -sys.maxsize if node == None else max(self.__maxValue(node.right), node.value)

    def minValue(self):
        return self.__minValue(self.root)

    def __minValue(self, node):
        return sys.maxsize if node == None else min(self.__minValue(node.left), node.value)

    def swap(self, a, b):
        temp = a.value
        a.value = b.value
        b.value = temp

    def inOrder(self):
        arr = []
        self.__inOrder(self.root)
        return arr

    def __inOrder(self, node, arr):
        if node == None:
            return

        self.__inOrder(node.left, arr)
        arr.append(node.value)
        self.__inOrder(node.right, arr)

    def preOrder(self):
        arr = []
        self.__preOrder(self.root)
        return arr

    def __preOrder(self, node, arr):
        if node == None:
            return

        arr.append(node.value)
        self.__preOrder(node.left, arr)
        self.__preOrder(node.right, arr)

    def postOrder(self):
        arr = []
        self.__postOrder(self.root)
        return arr

    def __postOrder(self, node, arr):
        if node == None:
            return

        self.__postOrder(node.left, arr)
        self.__postOrder(node.right, arr)
        arr.append(node.value)

    def rangeIn(self, a, b):
        res = []
        self.__rangeIn(self.root, a, b, res)
        return res

    def __rangeIn(self, node, a, b, res):
        if node == None:
            return

        self.__rangeIn(node.left, a, b, res)
        if node.value < a and node.value > b:
            res.add(node.value)
        self.__rangeIn(node.right, a, b, res)

    def rightMostOfLeft(self, node):
        if node == None:
            return node
        while node.right != None:
            node = node.right
        return node

    def leftMostOfRight(self, node):
        if node == None:
            return node
        while node.left != None:
            node = node.left
        return node

    def predecessor(self, target):
        return self.__predecessor(self.root, target)

    def __predecessor(self, node, target):
        if node == None:
            return -sys.maxsize

        if node.value == target:
            return self.rightMostOfLeft(node)

        leftAns = self.__predecessor(node.left, target)
        if leftAns != -sys.maxsize:
            if node.value < target:
                return max(node.value, leftAns)
            return leftAns

        rightAns = self.__predecessor(node.right, target)
        if rightAns != -sys.maxsize:
            if node.value < target:
                return max(node.value, rightAns)
            return rightAns
        return -sys.maxsize

    def successor(self, target):
        return self.__successor(self.root, target)

    def __successor(self, node, target):
        if node == None:
            return sys.maxsize

        if node.value == target:
            return self.leftMostOfRight(node)

        leftAns = self.__successor(node.left, target)
        if leftAns != sys.maxsize:
            if node.value < target:
                return min(node.value, leftAns)
            return leftAns

        rightAns = self.__successor(node.right, target)
        if rightAns != sys.maxsize:
            if node.value < target:
                return min(node.value, rightAns)
            return rightAns
        return sys.maxsize

    def mergerTwoBST(self, targetNode):
        in1 = self.inOrder()
        in2 = []
        self.__inOrder(targetNode, in2)

        inOrder = merge(in1, in2)
        self.constructFromInOrder(inOrder)

    def merge(self, in1, in2):
        arr = []

        i = 0
        j = 0

        n = len(arr1)
        m = len(arr2)

        while(i < n and j < m):
            if in1[i] < in2[j]:
                arr.append(in1[i])
                i += 1
            elif in1[i] > in2[j]:
                arr.append(in2[j])
                j += 1
            else:
                arr.append(in1[i])
                i += 1
                arr.append(in2[j])
                j += 1

        while(i < n):
            arr.append(in1[i])
            i += 1
        while(j < m):
            arr.append(in2[j])
            j += 1

        return arr

    def rootToNodePath(self, target):
        res = []
        self.__rootToNodePath(self.root, target. res)
        return reversed(res)

    def __rootToNodePath(self, node, target, res):
        if node == None:
            return

        if target < node.value:
            self.__rootToNodePath(node.left, target, res)
        elif target > node.value:
            self.__rootToNodePath(node.right, target, res)

        if target == node.value or len(res) != 0:
            res.add(node.value)

    def lowestCommonAncestor(self, a, b):
        return self.__lowestCommonAncestor(self.root, a, b)

    def __lowestCommonAncestor(self, node, a, b):
        if node == None:
            return -1

        ans = -1
        if node.value < a and node.value < b:
            ans = self.__lowestCommonAncestor(node.right, a, b)
        elif node.value > a and node.value > b:
            ans = self.__lowestCommonAncestor(node.left, a, b)
        else:
            ans = node.value if (self.find(a) and self.find(b)) else -1
        return ans

    # ? Similarly for KthSmallest
    def kthLargest(self, k):
        heap = []
        self.__kthLargest(self.root, k, heap)
        return heapq.heappop(heap)

    def __kthLargest(self, node, k, heap):
        if node == None:
            return

        self.__kthLargest(node.left, k, heap)
        heapq.heappush(heap, node.value)
        if len(heap) > k:
            heapq.heappop(heap)
        self.__kthLargest(node.right, k, heap)

    # *https://www.geeksforgeeks.org/smallest-greater-element-on-right-side/

    def leastGreaterElementOnItsRight(self, arr):
        self.root = None
        for ele in arr:
            self.add(ele)
        inOrder = self.inOrder()

        arr = []
        res = [-1 for i in range(len(arr))]
        for i in range(len(arr)):
            idx = inOrder.index(arr[i])
            if idx < len(arr):
                res[i] = arr[idx + 1]
        return res
