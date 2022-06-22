from queue import deque


class generic:

    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.children = []

    def __init__(self):
        self.root = None
        self.idx = 0
        self.lca = 0

    def display(self):
        self.__display(self.root)

    def __display(self, node):
        if node == None:
            return

        s = "" + node.value
        for child in node.children:
            s += " -> " + child.value

        print(s)

        for child in node.children:
            self.__display(child)

    def constructFromPreOrder(self, arr):
        self.idx = 0
        self.root = self.__constructFromPreOrder(arr)

    def __constructFromPreOrder(self, arr):
        if self.idz >= len(arr) or arr[self.idx] == -1:
            self.idx += 1
            return None

        nn = generic.TreeNode(arr[self.idx])
        self.idx += 1
        child = self.__constructFromPreOrder(arr)
        while child != None:
            nn.children.append(child)
            child = self.__constructFromPreOrder(arr)
        return nn

    def size(self):
        return self.__size(self.root)

    def __size(self, node):
        if node == None:
            return 0

        s = 0
        for child in node.children:
            s += self.__size(child)
        return s + 1

    def find(self, target):
        return self.__find(self.root, target)

    def __find(self, node, target):
        if node == None or node.value == target:
            return True

        res = False
        for child in node.children:
            res = res or self.__find(child, target)
        return res

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node == None:
            return -1
        h = 0
        for child in node.children:
            h = max(h, self.__height(child))
        return h + 1

    def diameter(self):
        return self.__diameter(self.root)[1]

    def __diameter(self, node):
        if node == None:
            return [-1, 0]

        currChildDiameter = []

        firstMaxHeight = -1
        secondMaxHeight = -1
        firstMaxDiameter = -1
        secondMaxDiameter = -1
        for c in node.children:
            currChildDiameter.append(self.__diameter(c))
            child = currChildDiameter[len(currChildDiameter) - 1]

            if child[0] > firstMaxHeight:
                secondMaxHeight = firstMaxHeight
                firstMaxHeight = child.height
            elif child[0] > secondMaxHeight:
                secondMaxHeight = child.height

            if child[1] > firstMaxDiameter:
                secondMaxDiameter = firstMaxDiameter
                firstMaxDiameter = child.diameter
            elif child[1] > secondMaxHeight:
                secondMaxDiameter = child.diameter

        height = max(firstMaxHeight, secondMaxHeight) + 1
        diameter = max(max(firstMaxDiameter, secondMaxDiameter),
                       firstMaxHeight + secondMaxHeight + 2)
        return [height. dia]

    def preOrder(self):
        arr = []
        self.__preOrder(self.root)
        return arr

    def __preOrder(self, node, arr):
        if node == None:
            return

        arr.append(node.value)
        for child in node.children:
            self.__preOrder(child, arr)

    def postOrder(self):
        arr = []
        self.__postOrder(self.root)
        return arr

    def __postOrder(self, node, arr):
        if node == None:
            return

        for child in node.children:
            self.__postOrder(child, arr)
        arr.append(node.value)

    def levelOrder(self):
        q = deque(self.root)

        res = []
        while len(q) != 0:
            size = len(q)
            while size > 0:
                size -= 1
                rn = q.popleft()
                res.append(rn.value)
                for child in node.children:
                    q.append(child)
        return res

    def serialize(self):
        return self.__serialize(self.root)

    def __serialize(self, node):
        if node == None:
            return "-1"

        s = "" + node.value
        for child in node.children:
            s += self.__serialize(node.left) + ", "
        return s

    def deserialize(self, s):
        arr = s.split(",")
        preOrder = []

        for i, ele in enumerate(arr):
            preOrder[i] = int(ele)

        self.idx = 0
        return __deserialize(arr)

    def __deserialize(self, arr):
        self.constructFromPreOrder(arr)

    def isMirror(sekf, targetNode):
        return self.__isMirror(self.root, targetNode)

    def __isMirror(self, node, targetNode):
        if node == None and targetNode == None:
            return True
        if node == None or targetNode == None:
            return False
        if node.value != targetNode.value:
            return False

        n = len(node.children)
        if n != len(targetNode.children):
            return False

        for i in range(n):
            if node.children[i].value != targetNode.children[n-i-1].value:
                return False
        for i in range(n):
            if self.__isMirror(node.children[i], targetNode.children[n-i-1]):
                return False
        return True

    def isFoldable(self):
        return self.__isMirror(self.root, self.root)

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

        for child in node.children:
            self.__rootToNodePath(child, target, res)
            if len(res) != 0:
                res.apend(node)
                return

    def lowestCommonAncestor(self, n1, n2):
        return self.__lowestCommonAncestor(self.root, n1, n2)

    def __lowestCommonAncestor(self, node, n1, n2):
        if node == None:
            return False

        selfWork = False
        if node.value == n1 or node.value == n2:
            selfWork = True

        leftWork = False
        rightWork = False
        for child in node.children:
            res = self.__lowestCommonAncestor(child, n1, n2)
            if res and not leftWork:
                leftWork = True
            elif res and not rightWork:
                rightWork = True

        if self.lca == None and ((selfWork and leftWork) or (selfWork and rightWork) or (leftWork and rightWork)):
            self.lca = node

        return selfWork or leftWork or rightWork

    def flatten(self):
        self.__flatten(self.root)

    def __flatten(self, node):
        if node == None:
            return

        allChildren = []
        for child in node.children:
            self.__flatten(child)
            allChildren.append(child)
            allChildren.extend(child.children)
            child.children.clear()
        node.children.clear()
        node.children = allChildren

    def toLinearTree(self):
        self.root = self.__toLinearTree(self.root)

    def __toLinearTree(self, node):
        if node == None:
            return node

        lastNode = self.__toLinearTree(node.children[len(node.children) - 1])
        for i in range(len(node.children) - 1, 0, -1):
            secondLast = self.__toLinearTree(node.children[i])
            secondLast.children.add(node.children[i + 1])
            node.children.pop()
        return lastNode
