from queue import *


class Trie:  # For Binary Numeric Values

    class Node:
        def __init__(self):
            self.children = [None for x in range(0, 2)]
            self.count = 0
            self.isWord = False

    def __init__(self):
        self.root = Trie.Node()

    def constructTrie(self, mat):
        curr = self.root
        for arr in mat:
            for ele in arr:
                if curr.children[ele] == None:
                    curr.children[ele] = Trie.Node()
                curr.children[ele].count += 1
                curr = curr.children[ele]
            curr.isWord = True

    def insert(self, arr):
        curr = self.root
        for ele in arr:
            if curr.children[ele] == None:
                curr.children[ele] = Trie.Node()
            curr.children[ele].count += 1
            curr = curr.children[ele]
        curr.isWord = True

    def search(self, arr):
        curr = self.root
        for ele in arr:
            if curr.children[ele] == None:
                return False
            curr = curr.children[ele]
        return curr.isWord

    def getCount(self, arr):
        curr = self.root
        for ele in arr:
            if curr.children[ele] == None:
                return -1
            curr = curr.children[ele]
        return curr.count


# **** Standard Trie with delete
class Trie1:
    class Node:
        def __init__(self):
            self.children = [None for i in range(0, 27)]
            self.isWord = False
            self.word = ""
            self.prefixCount = 0
            self.pq = PriorityQueue()

    def getMatrix(self, n, m):
        mat = []
        for i in range(0, n):
            mat[i] = [0 for x in range(0, m)]
        return mat

    def __init__(self):
        self.root = Node()

    def isNodeEmpty(node):
        if node == None:
            return True
        for i in range(0, 27):
            if node.children[i] != None:
                return False
        return True

    def constructTrie(self, arr):
        curr = self.root
        for s in arr:
            for ch in s:
                if curr.children[ord(ch) - ord('a')] == null:
                    curr.children[ord(ch) - ord('a')] = Trie1.Node()
                curr.children[ord(ch) - ord('a')].prefixCount += 1
                curr.children[ord(ch) - ord('a')].pq.put(s)
                curr = curr.children[ord(ch) - ord('a')]
            curr.isWord = True
            curr.word = s

    def insert(self, s):
        curr = self.root
        for ch in s:
            if curr.children[ord(ch) - ord('a')] == null:
                curr.children[ord(ch) - ord('a')] = Trie1.Node()
            curr.children[ord(ch) - ord('a')].prefixCount += 1
            curr.children[ord(ch) - ord('a')].pq.put(s)
            curr = curr.children[ord(ch) - ord('a')]
        curr.isWord = True
        curr.word = s

    def getCount(self, s):
        curr = self.root
        for ch in s:
            if curr.children[ord(ch) - ord('a')] == null:
                return -1
            curr = curr.children[ord(ch) - ord('a')]
        return curr.prefixCount

    def search(self, ele):
        return self.__search(self.root, ele)

    def __search(self, curr, ele):
        curr = self.root
        for ch in s:
            if curr.children[ord(ch) - ord('a')] == null:
                return False
            curr = curr.children[ord(ch) - ord('a')]
        return curr.isWord

    def searchLikeGoogle(self, curr, s, idx):
        if idx == len(s):
            return True

        res = false
        if s[idx] == '.':
            for i in range(0, 27):
                if curr.children[i] != None:
                    res = res or self.searchLikeGoogle(
                        curr.children[i], s, idx+1)
        else:
            res = False if curr.children[s[idx] - 'a'] == None else res or self.searchLikeGoogle(
                curr.children[i], s, idx+1)
        return res

    def prefixSearch(self, s):
        curr = self.root
        n = len(s)
        for i in range(0, n+1):
            idx = s[i] - 'a'
            if curr.isWord:
                return curr.word
            if curr.children[idx] == None:
                return curr.word if curr.isWord else s
            curr = curr.children[idx]
        return curr.word if curr.isWord else s

    def prefixSearchUptoK(self, s, k):
        curr = self.root
        n = len(s)
        n = n if k >= n else k
        for i in range(0, n+1):
            idx = s[i] - 'a'
            if curr.children[idx] == None:
                return -1
            curr = curr.children[idx]
        return curr.prefixCount

    def shortestUniquePrefixSearch(self, s):
        curr = self.root
        n = len(s)
        for i in range(0, n):
            idx = s[i] - 'a'
            if curr.children[idx] == None:
                return ""
            if curr.children[idx].prefixCount == 1:
                return s[0:i+1]
            curr = curr.children[idx]
        return ""

    def preOrder(self, curr, idx):
        if curr == None:
            return
        if curr.isWord:
            print(curr.word)
        for i in range(0, 27):
            self.preOrder(curr.children[i], i)

    def postOrder(self, curr, idx):
        if curr == None:
            return
        for i in range(0, 27):
            self.postOrder(curr.children[i], i)
        if curr.isWord:
            print(curr.word)

    def delete(self, s):
        self.root = self.delete(self.root, s, 0)

    def delete(self, curr, s, idx):
        if idx == len(s):
            if curr.isWord:
                curr.isWord = False

            curr.pq.pop(s)
            curr.prefixCount -= 1

            if isNodeEmpty(curr):
                curr = None
            return curr

        ch = s[idx] - 'a'
        curr.children[ch] = self.delete(curr.children[ch], s, idx+1)

        curr.pq.pop(s)
        curr.prefixCount -= 1

        if isNodeEmpty(curr) and curr.isWord == False:
            curr = None
        return curr

    def isPalindromePairExist(self, s):
        res = self.search(s[::-1]) or self.search(s[-1:0:-1])
        for i in range(0, 27):
            if self.root.children[i] != None:
                res = res or self.search(chr(i + int('a')) + s)
        return res

    def phoneDirectory(self, s):
        res = []
        curr = self.root
        for ch in s:
            idx = ord(ch) - ord('a')
            if curr.children[idx] == None:
                break
            res.append(curr.children[idx].pq.queue)
            curr = curr.children[idx]
        return res

    def mostFrequentElement(arr):
        maxCount = 0
        res = ''
        for s in arr:
            count = getCount(s)
            if count > maxCount:
                count = maxCount
                res = s
        return res

    dir = [[0, 1], [1, 0], [-1, 0], [0, -1],
           [1, 1], [-1, 1], [-1, -1], [1, -1]]
    ans = []

    def dfs1(self, curr, board, i, j, vis):
        if curr.isWord:
            cls.ans.append(curr.word)

        vis[i][j] = True
        for d in range(0, len(dir)):
            x = i + dir[d][0]
            y = j + dir[d][1]
            if(x >= 0 and y >= 0 and x < len(board) and y < len(board[0]) and vis[x][y] == False and curr.children[board[x][y] - 'a'] != None):
                self.dfs1(
                    curr.children[ord(board[x][y]) - ord('a')], board, x, y, vis)
        vis[i][j] = False

    def wordBoggle1(self, board):
        cls.ans.clear()

        n = len(board)
        m = len(board[0])
        for i in range(0, n):
            for j in range(0, m):
                if self.root.children[ord(board[i][j]) - ord('a')] != None:
                    self.dfs1(self.root, board, i, j, getMatrix(n, m))

    def dfs2(self, curr, board, i, j, vis):
        if curr.isWord:
            cls.ans.append(curr.word)
            self.delete(curr.word)

        vis[i][j] = True
        for d in range(0, len(dir)):
            x = i + dir[d][0]
            y = j + dir[d][1]
            if(x >= 0 and y >= 0 and x < len(board) and y < len(board[0]) and vis[x][y] == False and curr.children[board[x][y] - 'a'] != None):
                self.dfs2(
                    curr.children[ord(board[x][y]) - ord('a')], board, x, y, vis)
        vis[i][j] = False

    def wordBoggle2(self, board):
        cls.ans.clear()

        n = len(board)
        m = len(board[0])
        for i in range(0, n):
            for j in range(0, m):
                if self.root.children[ord(board[i][j]) - ord('a')] != None:
                    self.dfs2(self.root, board, i, j, getMatrix(n, m))

    def wordBreakBruteForce(self, s, idx):
        if idx == len(s):
            return True

        res = False
        for i in range(idx+1, len(s) + 1):
            if self.search(s[idx:i+1]):
                res = res or self.wordBreakBruteForce(s, i)
        return res

    def replaceWords(self, s):
        arr = s.split(" ")

        ans = ""
        for string in arr:
            ans += self.prefixSearch(string) + " "
        return ans

    def searchIfConcatenated(self, s, idx, subStringNumber):
        if idx == len(s):
            return subStringNumber > 1

        curr = self.root
        res = False
        for i in range(idx, len(s)):
            ch = s[i]
            if curr.children[ord(ch) - ord('a')] == None:
                return False
            if curr.children[ord(ch) - ord('a')].isWord:
                res = res or self.searchConcatenatedWords(
                    s, i + 1, subStringNumber + 1)
            if res:
                return res
            curr = curr.children[ord(ch) - ord('a')]
        return res

    def longestString(self, s):
        curr = self.root
        for ch in s:
            if curr.children[ord(ch) - ord('a')] == None or curr.children[ord(ch) - ord('a')].isWord == False:
                return False
            curr = curr.children[ord(ch) - ord('a')]
        return curr.isWord

