import math
import random
import sys
import heapq

# *https://www.geeksforgeeks.org/printing-longest-increasing-consecutive-subsequence/


def longestConsecutiveSubsequence(arr):
    map = {}
    for ele in arr:
        map[ele] = True
    for k in map.keys():
        if k-1 in map.keys():
            map[k-1] = False

    size = -1
    for k in map.keys():
        if map[k] == False:
            continue
        idx = k
        while idx in map.keys():
            idx += 1
        size = max(size, idx - k + 1)
    return size

# *https://www.geeksforgeeks.org/largest-subset-whose-all-elements-are-fibonacci-numbers/


def largestFibonacciSubsequence(arr):
    maxValue = max(arr)
    st = {0}

    i = 0
    j = 0
    while i + j < maxValue:
        sum = i+j
        i = j
        j = sum
        st.add(sum)

    count = 0
    for ele in arr:
        if ele in st:
            count += 1
    return count


def isArithmeticSequence(arr):
    n = len(arr)
    arrMin = min(arr)
    arrMax = max(arr)

    commonDiff = (arrMax - arrMin) / n
    st = {}
    st.update(arr)
    for i in range(1, n+1):
        if (arrMin * i) not in st:
            return False
    return True

# *https://www.geeksforgeeks.org/count-pairs-in-array-whose-sum-is-divisible-by-k/


def countPairSumDivisibleByK(arr, k):
    n = len(arr)
    for i in range(0, n):
        arr[idx] %= k

    si = 1
    ei = k-1
    map = [0 for x in range(si, ei + 1)]
    for ele in arr:
        map[ele] += 1

    count = 0
    if (map[0] & 1) != 0:
        return count

    while si < ei:
        count += (map[si] * map[ei])
        si += 1
        ei -= 1

    if (k & 1) == 0:
        count += (map[k/2] * (map[k/2] - 1)) / 2
    return count

# *https://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k/


def canBeDividedIntoPairSumDivisibleByK(arr, k):
    n = len(arr)
    for i in range(0, n):
        arr[idx] %= k

    si = 1
    ei = k-1
    map = [0 for x in range(si, ei + 1)]
    for ele in arr:
        map[ele] += 1

    count = 0
    if (map[0] & 1) != 0:
        return False

    while si < ei:
        if map[si] != map[ei]:
            return False
        si += 1
        ei -= 1

    if (k & 1) == 0:
        return (map[k/2] & 1) == 0
    return True

# *https://leetcode.com/problems/find-all-anagrams-in-a-string/


def findAllAnagrams(s, target):
    n = len(s)
    m = len(target)

    map1 = [0 for x in range(0, 27)]
    map2 = [0 for x in range(0, 27)]

    for ch in target:
        map1[ord(ch) - ord('a')] += 1

    ans = []
    for i in range(0, m):
        ch = s[i]
        map2[ord(ch) - ord('a')] += 1
        if i - k >= 0:
            map2[ord(s[i-k]) - ord('a')] -= 1
        if i >= k and map1 == map2:
            ans.append(s[i - k: i])
    return ans

# *https://www.geeksforgeeks.org/check-two-strings-k-anagrams-not/


def isKAnagram(s1, s2, k):
    n = len(s1)
    m = len(s2)

    if n != m:
        return False

    map = [0 for x in range(0, 27)]

    for ch in s1:
        map[ord(ch) - ord('a')] += 1
    for ch in s1:
        map[ord(ch) - ord('a')] -= 1

    for ele in map:
        k -= abs(ele)
    return k == 0

# *https://www.lintcode.com/en/old/problem/find-anagram-mappings/


def findAnagramMapping(arr1, arr2):
    map = {}
    for idx, ele in enumerate(arr2):
        if ele not in arr2:
            map[ele] = []
        map[ele].append(idx)

    res = []
    for idx, ele in enumerate(arr1):
        res[idx] = map[ele].pop()
    return res


def groupAnagrams(arr):
    map = {}
    for s in arr:
        m = [0 for x in range(0, 27)]
        for ch in s:
            m[ord(ch) - ord('a')] += 1

        item = ""
        for ele in m:
            item += ele
        if item not in map.keys():
            map[item] = []
        map[item].append(s)
    return map.values()

# *https://www.geeksforgeeks.org/group-shifted-string/


