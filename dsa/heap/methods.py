import heapq
import sys


def kthLargest(arr, k):
    if k < 1 or k > n:
        return -1

    for ele in arr:
        heapq.heappush(heap, ele)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)


def kthSmallest(arr, k):
    if k < 1 or k > n:
        return -1

    for ele in arr:
        heapq.heappush(heap, -1 * ele)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)


def kthLargestFromStream(arr):
    n = len(arr)

    heap = []
    for i in range(0, k):
        heapq.heappush(heap, arr[i])

    res = []
    for i in range(k, n):
        res.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])
    return res


def kthSmallestFromStream(arr):
    n = len(arr)

    heap = []
    for i in range(0, k):
        heapq.heappush(heap, -1 * arr[i])

    res = []
    for i in range(k, n):
        res.append(-1 * heapq.heappop(heap))
        heapq.heappush(heap, -1 * arr[i])
    return res


def nearlyKSortedArray(arr):
    n = len(arr)

    heap = []
    for i in range(0, k):
        heapq.heappush(heap, -1 * arr[i])

    idx = 0
    for i in range(k, n):
        arr[idx] = -1 * heapq.heappop(heap)
        heapq.heappush(heap, -1 * arr[i])
        idx += 1

    while len(heap) != 0:
        arr[idx] = -1 * heapq.heappop(heap)
        idx += 1
    return arr


def panCakeSorting(arr):
    n = len(arr)
    for i in range(0, n):
        l = [arr[x] for x in range(0, n - i - 1)]
        maxIdx = l.index(max(l)) + 1
        l = [arr[x] for x in range(0, maxIdx)].reverse()
        for x in range(0, maxIdx):
            arr[x] = l[x]
        l = [arr[x] for x in range(0, n - i - 1)].reverse()
        for x in range(0, n - i - 1):
            arr[x] = l[x]
    return arr


def medianInStream(arr):
    minHeap = []
    maxHeap = []

    res = []
    for idx, ele in enumerate(arr):
        if len(maxHeap) == 0:
            heapq.heappush(maxHeap, ele)
        elif len(minHeap) == 0 or len(maxHeap) == len(minHeap):
            if maxHeap.peek() < ele:
                heapq.heappush(maxHeap, ele)
                heapq.heappush(minHeap, heapq.heappop(maxHeap))
            else:
                heapq.heappush(minHeap, ele)
        else:
            if maxHeap.peek() < ele:
                heapq.heappush(maxHeap, ele)
                heapq.heappush(minHeap, heapq.heappop(maxHeap))
                heapq.heappush(minHeap, heapq.heappop(maxHeap))
            else:
                heapq.heappush(minHeap, ele)
        res[idx] = (self.minHeap.peek() + self.maxHeap.peek()) / \
            2 if self.minHeap.size() == self.maxHeap.size() else self.maxHeap.peek()
    return res

# *** Huffman Coding


def mergeRopeCuts(arr):
    heap = []
    for ele in arr:
        heapq.heappush(heap, ele)

    ans = 0
    while len(heap) > 1:
        sum = heapq.heappop(heap) + heapq.heappop(heap)
        ans += sum
        heapq.heappush(heap, sum)
    return ans + heapq.heappop(heap)


def mergeKSortedArrays(mat):
    k = len(mat)
    n = len(mat[0])

    heap = []
    for i in range(0, k):
        heapq.heappush(heap, [mat[i][0], i, 0])

    res = []
    while len(heap) != 0:
        item = heapq.heappop(heap)
        res.append(item[0])

        r = item[1]
        c = item[2]

        if c + 1 < n:
            heapq.heappush(
                heap, [mat[r][c + 1], r, c + 1])
    return res

# **https://www.geeksforgeeks.org/find-smallest-range-containing-elements-from-k-lists/


def minRange(mat):
    k = len(mat)
    n = len(mat[0])

    heap = []
    for i in range(0, k):
        heapq.heappush(heap, [mat[i][0], i, 0])

    currMin = min(heap)
    currMax = max(heap)

    diff = currMax - currMin
    ans = diff
    while len(heap) != 0:
        item = heapq.heappop(heap)
        r = item[1]
        c = item[2]
        if c + 1 < n:
            heapq.heappush(
                heap, [mat[r][c + 1], r, c + 1])

        currMin = min(heap)
        currMax = max(heap)
        diff = currMax - currMin
        ans = min(ans, diff)
    return ans