# *https://leetcode.com/problems/map-sum-pairs/


class MapSum:

    class Node:
        def __init__(self):
            self.children = [None for i in range(0, 27)]
            self.valueSum = 0

    def __init__(self):
        self.root = MapSum.Node()
        self.map = {}

    def insert(self, s, value):
        oldValue = self.map[s] if s in self.map.keys() else 0
        self.map[s] = value

        curr = self.root
        for ch in s:
            if curr.children[ord(ch) - ord('a')] == None:
                curr.children[ord(ch) - ord('a')] = MapSum.Node()
            curr.valueSum += (value - oldValue)
            curr = curr.children[ord(ch) - ord('a')]
        curr.valueSum += (value - oldValue)

    def sum(self, s):
        curr = self.root
        for ch in s:
            if curr.children[ord(ch) - ord('a')] == None:
                return 0
            curr = curr.children[ord(ch) - ord('a')]
        return curr.valueSum


# *https: // leetcode.com/problems/stream-of-characters/
class StreamChecker:

    class Node:
        def __init__(self):
            self.children = [None for i in range(0, 27)]
            self.isWord = False

    def __init__(self, words):
        self.root = StreamChecker.Node()
        self.insert(words)
        self.ans = ""

    def insert(self, arr):
        for s in arr:
            curr = self.root
            for ch in s[::-1]:
                if curr.children[ord(ch) - ord('a')] == None:
                    curr.children[ord(ch) - ord('a')] = StreamChecker.Node()
                curr = curr.children[ord(ch) - ord('a')]
            curr.isWord = True

    def search(self, s):
        curr = self.root
        for ch in s[::-1]:
            if curr.children[ord(ch) - ord('a')] == None:
                return False
            if curr.children[ord(ch) - ord('a')].isWord:
                return True
            curr = curr.children[ord(ch) - ord('a')]
        return curr.isWord

    def query(self, s):
        self.ans += str(s)
        return self.search(self.ans)
