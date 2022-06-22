from stack import Stack
from math import *
from queue import deque
from __queue._queue import *
import sys
sys.path.insert(1, 'D:\Python\simp\dsa')


def insertAtBottom(stack, ele):
    if stack.isEmpty():
        stack.push(ele)
        return
    re = stack.pop()
    insertAtBottom(stack, ele)
    stack.push(ele)


def reverseStack1(stack):  # Using Recursion
    if stack.isEmpty():
        return
    re = stack.pop()
    insertAtBottom(stack, re)
    reverseStack1(stack)


def reverseStack2(stack):  # Using Queue
    helper = _queue.Queue(len(stack))
    while stack.isEmpty() == False:
        helper.enqueue(stack.pop())

    while queue.isEmpty() == False:
        stack.push(helper.dequeue())
    return stack


def reverseStack3(stack):  # Using LinkedList
    return stack.reverse()


def reverse(stack, helper):
    if helper.isEmpty():
        return
    re = helper.pop()
    reverse(stack, helper)
    stack.push(re)


def reverseStack4(stack):  # Using Stack
    helper = Stack()
    while stack.isEmpty() == False:
        helper.push(stack.pop())
    reverse(stack, helper)
    return stack


def placeItAtRightPosition(stack, ele):
    if stack.isEmpty():
        stack.push(ele)
        return

    if stack.peek() > ele:
        re = stack.pop()
        placeItAtRightPosition(stack, ele)
        stack.push(re)
    else:
        stack.push(ele)


def sort(stack):
    helper = Stack()
    while stack.isEmpty() == False:
        placeItAtRightPosition(helper, stack.pop())
    while helper.isEmpty() == False:
        stack.push(helper.pop())
    return stack


def nextGreater(arr):
    n = len(arr)
    stack = Stack()
    res = [n for x in range(0, n)]
    for i in range(0, n):
        while stack.isEmpty() == False and arr[stack.peek()] < arr[i]:
            res[stack.pop()] = i
        stack.push(i)
    return res


def nextSmaller(arr):
    n = len(arr)
    stack = Stack()
    res = [n for x in range(0, n)]
    for i in range(0, n):
        while stack.isEmpty() == False and arr[stack.peek()] > arr[i]:
            res[stack.pop()] = i
        stack.push(i)
    return res


def prevGreater(arr):
    n = len(arr)
    stack = Stack()
    res = [-1 for x in range(0, n)]
    for i in range(n-1, -1, -1):
        while stack.isEmpty() == False and arr[stack.peek()] < arr[i]:
            res[stack.pop()] = i
        stack.push(i)
    return res


def prevSmaller(arr):
    n = len(arr)
    stack = Stack()
    res = [-1 for x in range(0, n)]
    for i in range(n-1, -1, -1):
        while stack.isEmpty() == False and arr[stack.peek()] > arr[i]:
            res[stack.pop()] = i
        stack.push(i)
    return res


def maxOfMinOfAllWindows(arr):

    n = len(arr)
    nextSmaller = nextSmaller(arr)
    prevSmaller = prevSmaller(arr)

    res = [-1 for x in range(0, n)]

    for i in range(0, n):
        windowSize = nextSmaller[i] - prevSmaller[i] - 1
        res[windowSize-1] = max(res[windowSize-1], arr[i])

    for i in range(n-2, -1, -1):
        res[i] = max(res[i], res[i+1])
    return res


def rainwaterTrapping1(arr):
    n = len(arr)
    leftMax = [0 for x in range(0, n)]
    rightMax = [0 for x in range(0, n)]

    leftMax[0] = -sys.maxsize
    rightMax[arr.length - 1] = -sys.maxsize

    for i in range(0, n):
        leftMax[i] = max(arr[i - 1], leftMax[i - 1])
    for i in range(n-1, -1, -1):
        rightMax[i] = max(arr[i + 1], rightMax[i + 1])

    res = 0
    for i in range(0, n):
        res += max(0, min(leftMax[i], rightMax[i]) - arr[i])
    return res


