import heapq
import sys
import queue


class binaryTree:

    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.leftMost = 0
        self.rightMost = 0
        self.lca = None
        self.distance = -1
        self.idx = 0
        self.DLLPrev = None
        self.DLLHead = None
        self.map = {}
        self.isDuplicateExist = False

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

    def constructFromPreAndIn(preOrder, inOrder):
        return __constructFromPreAndIn(0, len(preOrder) - 1, 0, len(inOrder) - 1, preOrder, inOrder)

    def __constructFromPreAndIn(self, sp, ep, si, ei, preOrder, inOrder):
        if sp > ep or si > ei:
            return None

        idx = si
        while inOrder[idx] != preOrder[sp]:
            idx += 1

        numberOfElements = idx - si

        nn = binaryTree.TreeNode(preOrder[sp])
        nn.left = self.__constructFromPreAndIn(
            sp + 1, sp + numberOfElements, si, idx - 1, preOrder, inOrder)
        nn.right = self.__constructFromPreAndIn(
            sp + numberOfElements + 1, ep, idx + 1, ei, preOrder, inOrder)
        return nn

    def constructFromPostAndIn(postOrder, inOrder):
        return __constructFromPostAndIn(0, len(postOrder) - 1, 0, len(inOrder) - 1, postOrder, inOrder)

    def __constructFromPostAndIn(self, sp, ep, si, ei, postOrder, inOrder):
        if sp > ep or si > ei:
            return None

        idx = si
        while inOrder[idx] != postOrder[sp]:
            idx += 1

        numberOfElements = idx - si

        nn = binaryTree.TreeNode(postOrder[ep])
        nn.left = self.__constructFromPostAndIn(
            sp + 1, sp + numberOfElements - 1, si, idx - 1, postOrder, inOrder)
        nn.right = self.__constructFromPostAndIn(
            sp + numberOfElements, ep, idx + 1, ei, postOrder, inOrder)
        return nn

    def constructFromPostAndPre(postOrder, preOrder):
        return __constructFromPostAndPre(0, len(postOrder) - 1, 0, len(preOrder) - 1, postOrder, preOrder)

    def __constructFromPostAndPre(self, spr, spo, epo, epr, postOrder, preOrder):
        if spo > epo or spr > epr:
            return None
        if spo == epo or spr == epr:
            return binaryTree.TreeNode(postOrder[spo])

        idx = spo
        while preOrder[spr] != postOrder[idx]:
            idx += 1

        numberOfElements = idx - spo + 1

        nn = binaryTree.TreeNode(postOrder[epo])
        nn.left = self.__constructFromPostAndPre(
            spr + 1, spr + numberOfElements, spo, idx, postOrder, preOrder)
        nn.right = self.__constructFromPostAndPre(
            spr + numberOfElements + 1, epr, idx + 1, epo - 1, postOrder, preOrder)
        return nn

    def constructFromParent(self, arr):
        n = len(arr)

        nodes = [binaryTree.TreeNode(i) for i in range(0, n)]
        for i in range(0, n):
            if arr[i] == -1:
                self.root = nodes[i]
            elif nodes[arr[i]].left == None:
                nodes[arr[i]].left = arr[i]
            else:
                nodes[arr[i]].right = arr[i]

    def constructFromAncestorMatrix(self, mat):
        n = len(mat)

        heap = []
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if mat[i][j] == 1:
                    count += 1
            heap.append([count, i])
        heapq.heapify(heap, key=lambda x: x[0])

        parent = []
        nodes = [binaryTree.TreeNode(i) for i in range(0, n)]

        while len(heap) != 0:
            rp = heapq.heappop(heap)

            count = rp[0]
            idx = rp[1]

            if count == 0:
                self.root = nodes[idx]
                continue

            for j in range(0, n):
                if idx != j and mat[idx][j] == 1 and parent[j] == None:
                    parent[j] = binaryTree.TreeNode(idx)
                    if parent[j].left == None:
                        parent[j].left = nodes[j]
                    else:
                        parent[j].right = nodes[j]

    def constructFromBrackets(self, s):
        stack = []
        num = ""
        for ch in s:
            if ch != '(' or ch != ')':
                num += ch
            else:
                if len(num) != 0:
                    stack.append(binaryTree.TreeNode(int(num)))
                num = ""

                if ch == ')':
                    node = stack.pop()
                    if stack[-1].left == None:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
        self.root = stack.pop()

    def size(self):
        return self.__size(self.root)

    def __size(self, node):
        return 0 if node == None else 1 + self.__size(node.left) + self.__size(node.right)

    def find(self, target):
        return self.__find(self.root, target)

    def __find(self, node, target):
        return True if node == None or node.value == target else self.__find(node.left, target) or self.__find(node.right, target)

    def search(self, target):
        return self.__search(self.root, target)

    def __search(self, node, target):
        if node == None or node.value == target:
            return node

        left = self.__search(node.left, target)
        right = self.__search(node.right, target)

        return left if left != None else right

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        return -1 if node == None else 1 + max(self.__height(node.left), self.__height(node.right))

    def maxValue(self):
        return self.__maxValue(self.root)

    def __maxValue(self, node):
        return -sys.maxsize if node == None else max(max(self.__maxValue(node.left), self.__maxValue(node.right)), node.value)

    def minValue(self):
        return self.__minValue(self.root)

    def __minValue(self, node):
        return sys.maxsize if node == None else min(min(self.__minValue(node.left), self.__minValue(node.right)), node.value)

    def diameter(self):
        return self.__diameter(self.root)[1]

    def __diameter(self, node):
        if node == None:
            return [-1, 0]

        left = self.__diameter(node.left)
        right = self.__diameter(node.right)

        height = 1 + max(letf[0], right[0])
        dia = max(max(left[1], right[1]), 2 + left[0] + right[0])
        return [height. dia]

    def width(self):
        self.__width(self.root, 0)
        return rightMost - leftMost

    def __width(self, node, width):
        if node == None:
            return

        self.leftMost = min(width, self.leftMost)
        self.rightMost = max(width, self.rightMost)

        self.__width(node.left, width-1)
        self.__width(node.right, width+1)

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

    def rightMostOfLeft(self, node, curr):
        while node.right != None and node.right != curr:
            node = node.right
        return node

    def morrisPreOrder(self):
        res = []
        curr = self.root
        while curr != None:
            if curr.left == None:
                res.append(curr.value)
                curr = curr.right
            else:
                rightMost = self.rightMostOfLeft(curr.left, curr)
                if rightMost.right == None:
                    rightMost.right = curr
                    res.append(curr.value)
                    curr = curr.left
                else:
                    rightMost.right = None
                    curr = curr.right
        return res

    def morrisInOrder(self):
        res = []
        curr = self.root
        while curr != None:
            if curr.left == None:
                res.append(curr.value)
                curr = curr.right
            else:
                rightMost = self.rightMostOfLeft(curr.left, curr)
                if rightMost.right == None:
                    rightMost.right = curr
                    curr = curr.left
                else:
                    rightMost.right = None
                    res.append(curr.value)
                    curr = curr.right
        return res

    def levelOrder(self):
        queue = queue.deque(self.root)
        res = []

        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                rn = queue.popleft()
                res.append(rn.value)

                if rn.left != None:
                    queue.append(rn.left)
                if rn.right != None:
                    queue.append(rn.right)

                size -= 1
        return res

    def levelOrderToInOrder(self, arr):  # ? Similarly to PreOrder and PostOrder
        res = []
        self.__levelOrderToInOrder(arr, 0, res)
        return res

    def __levelOrderToInOrder(self, arr, idx, res):
        if idx >= len(arr):
            return
        self.__levelOrderToInOrder(arr, 2*idx + 1, res)
        res.append(arr[idx])
        self.__levelOrderToInOrder(arr, 2*idx + 2, res)

    def verticalOrder(self):
        queue = queue.deque([self.root, -self.leftMost])
        res = [[] for i in range(0, self.width())]

        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                rn = queue.popleft()

                node = rn[0]
                width = rn[1]

                res[width].append(node.value)

                if node.left != None:
                    queue.append([node.left, width - 1])
                if node.right != None:
                    queue.append([node.right, width + 1])

                size -= 1
        return res

    def diagonalOrder(self):
        queue = queue.deque([self.root, 0])
        res = [[] for i in range(0, self.width())]

        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                rn = queue.popleft()

                node = rn[0]
                width = rn[1]

                res[width].append(node.value)

                if node.left != None:
                    queue.append([node.left, width + 1])
                if node.right != None:
                    queue.append([node.right, width])

                size -= 1
        return res

    def antiDiagonalOrder(self):
        queue = queue.deque([self.root, 0])
        res = [[] for i in range(0, self.width())]

        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                rn = queue.popleft()

                node = rn[0]
                width = rn[1]

                res[width].append(node.value)

                if node.left != None:
                    queue.append([node.left, width])
                if node.right != None:
                    queue.append([node.right, width + 1])

                size -= 1
        return res

    def leftView(self):
        queue = queue.deque(self.root)
        res = [-1 for i in range(0, self.height())]

        level = 0
        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                rn = queue.popleft()
                if res[level] == -1:
                    res[level] = rn.value

                if rn.left != None:
                    queue.append(rn.left)
                if rn.right != None:
                    queue.append(rn.right)

                size -= 1
            level += 1
        return res

    def rightView(self):
        queue = queue.deque(self.root)
        res = []

        level = 0
        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                rn = queue.popleft()
                res[level] = rn.value

                if rn.left != None:
                    queue.append(rn.left)
                if rn.right != None:
                    queue.append(rn.right)

                size -= 1
            level += 1
        return res

    def topView(self):
        queue = queue.deque([self.root, -self.leftMost])
        res = [-1 for i in range(0, self.width())]

        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                rn = queue.popleft()

                node = rn[0]
                width = rn[1]

                if res[width] == -1:
                    res[width] = node.value

                if node.left != None:
                    queue.append([node.left, width - 1])
                if node.right != None:
                    queue.append([node.right, width + 1])

                size -= 1
        return res

    def bottomView(self):
        queue = queue.deque([self.root, -self.leftMost])
        res = []

        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                rn = queue.popleft()

                node = rn[0]
                width = rn[1]

                res[width] = node.value

                if node.left != None:
                    queue.append([node.left, width - 1])
                if node.right != None:
                    queue.append([node.right, width + 1])

                size -= 1
        return res

    def boundaryView(self):
        top = self.topView()
        bottom = self.bottomView()

        res = [ele for ele in top]
        for i in range(-2, 1, -1):
            res.append(bottom[i])
        return res

    def rootToNodePath(self, target):
        res = []
        self.__rootToNodePath(self.root, target, res)
        return res.reverse()

    def __rootToNodePath(self, node, target, res):
        if node == None:
            return

        if node.value == target:
            res.append(node)
            return

        self.__rootToNodePath(node.left, target, res)
        if len(res) != 0:
            res.apend(node)
            return
        self.__rootToNodePath(node.right, target, res)
        if len(res) != 0:
            res.apend(node)
            return

    def lowestCommonAncestor1(self, n1, n2):
        return self.__lowestCommonAncestor1(n1, n2)

    def __lowestCommonAncestor1(self, n1, n2):
        rtnp1 = self.rootToNodePath(n1)
        rtnp2 = self.rootToNodePath(n2)

        n = len(rtnp1)
        m = len(rtnp2)

        resNode = None
        for i in range(0, min(n, m)):
            if rtnp1[i] == rtnp2[i]:
                resNode = rtnp1[i]
        return resNode

    def lowestCommonAncestor2(self, n1, n2):
        return self.__lowestCommonAncestor2(self.root, n1, n2)

    def __lowestCommonAncestor2(self, node, n1, n2):
        if node == None:
            return False

        selfWork = False
        if node.value == n1 or node.value == n2:
            selfWork = True

        leftWork = self.__lowestCommonAncestor2(node.left, n1, n2)
        rightWork = self.__lowestCommonAncestor2(node.right, n1, n2)

        if self.lca == None and ((selfWork and leftWork) or (selfWork and rightWork) or (leftWork and rightWork)):
            self.lca = node

        return selfWork or leftWork or rightWork

    def distanceBetweenTwoNodes(self, n1, n2):
        self.distance = -1
        return self.__distanceBetweenTwoNodes(self.root, n1, n2)[0]

    def __distanceBetweenTwoNodes(self, node, n1, n2):
        if node == None:
            return [-1, 0]

        selfWork = False
        if node.value == n1 or node.value == n2:
            selfWork = True

        leftWork = self.__distanceBetweenTwoNodes(node.left, n1, n2)
        rightWork = self.__distanceBetweenTwoNodes(node.right, n1, n2)

        if self.distance != -1:
            return [self.distance, 1]

        if self.distance == -1 and ((selfWork and leftWork[1] == 1) or (selfWork and rightWork[1] == 1) or (leftWork[1] == 1 and rightWork[1] == 1)):
            self.distance = left[0] + right[0]
            return [self.distance, 1]

        if selfWork:
            return [1, 1]
        if leftWork[1] == 1:
            return [left[0] + 1, 1]
        if rightWork[1] == 1:
            return [right[0] + 1, 1]
        return [-1, 0]

    def kDistanceChildren(self, target, k):
        res = []
        self.__kDistanceChildren(self.search(target), k, res)
        return res

    def __kDistanceChildren(self, node, k, res):
        if node == None:
            return

        if k == 0:
            res.append(node)
            return

        self.__kDistanceChildren(node.left, k - 1, res)
        self.__kDistanceChildren(node.right, k - 1, res)

    def kDistanceChildrenWithBlockNode(self, target, blockNode, k):
        res = []
        self.__kDistanceChildrenWithBlockNode(
            self.search(target), blockNode, k, res)
        return res

    def __kDistanceChildrenWithBlockNode(self, node, blockNode, k, res):
        if node == None or node == blockNode:
            return

        if k == 0:
            res.append(node)
            return

        self.__kDistanceChildrenWithBlockNode(node.left, blockNode, k - 1, res)
        self.__kDistanceChildrenWithBlockNode(
            node.right, blockNode, k - 1, res)

    def kDistanceNodes1(self, target, k):
        return self.__kDistanceNodes1(self.search(target), k)

    def __kDistanceNodes1(self, node, k):
        path = self.rootToNodePath(node.value)
        path.append(None)
        n = len(path)

        res = []
        for i in range(n-1, -1, -1):
            if k > n-i-2:
                l = self.kDistanceChildrenWithBlockNode(
                    path[i].value, path[i+1], k-(n-i-2))
                for child in l:
                    res.append(child)
        return res

    def kDistanceNodes2(self, target, k):
        res = []
        self.__kDistanceNodes2(self.root, target, k, res)
        return res

    def __kDistanceNodes2(self, node, target, k, list):
        if node == None:
            return -1
        if node.value == target:
            list = self.kDistanceChildren(target, k)
            return 1

        leftDistance = self.__kDistanceNodes2(node.left, target, k, list)
        if leftDistance != -1:
            l = self.kDistanceChildrenWithBlockNode(target, node.left, k)
            for ele in l:
                list.append(ele)
            return leftDistance + 1

        rightDistance = self.__kDistanceNodes2(node.left, target, k, list)
        if rightDistance != -1:
            l = self.kDistanceChildrenWithBlockNode(target, node.right, k)
            for ele in l:
                list.append(ele)
            return rightDistance + 1
        return -1

    ans = []

    def kSumPathFromRoot(self, k):
        ans = []
        self.__kSumPathFromRoot(self.root, 0, k, [])
        return ans

    def __kSumPathFromRoot(self, node, sum, k, res):
        if node == None:
            return

        if sum == k:
            ans, append([ele for ele in res])
            return ans[-1]

        res, add(node.value)
        self.__kSumPathFromRoot(node.left, sum + node.value, k, res)
        self.__kSumPathFromRoot(node.right, sum + node.value, k, res)

    def kSumPaths1(self, k):
        ans = []
        self.__kSumPaths1(self.root, k)
        return ans

    def __kSumPaths1(self, node, k):
        if node == None:
            return

        self.__kSumPathFromRoot(node, k, 0, [])
        self.__kSumPath1(node.left, k)
        self.__kSumPath1(node.right, k)

    preOrder = []

    def kSumPaths2(self, k):
        preOrder = []
        ans = []
        self.__kSumPaths2(self.root, k)
        return ans

    def __kSumPaths2(self, node, k):
        if node == None:
            return

        preOrder.append(node.value)

        self.__kSumPaths2(node.left, k)
        self.__kSumPaths2(node.right, k)

        sum = 0
        path = []
        for i in range(len(preOrder) - 1, -1. - 1):
            sum += preOrder[i]
            path.append(preOrder[i])
            if sum == k:
                res = [ele for ele in path]
                ans.append(res)
        preOrder.pop()

    def maxPathSum(self):
        return self.__maxPathSum(self.root)

    def __maxPathSum(self, node):
        if node == None:
            return -sys.maxsize

        leftMax = self.__maxPathSum(node.left)
        rightMax = self.__maxPathSum(node.right)

        a = leftMax + node.value
        b = rightMax + node.value
        c = node.value
        d = leftMax + node.value + rightMAx

        return max(max(a, b), max(c, d))

    def getMirror(self):
        return self.__getMirror(self.root)

    def __getMirror(self, node):
        if node == None:
            return node

        nn = binaryTree.TreeNode(node.value)
        nn.left = self.__getMirror(node.right)
        nn.right = self.__getMirror(node.left)
        return nn

    def isMirror(sekf, targetNode):
        return self.__isMirror(self.root, targetNode)

    def __isMirror(self, node, targetNode):
        if node == None and targetNode == None:
            return True
        if node == None or targetNode == None:
            return False
        if node.value != targetNode.value:
            return False
        return self.__isMirror(node.left, targetNode.right) and self.__isMirror(node.right, targetNode.left)

    def isFoldable(self):
        return self.isMirror(self.root)

    def treeToSumTree(self):
        return self.__treeToSumTree(self.root)

    def __treeToSumTree(self, node):
        if node == None:
            return 0

        value = node.value
        node.value = self.__treeToSumTree(
            node.left) + self.__treeToSumTree(node.right)
        return value + node.value

    def isSumTree(self):
        return self.isSumTree(self.root)

    def __isSumTree(self, root):
        if node == None:
            return [0, 1]
        if node.left == None and node.right == None:
            return [node.value, 1]

        left = self.__isSumTree(node.left)
        right = self.__isSumTree(node.right)

        if left[1] == 0 or right[1] == 0 or node.value != left[0] + right[0]:
            return [0, 0]
        return [node.value + left[0] + right[0], 1]

    def isIsomorphic(self, targetNode):
        return self__isIsomorphic(self.root, targetNode)

    def __isIsomorphic(self, node, targetNode):
        if node == None and targetNode == None:
            return True
        if node == None or targetNode == None or node.value != targetNode.value:
            return False
        return (self.__isIsomorphic(node.left, targetNode.left) and self.__isIsomorphic(node.right, targetNode.right)) or (self.__isIsomorphic(node.left, targetNode.right) and self.__isIsomorphic(node.right, targetNode.left))

    def serialize(self):
        return self.__serialize(self.root)

    def __serialize(self, node):
        if node == None:
            return "-1"

        left = self.__serialize(node.left)
        right = self.__serialize(node.right)

        return "" + node.value + "," + left + "," + right

    def deserialize(self, s):
        arr = s.split(",")
        preOrder = []

        for i, ele in enumerate(arr):
            preOrder[i] = int(ele)

        self.idx = 0
        return __deserialize(arr)

    def __deserialize(self, preOrder):
        if self.idx == len(preOrder):
            return None

        if preOrder[self.idx] == -1:
            self.idx += 1
            return None

        nn = binaryTree.TreeNode(preOrder[idx])
        idx += 1

        nn.left = self.__deserialize(preOrder)
        nn.right = self.__deserialize(preOrder)
        return nn

    def treeToDLL(self):
        self.__treeToDLL(self.root)
        return self.DLLHead

    def __treeToDLL(self, node):
        if node == None:
            return

        self.__treeToDLL(node.left)

        if self.DLLHead == None:
            self.DLLHead = node
        else:
            self.DLLPrev.right = node
            node.left = self.DLLPrev

        self.DLLPrev = node

        self.__treeToDLL(node.right)

    def isDuplicateSubTreeExist(self):
        self.map = {}
        self.__isDuplicateSubTreeExist(self.root)
        return self.isDuplicateExist

    def __isDuplicateSubTreeExist(self, node):
        if node == None:
            return "-1"
        left = self.__isDuplicateSubTreeExist(node.left)
        right = self.__isDuplicateSubTreeExist(node.right)

        s = "" + node.value + left + right
        if s in self.map.keys():
            self.isDuplicateExist = True
        else:
            self.map[s] = 1

        return s

    def allDuplicates(self):
        self.map = {}
        return self.__allDuplicates(self.root)

    def __allDuplicates(self, node):
        if node == None:
            return "-1"
        left = self.__allDuplicates(node.left)
        right = self.__allDuplicates(node.right)

        s = "" + node.value + left + right
        if s in self.map.keys():
            self.map[s] += 1
        else:
            self.map[s] = 1
        return s

    def houseRobber3(self, node):
        p = self.__houseRobber3(node)
        return max(p[0], p[1])

    def __houseRobber3(self, node):
        if node == None:
            return [0, 0]

        left = self.__houseRobber3(node.left)
        right = self.__houseRobber3(node.right)

        inc = left[1] + right[1] + node.value
        exc = max(left[1], left[0]) + max(right[1], right[0])

        return [inc, exc]

    def minSwapsFromBinaryToBST(self, levelOrder):
        inOrder = self.levelOrderToInOrder(levelOrder)
        arr = []

        for i, ele in enumerate(inOrder):
            arr.append([ele, i])
        sorted(arr, key=lambda x: (x[0], x[1]))

        count = 0
        n = len(arr)
        for i in range(0, n):
            if arr[i][0] != i:
                self.swap(arr, i, j)
                count += 1
                i -= 1
        return count

    def swap(self, arr, i, j):
        temp = arr[i][0]
        arr[i][0] = arr[j][0]
        arr[j][0] = temp
        temp = arr[i][1]
        arr[i][1] = arr[j][1]
        arr[j][1] = temp

    def binaryToBST(self):
        inOrder = self.inOrder()
        sorted(inOrder)
        self.idx = 0
        self.fill(self.root, inOrder)

    def fill(self, node, inOrder):
        if node == None or self.idx >= len(inOrder):
            return

        self.fill(node.left, inOrder)
        node.value = inOrder[idx]
        idx += 1
        self.fill(node.right, inOrder)

    def largestBST1(self):
        inOrder = self.inOrder()
        n = len(inOrder)
        res = 1
        count = 1
        for i in range(0, n-1):
            if inOrder[i] < inOrder[i+1]:
                count += 1
            else:
                res = max(res, count)
                count = 0
        return max(res, count)

    def largestBST2(self):
        return self.__largestBST2(self.root)

    def __largestBST2(self, node):
        if node == None:
            return [0, 0, 0, 0, False]

        left = self.__largestBST2(node.left)
        right = self.__largestBST2(node.right)

        mi = min(node.value, min(left[0], right[0]))
        ma = max(node.value, max(left[1], right[1]))
        size = left[2] + right[2] + 1

        if left[4] and right[4]:
            if left[1] < node.value and right[0] > node.value:
                return [mi, ma, size, size, True]
            else:
                return [mi, ma, size, max(left[2], right[2]), False]
        return [mi, ma, size, max(left[3], right[3]), False]
