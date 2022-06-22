from trie import *

# **** https://www.geeksforgeeks.org/print-unique-rows/


def uniqueRows(mat):
    trie = Trie()

    n = len(mat)
    ans = []
    for i in range(0, n):
        trie.insert(mat[i])
        if(trie.getCount(mat[i]) == 1):
            ans.append(mat[i])
    return ans


def notUniqueRows(mat):
    trie = Trie()

    n = len(mat)
    ans = []
    for i in range(0, n):
        trie.insert(mat[i])
        if(trie.getCount(mat[i]) != 1):
            ans.append(mat[i])
    return ans

# ****https://www.geeksforgeeks.org/count-of-strings-whose-prefix-match-with-the-given-string-to-a-given-length-k/


def prefixSearchUptoK(arr, s):
    trie = Trie()
    trie.construct(arr)
    return trie.prefixSearchUptoK(s)

# ***https://www.geeksforgeeks.org/find-all-shortest-unique-prefixes-to-represent-each-word-in-a-given-list/


def shortestUniquePrefix(arr):
    trie = Trie()
    trie.construct(arr)

    res = []
    for s in arr:
        res.append(trie.shortestUniquePrefixSearch(s))
    return res


# *https://www.geeksforgeeks.org/palindrome-pair-in-an-array-of-words-or-strings/
def palindromicPairs(arr):
    trie = Trie()
    trie.insert(arr[0])

    n = len(arr)
    for i in range(1, n):
        res = res or trie.isPalindromePairExist(arr[i])
        trie.insert(arr[i])
    return res

# *** https://www.geeksforgeeks.org/implement-a-phone-directory/


def phoneDirectory(arr, s):
    trie = Trie()
    trie.construct(arr)
    return trie.phoneDirectory(s)


# **** https://www.geeksforgeeks.org/frequent-word-array-strings/
def mostFrequentElement(arr):
    trie = Trie()
    trie.construct(arr)
    return trie.mostFrequentElement(arr)


# *https://leetcode.com/problems/word-search-ii/
#  ? Same as Word Search 2 (LeetCode)
def wordBoggle1(board, arr):
    trie = Trie()
    trie.construct(arr)
    return trie.wordBoggle1(board)


def wordBoggle2(board, arr):
    trie = Trie()
    trie.construct(arr)
    return trie.wordBoggle2(board)

#  ? Only Recursion


def wordBreak(arr, s):
    trie = Trie()
    trie.construct(arr)
    return trie.wordBreakBruteForce(s, 0)


# *https://leetcode.com/problems/replace-words/
def replaceWords(arr, s):
    trie = Trie()
    trie.construct(arr)
    return trie.replacaWords(s)

# *https://leetcode.com/problems/concatenated-words/


def concatenatedWords(arr):
    trie = Trie()
    trie.construct(arr)

    ans = []
    for s in arr:
        if trie.searchIfConcatenated(s):
            ans.append(s)
    return ans

# *https://leetcode.com/problems/longest-word-in-dictionary/


def longestString(arr):
    trie = Trie()
    trie.construct(arr)

    res = ""
    for s in arr:
        if trie.searchIfLongest(str):
            if (res.equals("")):
                res = s
            else:
                if len(res) == len(s):
                    res = res if res > s else s
                elif len(res) < len(s):
                    res = s
    return res
