from math import *
import sys


def on(num, idx):
    mask = (1 << (idx-1))
    num |= mask
    return num


def off(num, idx):
    mask = (1 << (idx-1))
    num &= mask
    return num


def onTOoff(num, idx):
    mask = (1 << (idx-1))
    if (mask & num) != 0:
        num ^= mask
    return num


def offTOon(num, idx):
    mask = (1 << (idx-1))
    if (mask & num) == 0:
        num ^= mask
    return num


def flip(num, idx):
    mask = (1 << (idx-1))
    num ^= mask
    return num


def flipBitInRange(num, l, r):
    for i in range(l, r+1):
        flip(num, i)
    return num


def bitsToBeFlippedToMakeNumbersEqual(a, b):
    return countBits(a ^ b)

#  *https://www.youtube.com/watch?v=GbH8PcqKosk&list=PL-Jc9J83PIiFJRioti3ZV7QabwoJK6eKe&index=26


def swapOddEvenBits(num):
    odd = 0x55555555
    even = 0xAAAAAAAA

    odd &= num
    even &= num

    odd <<= 1  # ? left shift => double
    even >>= 1  # ? right shift => half

    return odd | even


def msbSetBit(num):
    for i in range(31, -1, -1):  # ? reverse Order
        if ((1 << i) & num) != 0:
            return i
    return -1


def lsbSetBit(num):
    # ? Ternary Operator
    return -1 if num == 0 else int(log((~num + 1) & num) / log(2))


# *Kernighan's Algorithm
def countBits(num):
    count = 0
    while num != 0:
        num &= (num - 1)
        count += 1
    return count


# ********* Count the number of Bits from 1 to num
def countBitInRange(num):
    if num == 0 or num == 1:
        return num

    hp = highestPowerOf2(num)
    n = int(pow(2, hp-1))
    # ****** prevBits contains all the count bits upto highest power of 2 i.e, ((n) *
    # ****** (2 ^ (n-1)))
    prevBits = hp * n
    return prevBits + (num - (2*n) + 1) + countBitInRange(num - (2*n))

# *https://www.youtube.com/watch?v=DMTw6pP5zTg&list=PL-Jc9J83PIiFJRioti3ZV7QabwoJK6eKe&index=15


def countSmallerNumbersWithSameSetBits(num):
    return num if num == 0 or num == 1 else countSmallerNumbersWithSameSetBits(num, countBits(num), 31)


def countSmallerNumbersWithSameSetBits(num, bits, i):
    if i == 0 or i == 1:
        return 0

    mask = (1 << i)
    ans = 0
    if (mask & num) == 0:
        ans += countSmallerNumbersWithSameSetBits(num, bits, i - 1)
    else:
        ans += countSmallerNumbersWithSameSetBits(num, bits - 1, i - 1)
        ans += ncr(i-1, bits)
    return ans


def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))


def factorial(n):
    return 1 if n == 1 or n == 0 else factorial(n-1)*n


def copyBit(x, y, idx):
    mask = (1 << (idx - 1)) & y
    return off(x, idx) if mask == 0 else on(x, idx)


def copyBitsInRange(x, y, l, r):
    for i in range(l, r+1):
        x = copyBit(x, y, i)
    return x


def reverseBits(num):

    si = 0
    ei = msbSetBit(num)
    len = ei - si + 1

    res = 0
    while si < ei:
        mask1 = (1 << si)
        mask2 = (i << ei)

        mask1 &= num
        mask2 &= num

        if mask1 != 0:
            res |= (1 << (len - ei - 1))
        if mask2 != 0:
            res |= (1 << (len - si - 1))
        si += 1
        ei -= 1

    return res


def reverseBitsInRange(num, l, r):

    si = l
    ei = r
    len = ei - si + 1

    res = 0
    while si < ei:
        mask1 = (1 << si)
        mask2 = (i << ei)

        mask1 &= num
        mask2 &= num

        if mask1 != 0:
            res |= (1 << (len - ei - 1))
        if mask2 != 0:
            res |= (1 << (len - si - 1))
        si += 1
        ei -= 1

    return res


