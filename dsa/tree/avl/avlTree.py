import sys


class avlTree:
    class TreeNode:
        def __init__(self, v):
            self.value = v
            self.left = None
            self.right = None
            self.height = -1

    def __init__(self):
        self.root = None

    def balanceFactor(self, node):
        if node == None:
            return 0
        return (node.left.height if node.left != None else 0) - (node.right.height if node.right != None else 0)

    def add(self, v):
        self.root = self.__add(self.root, v)

    def __add(self, node, v):
        if node == None:
            return avlTree.TreeNode(v)

        if v < node.value:
            node.left = self.__add(node.left, v)
        else:
            node.right = self.__add(node.right, v)

        node.height = max(node.left.height, node.right.height) + 1
        return self.balance(node)

    def rempve(self, v):
        self.__remove(self, self.root, v)

    def __max(self, node):
        if node == None:
            return -sys.maxsize
        return max(max(self.__max(node.left), self.__max(node.right)), node.value)

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
        node.height = max(node.left.height, node.right.height) + 1
        return self.balance(node)

    def balance(self, node):
        if node == None:
            return node

        bf = self.balanceFactor(node)

        #  ** LL
        if bf > 1 and ele < node.left.value:
            return self.rightRotate(node)
        #  ** RR
        if bf < -1 and ele > node.right.value:
            return self.leftRotate(node)
        #  ** LR
        if bf > 1 and ele > node.left.value:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        #  ** RL
        if bf < -1 and ele < node.right.value:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def rightRotate(self, c):
        b = c.left
        t3 = b.right

        b.right = c
        c.left = t3

        b.height = max(b.left.height, b.right.height) + 1
        c.height = max(c.left.height, c.right.height) + 1
        return b

    def leftRotate(self, c):
        b = c.right
        t3 = b.left

        b.left = c
        c.right = t3

        b.height = max(b.left.height, b.right.height) + 1
        c.height = max(c.left.height, c.right.height) + 1
        return b