def rainWaterTrapping2(arr):
    n = len(arr)
    stack = Stack()

    res = 0
    for i in range(0, n):
        while stack.isEmpty() == False and arr[stack.peek()] < arr[i]:
            currIdx = stack.pop()
            if stack.isEmpty():
                break
            width = i - currIdx
            res += width * (min(arr[stack.peek()], arr[i]) - arr[currIdx])
        stack.push(i)
    return res


def areaInHistogram1(arr):
    n = len(arr)
    res = 0
    for i in range(0, n):
        currHeight = arr[i]
        for j in range(0, n):
            if arr[j] <= arr[i]:
                currHeight = Math.min(currHeight, arr[j])
        idx = n - 1
        for j in range(n-1, -1, -1):
            if arr[j] == currHeight:
                idx = j
                break
        width = idx - i + 1
        res = Math.max(res, width * currHeight)
    return res


def areaInHistogram2(arr):
    n = len(arr)
    stack = Stack()
    stack.push(0)

    res = 0
    for i in range(0, n):
        while stack.isEmpty() == False and arr[stack.peek()] > arr[i]:
            currIdx = stack.pop()
            if stack.isEmpty():
                res = max(res, arr[currIdx] * i)
                continue
            width = i - currIdx + 1
            res = max(res, width * arr[currIdx])
        stack.push(i)
    return res


def stockspan(arr):
    n = len(arr)

    stack = []
    ans = [1 for x in range(0, n)]
    for i in range(0, n):
        count = 0
        while len(stack) != 0 and stack[len(stack) - 1][0] < arr[i]:
            temp = stack.pop()
            count += temp[1]
        ans[i] += count
        stack.append([arr[i], count + 1])
    return ans


def validStackSequence(pushed, popped):
    stack = []

    n = len(pushed)
    j = 0
    for i in range(0, n):
        while len(stack) != 0 and popped[j] == stack[len(stack) - 1]:
            stack.pop()
            j += 1
        stack.append(pushed[i])

    for k in range(j, n):
        while len(stack) != 0 and popped[k] == stack[len(stack) - 1]:
            stack.pop()
    return len(stack) == 0


def pattern132(arr):
    n = len(arr)

    preMin = [0 for x in range(0, n)]
    preMin[0] = sys.maxsize
    for i in range(1, n):
        preMin[i] = min(preMin[i-1], arr[i-1])

    stack = []
    for i in range(n-1, -1, -1):
        while len(stack) != 0 and preMin[i] >= arr[stack[len(stack) - 1]]:
            stack.pop()
        if len(stack) != 0 and arr[stack[len(stack) - 1]] < arr[i] and preMin[i] < arr[stack[len(stack) - 1]]:
            return True
        s.append(i)
    return False


def celebrityProblem(mat):
    n = len(mat)
    stack = [i for i in range(0, n)]

    while len(stack) != 1:
        a = stack.pop()
        b = stack.pop()

        if mat[a][b] == 1:
            stack.append(b)
        else:
            stack.append(a)
    return stack.pop()


def isBalancedParenthesis(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) != 0 or stack[len(stack) - 1] != '(':
                return False
            else:
                stack.pop()
    return len(stack) == 0

# ? Duplicate Parenthesis


def redundantParenthesis(s):  # Duplicate Parenthesis
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(0)
        elif ch != ')':
            stack.append(1)
        else:
            count = 0
            while len(stack) != 0 or stack[len(stack) - 1] != 0:
                s.pop()
                count += 1
            if len(stack) != 0:
                s.pop()
            if count < 1:  # If count of operators is < 1
                return true
    return len(stack) != 0

#  ***** Minimum number of bracket reversals needed to make an expression
#  ***** balanced