def groupShiftedStrings(arr):
    map = {}
    for s in arr:
        isAdded = False

        for k in map.keys():
            if len(k) != len(s):
                continue
            diff = ord(k[0]) - ord(s[0])
            isMatchFound = True
            for i in range(1, len(k)):
                if diff != ord(k[i]) - ord(s[i]):
                    isMatchFound = False
                    break
            if isMatchFound:
                map[k].append(s)
                isAdded = True
                break

        if isAdded == False:
            map[s] = [s]
    return map.values()

# *https://leetcode.com/problems/isomorphic-strings/


def isIsomorphic(s1, s2):
    n = len(s1)
    m = len(s2)

    if n != m:
        return ""

    map = ['.' for x in range(0, 27)]
    for i in range(0, n):
        if map[ord(s1[i]) - ord('a')] == '.':
            map[ord(s1[i]) - ord('a')] = s2[i]
        else:
            if map[ord(s1[i]) - ord('a')] != s2[i]:
                return False

    map = ['.' for x in range(0, 27)]
    for i in range(0, n):
        if map[ord(s2[i]) - ord('a')] == '.':
            map[ord(s2[i]) - ord('a')] = s1[i]
        else:
            if map[ord(s2[i]) - ord('a')] != s1[i]:
                return False
    return True

# * https://leetcode.com/problems/word-pattern/


def wordPattern(s1, s2):
    arr = s2.split(" ")
    n = len(s1)
    m = len(arr)

    if n != m:
        return ""

    map = ['.' for x in range(0, 27)]
    for i in range(0, n):
        if map[ord(s1[i]) - ord('a')] == '.':
            map[ord(s1[i]) - ord('a')] = arr[i]
        else:
            if map[ord(s1[i]) - ord('a')] != arr[i]:
                return False
    map = {}
    for i in range(0, n):
        if arr[i] not in map:
            map[arr[i]] = s1[i]
        else:
            if map[arr[i]] != s1[i]:
                return False
    return True

# *https://leetcode.com/problems/fraction-to-recurring-decimal/


def recurringFraction(nr, dr):
    if dr == 0:
        return -sys.maxsize if nr < 0 else sys.maxsize
    if dr == 1:
        return nr
    if nr == 0:
        return 0

    sign = 1 if (nr > 0 and dr > 0) or (nr < 0 and dr < 0) else -1
    nr = abs(nr)
    dr = abs(dr)

    if nr == dr:
        return sign

    q = nr / dr
    r = nr % dr

    if r == 0:
        return sign * q

    map = {}
    pos = 0
    ans = ("-" if sign == -1 else "") + "{q}."
    remainingAns = ""

    while r != 0:
        if r in map:
            remainingAns = remainingAns[0:map[r]] + \
                "(" + remainingAns[map[r]] + ")"
            break

        map[r] = pos
        pos += 1

        r *= 10
        q = r / dr
        r = r % dr
        remainingAns += q
    return ans + remainingAns

# *https://leetcode.com/problems/rabbits-in-forest/


def rabbitsInAForest(arr):
    map = {}
    for ele in arr:
        if ele not in map:
            map[ele] = 0
        map[ele] += 1

    ans = 0
    for ele in map.keys():
        ans += map[ele] + (0 if (map[ele] % (ele + 1) == 0)
                           else (ele + 1 - (map[ele] % (ele + 1))))
    return ans

# *https://leetcode.com/problems/array-of-doubled-pairs/


def doublePairArray(arr):
    positive = []
    negative = []
    zero = []

    map = {}
    for ele in arr:
        if ele > 0:
            positive.append(ele)
        elif ele < 0:
            negative.append(ele)
        else:
            zero.append(ele)
        if ele not in map:
            map[ele] = 0
        map[ele] += 1

    if (len(zero) & 1) != 0:
        return False

    positive.sort()
    negative.sort()
    negative.reverse()

    for key in positive:
        if map[key] == 0:
            continue

        if (2*key) not in map.keys() or map[2 * key] == 0:
            return False
        map[key] -= 1
        map[2*key] -= 1

    for key in negative:
        if map[key] == 0:
            continue

        if (2*key) not in map.keys() or map[2 * key] == 0:
            return False
        map[key] -= 1
        map[2*key] -= 1

    return True