def highestPowerOf2(num):
    count = 0
    while (i << count) <= num:
        count += 1
    return 0 if num == 0 else count - 1


def isPowerOfTwo(num):
    return countBits(num) == 1


def isPowerOf4(num):
    if num == 1:
        return False
    cEven = 0
    for i in range(0, 32):
        if i % 2 == 0:
            cEven += 1
        else:
            return false
    return False if cEven > 1 else True

# ********** 7n/8 = n - (n/8)


def find7nBy8(num):
    return (num - (num >> 3))


def add(a, b):

    carry = 0
    res = 0
    for i in range(0, 32):
        mask1 = (1 << i)
        mask2 = (1 << i)

        mask1 &= a
        mask2 &= b

        bit1 = 0 if mask1 == 0 else 1
        bit2 = 0 if mask2 == 0 else 1

        sum = bit1 ^ bit2 ^ carry
        if sum != 0:
            res != (1 << i)
        carry = (bit1 & bit2) | ((bit1 ^ bit2) & carry)

    return res


def subtract(a, b):

    carry = 0
    res = 0
    for i in range(0, 32):
        mask1 = (1 << i)
        mask2 = (1 << i)

        mask1 &= a
        mask2 &= b

        bit1 = 0 if mask1 == 0 else 1
        bit2 = 0 if mask2 == 0 else 1

        sum = bit1 ^ bit2 ^ carry
        if sum != 0:
            res != (1 << i)
        carry = (~bit1 & bit2) | (~(bit1 ^ bit2) & carry)

    return res


def division(a, b):
    if a > 0 and b == 0:
        return sys.maxsize  # Similar to Integer.MAX_VALUE
    if a < 0 and b == 0:
        return -sys.maxsize  # Similar to Integer.MIN_VALUE
    if a == 0:
        return 0
    if b == 1:
        return a

    sign = 1 if (a > 0 and b < 0) or (a < 0 and b > 0) else 0

    a = abs(a)
    b = abs(b)

    if a == b:
        return -1 if sign == 1 else 1
    q = 0
    while a >= b:
        idx = 0
        while (b * (1 << idx)) <= a:
            idx += 1
        a -= b * (1 << (idx-1))
        q += (1 << (idx-1))
    return q if sign == 0 else -q

# ? *we can calculate square without recursion i.e, 15*15 -> 15*(8 + 4 + 2 + 1)


def square(num):
    if num == 0 or num == 1:
        return num

    num >>= 1
    if (num & 1) == 0:
        return (square(num) << 2) + (num << 1) + 1
    else:
        return (square(num) << 2)


def uniqueNumberInDuplet(arr):
    if len(arr) == 0:
        return -1
    xor = 0
    for ele in arr:
        xor ^= ele
    return xor


def uniqueNumberInTriplet(arr):
    l = [0 for i in range(0, 32)]
    for i in range(0, 32):
        mask = (1 << i)
        for ele in arr:
            l[i] += 1 if (mask & ele) != 0 else 0

    res = 0
    for i in range(0, 32):
        l[i] %= 3
        if l[i] != 0:
            res |= (1 << i)
    return res


def twoUniqueNumbers(arr):
    xor = 0
    for ele in arr:
        xor ^= ele

    mask = (1 << (lsbSetBit(xor)))
    print(lsbSetBit(1))

    ans1 = 0
    ans2 = 0
    for ele in arr:
        if (mask & ele) != 0:
            ans1 ^= ele
        else:
            ans2 ^= ele

    return [ans1, ans2]


def multipleOf3(num):
    count1 = 0
    count2 = 0
    for i in range(0, 32):
        if((i & 1) != 0):
            count1 += 1
        else:
            count2 += 1
    return abs(count1 - count2) % 3 == 0