def countReversals(arr):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) != 0 or stack[len(stack) - 1] == '(':
                stack.pop()
            else:
                stack.append(ch)

    count1 = 0
    count2 = 0
    while len(stack) != 0:
        rc = stack.pop()
        if rc == '(':
            count1 += 1
        else:
            count2 += 1
    return int(ceil(count1/2)) + int(ceil(count2/2))


def longestValidParenthesis(s):
    stack = [-1]

    res = 0
    for i in range(0, n):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) > 1 and s[stack[len(stack) - 1]] == '(':
                res = max(res, i - stack.pop())
            else:
                stack.append(i)
    return res


precedence = {}
associativity = {}


def builderForConverter():
    precedence['*'] = 2
    precedence['^'] = 3
    precedence['/'] = 2
    precedence['+'] = 1
    precedence['-'] = 1

    associativity['^'] = False
    associativity['*'] = True
    associativity['/'] = True
    associativity['+'] = True
    associativity['-'] = True


def infixTOpostfix(s):
    builderForConverter()
    ans = ""

    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            while len(stack) > 1 and stack[len(stack) - 1] != '(':
                ans += stack.pop()
            stack.pop()
        elif ch not in precedence.keys():
            ans += ch
        else:
            if len(stack) == 0 or stack[len(stack) - 1] != '(':
                stack.append(ch)
                continue
            elif precedence[ch] != precedence[stack[len(stack) - 1]]:
                while len(stack) != 0 and stack[len(stack) - 1] != '(' and precedence[stack[len(stack) - 1]] >= precedence[ch]:
                    ans += stack.pop()
            else:
                if associativity[ch]:
                    ans += stack.pop()
            stack.append(ch)

    while len(stack) != 0:
        ans += stack.pop()

    return ans


def infixTOPreFix(s):
    s = s[::-1]
    builderForConverter()
    ans = ""

    stack = []
    for ch in s:
        if ch == '}':
            stack.append(ch)
        elif ch == '(':
            while len(stack) > 1 and stack[len(stack) - 1] != ')':
                ans += stack.pop()
            stack.pop()
        elif ch not in precedence.keys():
            ans += ch
        else:
            if len(stack) == 0 or stack[len(stack) - 1] != ')':
                stack.append(ch)
                continue
            elif precedence[ch] != precedence[stack[len(stack) - 1]]:
                while len(stack) != 0 and stack[len(stack) - 1] != ')' and precedence[stack[len(stack) - 1]] < precedence[ch]:
                    ans += stack.pop()
            else:
                if associativity[ch]:
                    ans += stack.pop()
            stack.append(ch)

    while len(stack) != 0:
        ans += stack.pop()

    return ans[::-1]


def postfixTOinfix(s):
    builderForConverter()
    ans = ""

    stack = []
    for ch in s:
        if ch not in precedence.keys():
            stack.append(str(ch))
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append("(" + s1 + "" + str(ch) + "" + s2 + ")")
    return stack.pop()


def prefixToInfix(s):
    builderForConverter()
    ans = ""

    stack = []
    for ch in s:
        if ch not in precedence.keys():
            stack.append(str(ch))
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append("(" + s2 + "" + str(ch) + "" + s1 + ")")
    return stack.pop()


def postfixTOprefix(s):
    builderForConverter()
    ans = ""

    stack = []
    for ch in s:
        if ch not in precedence.keys():
            stack.append(str(ch))
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append("(" + str(ch) + "" + s2 + "" + s1 + ")")
    return stack.pop()


def prefixTOpostfix(s):
    builderForConverter()
    ans = ""

    stack = []
    for ch in s:
        if ch not in precedence.keys():
            stack.append(str(ch))
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append("(" + s2 + "" + s1 + "" + str(ch) + ")")
    return stack.pop()


def arithmeticExpression(str, key):
    if (key == 0):
        return postfixExpression(str)
    elif (key == 1):
        return infixExpression(str)
    else:
        return prefixExpression(str)