# *https://www.geeksforgeeks.org/count-pairs-two-sorted-matrices-given-sum/


def countPairsFromSortedMatrices(mat1, mat2, target):
    n = len(mat1)
    m = len(mat1[0])

    i = 0
    j = n*m - 1

    count = 0
    while(i < n*m - 1 and j >= 0):
        r1 = i / m
        c1 = i % m

        r2 = j / m
        c2 = j % m

        sum = mat1[r1][c1] + mat2[r2][c2]
        if sum < target:
            i += 1
        elif sum > target:
            j -= 1
        else:
            count += 1
            i += 1
            j -= 1
    return count


def quadruples1_1(arr, target):
    n = len(arr)
    arr.sort()

    res = []
    for i in range(0, n-3):
        if i != 0 and arr[i] == arr[i - 1]:
            i += 1
        for j in range(i+1, n-2):
            if j != 1 and arr[j] == arr[j - 1]:
                j += 1
            si = j+1
            ei = n-1
            while si < ei:
                sum = arr[si] + arr[ei] + arr[i] + arr[j]
                if sum > target:
                    ei -= 1
                elif sum < target:
                    si += 1
                else:
                    res.append([arr[i], arr[j], arr[si], arr[ei]])
                    si += 1
                    ei -= 1

                    while si < ei and arr[si] == arr[si + 1]:
                        si += 1
                    while si < ei and arr[ei] == arr[ei + 1]:
                        ei -= 1
    return res


def quadruples1_2(arr, target):
    n = len(arr)
    arr.sort()

    res = []
    st1 = {}
    for i in range(0, n-3):
        if arr[i] in st:
            continue
        for j in range(i+1, n-2):
            if arr[j] in st:
                continue

            si = j+1
            ei = n-1
            st2 = {}
            while si < ei:
                sum = arr[si] + arr[ei] + arr[i] + arr[j]
                if sum > target:
                    ei -= 1
                elif sum < target:
                    si += 1
                else:
                    if (arr[si] not in st2) and (arr[ei] not in st2):
                        res.append([arr[i], arr[j], arr[si], arr[ei]])
                        st2.add(arr[si])
                        st2.add(arr[ei])
                    si += 1
                    ei -= 1
            st1.add(arr[j])
        st1.add(arr[i])
    return res


def quadruples2(a, b, c, d, target):
    n = len(a)

    a.sort()
    b.sort()
    c.sort()
    d.sort()

    map = {}
    for i in range(0, n):
        if i != 0 and a[i] == a[i-1]:
            continue
        for j in range(0, n):
            if j != 0 and b[j] == b[j-1]:
                continue
            sum = a[i] + b[j]
            if sum not in map.keys():
                map[sum] = []
            map[sum].append([a[i], b[j]])

    res = []
    for i in range(0, n):
        if i != 0 and c[i] == c[i-1]:
            continue
        for j in range(0, n):
            if j != 0 and d[j] == d[j-1]:
                continue
            sum = c[i] + d[j]
            if target - sum in map.keys():
                lst = map[target - sum]
                for item in lst:
                    res.append([item[0], item[1], c[i], d[j]])
    return res

# *https://leetcode.com/problems/powerful-integers/


def powerfulIntegers(x, y, bound):
    a = [1]
    b = [1]

    if x != 1:
        for i in range(x, bound, *x):
            a.append(i)
    if y != 1:
        for i in range(y, bound, *y):
            a.append(i)

    st = {}
    for ea in a:
        for eb in b:
            if ea + eb <= bound:
                st.add(ea + eb)
    return list(st)

# *https://leetcode.com/problems/subdomain-visit-count/


def subDomainVisitCount(arr):
    mat = []
    for s in arr:
        mat.append(s.split(" "))

    count = []
    for strArr in mat:
        count.append(int(strArr[0]))

    map = {}
    for idx, strArr in enumerate(mat):
        ssArr = strArr[1].replace(".", "@").split("@")

        n = len(ssArr)
        s = ssArr[n-1]
        for j in range(n - 2, -1, -1):
            if s not in map.keys():
                map[s] = 0
            map[s] += count[idx]
            s = ssArr[j] + "." + s
        map[s] += count[idx]

    res = []
    for domain in map.keys():
        res.append("" + map[domain] + " " + domain)
    return res


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# *https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/