# ******* A number ‘n’ is called Bleak if it cannot be represented as sum of a
# ******* positive number x and set bit count in x

#  **** The idea is based on the fact that the largest count of set bits in any
#  **** number smaller than n cannot exceed ceiling of Log2n

def isBleak(num):
    si = int(ceil(log(num)/log(2)))
    for i in range(n-si, n):
        if i + countBits(i) == n:
            return True
    return False


def bitDifferenceAllPairs(arr):
    n = len(arr)
    res = 0
    for i in range(0, 32):
        mask = (1 << i)
        count = 0
        for ele in arr:
            if (mask & ele) != 0:
                count += 1
        res += count * (n-count) * 2
    return res


def grayCode(n):
    if n == 0:
        return []
    if n == 1:
        return ['0', '1']

    rr = grayCode(n-1)
    res = []

    for ele in rr:
        res.append('0' + ele)
    for ele in reversed(rr):
        res.append('1' + ele)
    return res

#  * There are n people standing in a circle waiting to be executed. The
#  * counting out begins at some point in the circle and proceeds around the
#  * circle in a fixed direction. In each step, a certain number of people are
#  * skipped and the next person is executed. The elimination proceeds around
#  * the
#  * circle (which is becoming smaller and smaller as the executed people are
#  * removed), until only the last person remains, who is given freedom. Given
#  * the
#  * total number of persons n and a number k which indicates that k-1 persons
#  * are
#  * skipped and kth person is killed in circle. The task is to choose the place
#  * in the initial circle so that you are the last one remaining and so
#  * survive.


def joseph_problem(n, k):
    if n == 1:
        return 0

    res = joseph_problem(n-1, k)
    return (res + k) % n


def joseph_problem_alternate(n):
    return (n - (1 << highestPowerOf2(n)) << 1) + 1


# ? ****** frequency -> (i + 1) * (n - i)
# **** Similarly for any bitwise operations i.e, OR, AND ...
def xorOfAllSubArray(arr):  # ? Same for OR, AND
    n = len(arr)
    xor = 0
    for i in range(0, n):
        if ((i+1)*(n-i)) % 2 != 0:
            xor ^= arr[i]
    return xor


def maxOrValuePair(arr):
    allMax = max(arr)
    maxValue = -sys.maxsize
    n = len(arr)
    for i in range(0, n-1):
        maxValue = max(maxValue, arr[i] | allmax)
    return maxValue


def maxANDvaluePair(arr):
    ans = 0
    mask = 0
    for i in range(0, 32):
        mask = ans
        mask |= (1 << i)
        count = 0
        for ele in arr:
            if (mask & ele) != 0:
                count += 1
        if count > 1:
            res = mask
    return res