def operate(a, b, ch):
    res = 0
    if (ch == '+'):
        res = a + b
    elif (ch == '-'):
        res = a - b
    elif (ch == '*'):
        res = a * b
    elif (ch == '/'):
        res = a / b
    else:
        res = int(pow(a, b))
    return res


def prefix(s):
    builderForConverter()
    ans = ""

    stack = []
    for ch in s:
        if ch not in precedence.keys():
            stack.append(ord(ch) - ord('0'))
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append(operate(s1, s2, ch))
    return stack.pop()


def postfix(s):
    builderForConverter()
    ans = ""

    stack = []
    for ch in s:
        if ch not in precedence.keys():
            stack.append(ord(ch) - ord('0'))
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append(operate(s2, s1, ch))
    return stack.pop()


def infix(s):
    return postfix(infixTOpostfix(s))


class Node:
    def __init__(self, node):
        self.left = self.right = self.curr = False
        self.node = node


def preOrder(node):
    stack = [Node(node)]

    ans = []
    while len(stack) != 0:
        top = stack[len(stack) - 1]
        if top.curr == False:
            top.curr = True
            ans.append(top.node.value)
        elif top.left == False:
            top.left = True
            if top.node.left != None:
                stack.append(Node(top.node.left))
        elif top.right == False:
            top.right = True
            if top.node.right != None:
                stack.append(Node(top.node.right))
        else:
            stack.pop()
    return ans


def inOrder(node):
    stack = [Node(node)]

    ans = []
    while len(stack) != 0:
        top = stack[len(stack) - 1]
        if top.left == False:
            top.left = True
            if top.node.left != None:
                stack.append(Node(top.node.left))
        elif top.curr == False:
            top.curr = True
            ans.append(top.node.value)
        elif top.right == False:
            top.right = True
            if top.node.right != None:
                stack.append(Node(top.node.right))
        else:
            stack.pop()
    return ans


def inOrder(node):
    stack = [Node(node)]

    ans = []
    while len(stack) != 0:
        top = stack[len(stack) - 1]
        if top.left == False:
            top.left = True
            if top.node.left != None:
                stack.append(Node(top.node.left))
        elif top.curr == False:
            top.curr = True
            ans.append(top.node.value)
        elif top.right == False:
            top.right = True
            if top.node.right != None:
                stack.append(Node(top.node.right))
        else:
            stack.pop()
    return ans


def postOrder(node):
    stack = [Node(node)]

    ans = []
    while len(stack) != 0:
        top = stack[len(stack) - 1]
        if top.left == False:
            top.left = True
            if top.node.left != None:
                stack.append(Node(top.node.left))
        elif top.right == False:
            top.right = True
            if top.node.right != None:
                stack.append(Node(top.node.right))
        elif top.curr == False:
            top.curr = True
            ans.append(top.node.value)
        else:
            stack.pop()
    return ans


def towerOfHanoi1(n, a, b, c):
    if n == 0:
        return
    towerOfHanoi1(n - 1, a, c, b)
    print("Move the disk from : " + a + " to " + b)
    towerOfHanoi1(n - 1, c, b, a)


class hanoiNode:
    def __init__(self, n, a, b, c):
        self.n = n
        self.a = a
        self.b = b
        self.c = c
        self.aTOcWITHb = self.self = self.cTObWITHa = False


def towerOfHanoi2(n, a, b, c):
    stack = [hanoiNode(n, a, b, c)]

    while len(stack) != 0:
        rn = stack[len(stack) - 1]
        if rn.aTOcWITHb:
            rn.aTOcWITHb = True
            if rn.n != 0:
                stack.append(hanoiNode(rn.n - 1, rn.a, rn.c, rn.b))
        elif rn.self:
            rn.self = True
            print("Move the disk from : " + rn.a + " to " + rn.b)
        elif rn.cTObWITHa:
            rn.cTObWITHa = True
            if (rn.n != 0):
                stack.append(hanoiNode(rn.n - 1, rn.c, rn.b, rn.a))
        else:
            stack.pop()