def kthLargestElementInSortedMatrix(mat, k):
    n = len(mat)
    m = len(mat[0])

    heap = []
    for i in range(0, n):
        heapq.heappush(heap, [mat[i][0], i, 0])

    while len(heap) != 0 and k > 0:
        item = heapq.heappop(heap)
        k -= 1

        r = item[1]
        c = item[2]
        if c + 1 < n:
            heapq.heappush(
                heap, [mat[r][c + 1], r, c + 1])
    return heapq.heappop(heap)

# *https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/


def kthSmallestElementInSortedMatrix(mat, k):
    n = len(mat)
    m = len(mat[0])

    heap = []
    for i in range(0, n):
        heapq.heappush(heap, [-1 * mat[i][0], i, 0])

    while len(heap) != 0 and k > 0:
        item = heapq.heappop(heap)
        k -= 1

        r = item[1]
        c = item[2]
        if c + 1 < n:
            heapq.heappush(
                heap, [-1 * mat[r][c + 1], r, c + 1])
    return heapq.heappop(heap)


def kthLargestSubArraySum(arr):
    if k < 0 or k > (n*n / 2):
        return -1

    n = len(arr)
    heap = []
    for i in range(0, n):
        sum = 0
        for j in range(idx, n):
            sum += arr[j]
            heapq.heappush(heap, sum)

            if len(heap) > k:
                heapq.heappop(heap)
    return heapq.heappop(heap)


def kthSmallestSubArraySum(arr):
    if k < 0 or k > (n*n / 2):
        return -1

    n = len(arr)
    heap = []
    for i in range(0, n):
        sum = 0
        for j in range(idx, n):
            sum += arr[j]
            heapq.heappush(heap, -1 * sum)

            if len(heap) > k:
                heapq.heappop(heap)
    return heapq.heappop(heap)

# **** https://leetcode.com/problems/reorganize-string/


def rearrangeString(s):
    map = {}
    for ch in s:
        if ch not in map.keys():
            map[ch] = 0
        map[ch] += 1

    heap = []
    for ch in s:
        heap.append([map[ch], ch])
    heapq.heapify(heap)

    ans = ""
    while len(heap) > 1:
        item1 = heapq.heappop(heap)
        item2 = heapq.heappop(heap)

        ans += item1[1] + item2[1]
        item1[0] -= 1
        item1[1] -= 1

        if item1[0] != 0:
            heapq.heappush(heap, item1)
        if item2[0] != 0:
            heapq.heappush(heap, item2)
    last = heapq.heappop(heap)

    return "" if last[0] != 1 else ans + last[1]

# ***** https://practice.geeksforgeeks.org/problems/minimum-sum4058/1


def minSum(arr):
    heap = []
    for ele in arr:
        heapq.heappush(heap, ele)

    num1 = 0
    num2 = 0
    idx = 0
    while len(heap) != 0:
        item = heapq.heappop(heap)
        if (idx & 1) == 0:
            num1 *= 10
            num1 += item
        else:
            num2 *= 10
            num2 += item
        idx += 1
    return num1 + num2


def inorder(node, values):
    if node == None:
        return

    inorder(node.left, values)
    values.append(node.value)
    inorder(node.right, values)


index = 0


def preorder(node, values):
    if node == None:
        return

    node.value = values[index]
    index += 1
    preorder(node.left, values)
    preorder(node.right, values)


def BSTtoMinHeap(root):
    values = []
    inorder(root, values)
    preorder(root, values)


def kFarestElements(arr, target):
    heap = []
    for ele in arr:
        heapq.heappush(heap, [abs(ele - target), ele])
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

# *https://leetcode.com/problems/find-k-closest-elements/submissions/


def kClosestElements(arr, target):
    heap = []
    for ele in arr:
        heapq.heappush(heap, [-1 * abs(ele - target), ele])
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

# *https://leetcode.com/problems/the-skyline-problem/submissions/


def skyLineProblem(mat):
    arr = []
    for building in mat:
        arr.append([building[0], -buillding[2]])  # Start Point
        arr.append([building[1], buillding[2]])  # End Point
    sorted(arr, key=lambda x: (x[0], x[1]))

    heap = []
    ans = []
    currHeight = 0
    for point in arr:
        if point[1] < 0:
            heapq.heappush(heap, point[1])
        else:
            heap.remove(point[1])
            heapq.heapify(heap)

        re = -1 * heapq.heappop(heap)
        if re != currheight:
            ans.append([point[0], re])
            currHeight = re
        heapq.heappush(heap, -1 * re)
    return ans