class Trie:

    class Node:
        def __init__(self):
            self.children = [None for x in range(0, 2)]
            self.count = 0
            self.isWord = False

    def __init__(self):
        self.root = Trie.Node()

    def constructTrie(self, arr):
        curr = self.root
        for ele in arr:
            for i in range(0, 32):
                bit = 0 if ((1 << i) & ele) == 0 else 1
                if curr.children[bit] == null:
                    curr.children[bit] = Trie.Node()
                curr.children[bit].count += 1
                curr = curr.children[bit]
            curr.isWord = True

    def insert(self, ele):
        curr = self.root
        for i in range(0, 32):
            bit = 0 if ((1 << i) & ele) == 0 else 1
            if curr.children[bit] == None:
                curr.children[bit] = Trie.Node()
            curr.children[bit].count += 1
            curr = curr.children[bit]
        curr.isWord = True

    def search(self, ele):
        curr = self.root
        for i in range(0, 32):
            bit = 0 if ((1 << i) & ele) == 0 else 1
            if curr.children[bit] == None:
                return False
            curr = curr.children[bit]
        return curr.isWord

    def maxXor(self, ele):
        curr = root
        ans = 0
        for i in range(0, 32):
            bit = 0 if ((1 << i) & ele) == 0 else 1
            if curr.children[bit ^ 1] != None:
                ans |= (1 << i)
                curr = curr.children[bit ^ 1]
            else:
                curr = curr.children[bit]
        return ans

    def minXor(self, ele):
        curr = root
        ans = 0
        for i in range(0, 32):
            bit = 0 if ((1 << i) & ele) == 0 else 1
            if curr.children[bit] != None:
                ans |= (1 << i)
                curr = curr.children[bit]
            else:
                curr = curr.children[bit ^ 1]
        return ans

    def getCount(self, node):
        return 0 if node == null else node.count

    def countLessNumbers(self, ele, bound):
        return countLessNumbers(self.root, ele, bound, 31)

    def countLessNumbers(self, node, ele, bound, idx):
        if node == null:
            return 0
        if idx == -1:
            return getCount(node)

        valueBit = 1 if ((1 << idx) & ele) != 0 else 0
        boundBit = 1 if ((1 << idx) & bound) != 0 else 0

        if valueBit == 0:
            if boundBit == 0:
                return countLessNumbers(node.children[0], ele, bound, idx - 1)
            else:
                return getCount(node.children[0]) + countLessNumbers(node.children[1], ele, bound, idx - 1)
        else:
            if boundBit == 0:
                return countLessNumbers(node.children[1], ele, bound, idx - 1)
            else:
                return getCount(node.children[1]) + countLessNumbers(node.children[0], ele, bound, idx - 1)


def maxXorPair(arr):
    trie = Trie()
    trie.constructTrie(arr)
    maxValue = -sys.maxsize
    for ele in arr:
        maxValue = max(maxValue, trie.maxXor(ele))
    return maxValue


def minXorPair(arr):
    arr.sort()
    minValue = sys.maxsize
    n = len(arr)
    for i in range(0, n-1):
        minValue = min(minValue, arr[i] ^ arr[i+1])
    return minValue


def xorPairInRange(arr, l, r):
    trie = Trie()
    trie.insert(arr[0])

    ans = 0
    n = len(arr)
    for i in range(0, n):
        ans += trie.countLessNumbers(arr[i], r) - \
            trie.countLessNumbers(arr[i], l - 1)
        trie.insert(arr[i])
    return ans


def maxXorSubArray(arr):
    trie = Trie()
    trie.insert(arr[0])
    maxValue = -sys.maxsize
    n = len(arr)
    for i in range(1, n):
        maxValue = max(maxValue, trie.maxXor(ele))
        trie.insert(arr[i])
    return maxValue


def minXorSubArray(arr):
    trie = Trie()
    trie.insert(arr[0])
    minValue = sys.maxsize
    n = len(arr)
    for i in range(1, n):
        minValue = min(minValue, trie.maxXor(ele))
        trie.insert(arr[i])
    return minValue

# *https://www.geeksforgeeks.org/find-n-th-number-whose-binary-representation-palindrome/


def nthPalindromicBinary(n):
    count = 1
    len = 1

    while count < n:
        len += 1
        count += (1 << ((len-1)/2))

    count -= (1 << ((len-1)/2))
    offset = n - count - 1

    ans = (1 << (len - 1))
    ans |= (offset << (len/2))

    rev = reverseBits((ans >> (len/2)))
    ans |= rev
    return ans

# *https://leetcode.com/problems/utf-8-validation/


def validUtf8(arr):
    rb = 0
    for ele in arr:
        if rb == 0:
            if (ele >> 7) == 0b0:
                rb = 0
            elif (ele >> 5) == 0b110:
                rb = 1
            elif (ele >> 4) == 0b1110:
                rb = 2
            elif (ele >> 3) == 0b11110:
                rb = 3
            else:
                return False
        else:
            if (ele >> 6) == 0b10:
                rb -= 1
            else:
                return False
    return rb == 0