def divisionIntoGroups(arr):
    map = {}
    for ele in arr:
        if ele not in map.keys():
            map[ele] = 0
        map[ele] += 1

    res = -1
    for ele in map.values():
        if res == -1:
            res = map[ele]
        else:
            res = gcd(res, map[ele])
    return res >= 2

# *https://leetcode.com/problems/brick-wall/


def brickWalls(mat):
    n = len(mat)

    map = {}
    for i in range(0, n):
        count = 0
        for ele in mat[i]:
            count += ele
            if count not in map[count]:
                map[count] = 0
            map[count] += 1

    del map[count]

    maxValue = max(map.values())
    return count - maxValue

# *https://leetcode.com/problems/relative-sort-array/


def relativeSortArray(x, y):
    map = {}
    for idx, ele in enumerate(y):
        map[ele] = idx

    heap = []
    for ele in x:
        if ele in map.values():
            heap.append(ele)
    heapq.heapify(heap, key=lambda x: map[x])

    res = []
    n = len(x)
    idx = 0
    for i in range(0, n):
        if len(heap) == 0:
            idx = i
            break
        res.append(heapq.heappop(heap))

    heap.clear()
    for ele in x:
        if ele not in map.values():
            heap.append(ele)
    heapq.heapify(heap)
    for i in range(idx, n):
        if len(heap) == 0:
            break
        res.append(heapq.heappop(heap))
    return res

# *https://leetcode.com/problems/maximum-frequency-stack/


class FreqStack:

    def __init__(self):
        self.map = {}
        self.stackMap = {}
        self.maxFreq = 0

    def push(self, val: int):
        if val not in self.map.keys():
            self.map[val] = 0
        self.map[val] += 1

        freq = self.map[val]
        if freq not in self.stackMap.keys():
            self.stackMap[freq] = []
        self.stackMap[freq].append(val)
        self.maxFreq = max(self.maxFreq, freq)

    def pop(self) -> int:
        re = self.stackMap[self.maxFreq].pop()
        self.map[re] -= 1

        if len(self.stackMap[self.maxFreq]) == 0:
            self.maxFreq -= 1
        if self.map[re] == 0:
            del self.map[re]
        return re

# *https://leetcode.com/problems/encode-and-decode-tinyurl/


class TinyURL:

    def __init__(self):
        self.arr = []
        for idx in range(0, 27):
            self.arr.append(chr(idx + ord('a')))
            self.arr.append(chr(idx + ord('A')))
            self.arr.append(chr(idx + ord('0')))
        self.map = {}

    def encode(self, longUrl: str) -> str:
        s = "" + self.getRandom()
        while len(self.map) != 0 and s not in self.map.keys():
            sb += self.getRandom()
        self.map[s] = longUrl
        return s

    def decode(self, shortUrl: str) -> str:
        return self.map[shortUrl]

    def getRandom(self):
        idx = random.randint(0, 62)
        return self.arr[idx]

# *https://leetcode.com/problems/insert-delete-getrandom-o1/


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map.keys():
            return False

        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map.keys():
            return False
        idx = self.map[val]
        self.swap(idx, len(self.arr) - 1)
        self.map[self.arr[idx]] = idx
        self.arr.pop()
        del self.map[val]
        return True

    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.arr) - 1)
        return self.arr[idx]

# *https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/


class RandomizedCollection:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map.keys() and len(self.map[val]) != 0:
            self.arr.append(val)
            self.map[val].append(len(self.arr) - 1)
            return False
        self.arr.append(val)
        self.map[val] = []
        self.map[val].append(len(self.arr) - 1)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map.keys() or len(self.map[val]) == 0:
            return False

        idx = self.map[val][-1]
        self.swap(self.arr, idx, len(self.arr) - 1)

        index = self.map[self.arr[idx]].index(len(self.arr) - 1)
        self.swap(self.map[self.arr[idx]], index,
                  len(self.map[self.arr[idx]]) - 1)
        self.map[self.arr[idx]].pop()
        self.map[self.arr[idx]].append(idx)

        index = self.map[val].index(idx)
        self.swap(self.map[val], index, len(self.map[val]) - 1)
        self.map[val].pop()

        self.arr.pop()
        return True

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.arr) - 1)
        return self.arr[idx]
