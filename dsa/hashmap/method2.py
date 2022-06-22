import math
import sys

# *https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/


def countDistinctElementsInWindowsOfSizeK(arr, k):
    n = len(arr)
    if k > n:
        n = k

    map = {}
    for i in range(0, k):
        if arr[i] not in map.keys():
            map[arr[i]] = 0
        map[arr[i]] += 1
    res = [len(map)]

    for i in range(k+1, n):
        map[arr[i - k - 1]] -= 1
        if arr[i] not in map:
            map[arr[i]] = 0
        map[arr[i]] += 1
        res.append(len(map))
    return res

# *https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/


def longestSubstringWithKDistinctCharacters(s, k):
    n = len(s)
    if n == 0 or k == 0:
        return 0
    if k > n:
        n = k

    map = {}

    res = -sys.maxsize
    j = 0
    #  ? Acquire
    for i in range(0, n):
        ch = s[i]
        if ch not in map.keys():
            map[ch] = 0
        map[ch] += 1

        #  ? Release
        while j < i and len(map) > k:
            ch = s[j]
            map[ch] -= 1
            if map[ch] == 0:
                del map[ch]
            j += 1

        if len(map) == k:
            res = max(res, j - i + 1)
    return res

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-substrings-with-exactly-k-unique-characters-official/ojquestion


def countSubstringWithKDistinctCharacters(s, k):
    n = len(s)
    if n == 0 or k == 0:
        return 0
    if k > n:
        n = k

    if k == 1:
        return countSubstringWithKDistinctCharactersFor1(s)

    bigMap = {}
    smallMap = {}

    i = 0
    j = 0
    count = 0
    #  ? Release
    for idx in range(0, n):
        #  ? Acquire Big
        while i < n and not (ch not in bigMap.keys() and len(bigMap) == k):
            ch = s[i]
            if ch not in bigMap.keys():
                bigMap[ch] = 0
            bigMap[ch] += 1
            i += 1
        #  ? Acquire Small
        while j < n and not (ch not in smallMap.keys() and len(smallMap) == k - 1):
            ch = s[j]
            if ch not in smallMap.keys():
                smallMap[ch] = 0
            smallMap[ch] += 1
            j += 1

        count += j - i

        #  ? Release Big and Small
        ch = s[idx]
        smallMap[ch] -= 1
        bigMap[ch] -= 1

        if bigMap[ch] == 0:
            del bigMap[ch]
        if smallMap[ch] == 0:
            del smallMap[ch]
    return count


def countSubstringWithKDistinctCharactersFor1(s):
    bigMap = {}

    i = 0
    count = 0
    for idx in range(0, n):
        while i < n and not (ch not in bigMap.keys() and len(bigMap) == k):
            ch = s[i]
            if ch not in bigMap.keys():
                bigMap[ch] = 0
            bigMap[ch] += 1
            i += 1

        count += j - i

        ch = s[idx]
        bigMap[ch] -= 1

        if bigMap[ch] == 0:
            del bigMap[ch]
    return count

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/equivalent-subarrays-official/ojquestion


def countOfEquivalentSubArrays(arr):
    st = {ele for ele in arr}

    k = len(st)
    n = len(arr)

    bigMap = {}
    smallMap = {}

    i = 0
    j = 0
    count = 0
    #  ? Release
    for idx in range(0, n):
        #  ? Acquire Big
        while i < n and not (arr[i] not in bigMap.keys() and len(bigMap) == k):
            if arr[i] not in bigMap.keys():
                bigMap[arr[i]] = 0
            bigMap[arr[i]] += 1
            i += 1
        #  ? Acquire Small
        while j < n and not (arr[j] not in smallMap.keys() and len(smallMap) == k - 1):
            if arr[j] not in smallMap.keys():
                smallMap[arr[j]] = 0
            smallMap[arr[j]] += 1
            j += 1

        count += j - i

        #  ? Release Big and Small
        smallMap[arr[idx]] -= 1
        bigMap[arr[idx]] -= 1

        if bigMap[arr[idx]] == 0:
            del bigMap[arr[idx]]
        if smallMap[arr[idx]] == 0:
            del smallMap[arr[idx]]
    return count

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/longest-substring-with-at-most-k-unique-characters-official/ojquestion


def longestSubstringWithAtMostKDistinctCharacters(s, k):
    n = len(s)
    if n == 0 or k == 0:
        return 0
    if k > n:
        n = k

    map = {}

    res = -sys.maxsize
    j = 0
    #  ? Acquire
    for i in range(0, n):
        ch = s[i]
        if ch not in map.keys():
            map[ch] = 0
        map[ch] += 1

        #  ? Release
        while j < i and len(map) > k:
            ch = s[j]
            map[ch] -= 1
            if map[ch] == 0:
                del map[ch]
            j += 1
        res = max(res, j - i + 1)
    return res

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-substrings-having-at-most-k-unique-characters-official/ojquestion


def countSubstringWithAtMostKDistinctCharacters(a, k):
    n = len(s)
    if n == 0 or k == 0:
        return 0
    if k > n:
        n = k

    map = {}

    j = 0
    count = 0
    #  ? Acquire
    for i in range(0, n):
        ch = s[i]
        if ch not in map.keys():
            map[ch] = 0
        map[ch] += 1

        count += i-j

        #  ? Release
        while j < i and len(map) > k:
            ch = s[j]
            map[ch] -= 1
            if map[ch] == 0:
                del map[ch]
            j += 1
    return count

# ? Distinct -> Non Repeating

# *https: // www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/longest-substring-with-unique-characters-official/ojquestion


def longestSubstringWithDistinctCharacters(s):
    n = len(s)

    if n == 0:
        return 0

    map = {}
    j = 0
    res = -sys.maxsize

    #  ? Acquire
    for i in range(0, n):
        ch = s[i]
        if ch not in map.keys():
            map[ch] = 0
        map[ch] += 1

        #  ? Release
        while j < i and map[ch] > 1:
            map[ch] -= 1
            if map[ch] == 0:
                del map[ch]
            j += 1

        res = max(res, i - j + 1)
    return res

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-substrings-having-all-unique-characters-official/ojquestion


def countSubstringWithDistinctCharacters(s):
    n = len(s)

    if n == 0:
        return 0

    map = {}
    j = 0
    count = 0

    #  ? Acquire
    for i in range(0, n):
        ch = s[i]
        if ch not in map.keys():
            map[ch] = 0
        map[ch] += 1

        count += i - j

        #  ? Release
        while j < i and map[ch] > 1:
            map[ch] -= 1
            if map[ch] == 0:
                del map[ch]
            j += 1
    count += n - j
    return count

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/largest-subarray-with-zero-sum-official/ojquestion


def largestSubArrayWithSum0(arr):
    n = len(arr)

    sum = 0
    map = {}
    for i in range(0, n):
        sum += arr[i]
        map[sum] = i

    res = -sys.maxsize
    sum = 0
    for i in range(0, n):
        sum += arr[i]
        res = max(res, map[sum] - i)
    return res

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-all-subarrays-with-zero-sum-official/ojquestion


def countSubArrayWithSum0(arr):
    n = len(arr)

    sum = 0
    map = {}
    for i in range(0, n):
        sum += arr[i]
        if sum not in map.keys():
            map[sum] = 0
        map[sum] += 1

    count = 0
    for key in map.keys():
        count += map[key] * (map[key] - 1) / 2
    return count


def largestSubArrayWithSumK(arr):
    n = len(arr)
    if n == 0:
        return 0

    sum = 0
    map = {}
    for i in range(0, n):
        sum += arr[i]
        map[sum] = i

    res = -sys.maxsize
    sum = 0
    for i in range(0, n):
        sum += arr[i]
        if map[sum + k] in map.keys():
            res = max(res, map[sum + k] - i)
    return res

#  *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-subarrays-having-sum-equals-to-k-official/ojquestion


def countSubArrayWithSumK(arr, k):
    n = len(arr)
    if n == 0:
        return 0

    sum = 0
    map = {}
    count = 0
    for key in map.keys():
        sum += arr[i]
        if map[sum - k] in map.keys():
            count += map[sum] * map[sum - k]
        if sum == k:
            count += 1
        if sum not in map.keys():
            map[sum] = 0
        map[sum] += 1
    return count

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/longest-subarray-with-sum-divisible-by-k-official/ojquestion


def longestSubArrayWhoseSumDivisibleByK(arr, k):
    n = len(arr)
    if n == 0:
        return 0

    map = {0: -1}

    sum = 0
    res = -sys.maxsize
    for i in range(0, n):
        sum += arr[i]
        rem = sum % k

        if rem < 0:
            rem += k

        if rem not in map.keys():
            map[rem] = i

        if rem in map.keys():
            res = max(res, i - map[rem])
    return res

# ? Here -15 and 15 as sum are equivalent as both are divisible by 5;
# *https: // www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-subarrays-with-sum-divisible-by-k-official/ojquestion


def countSubArrayWhoseSumDivisibleByK(arr, k):
    n = len(arr)
    if n == 0:
        return 0

    map = {0: 1}
    for i in range(0, n):
        sum += arr[i]
        rem = sum % k

        if rem < 0:
            rem += k

        if rem not in map.keys():
            map[rem] = 0
        map[rem] += 1

    count = 0
    for key in map.keys():
        count += map[key] * (map[key] - 1) / 2
    return count


# *https: // www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/longest-subarray-with-equal-number-of-zeroes-and-ones-official/ojquestion
def longestSubArrayWithEqual0sAnd1s(arr):
    n = len(arr)
    if n == 0:
        return 0

    map = {0: -1}
    sum = 0
    res = -sys.maxsize
    for i in range(0, n):
        sum += -1 if arr[i] == 0 else arr[i]
        if sum not in map.keys():
            map[sum] = i
        else:
            res = max(res, i - map[sum])
    return res

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-subarrays-with-equal-number-of-zeroes-and-ones-official/ojquestion


def countSubArrayWithEqual0sAnd1s(arr):
    n = len(arr)
    if n == 0:
        return 0

    map = {0: 1}
    sum = 0
    for i in range(0, n):
        sum += -1 if arr[i] == 0 else arr[i]
        if sum not in map.keys():
            map[sum] = 0
        map[sum] += 1

    count = 0
    for key in map.keys():
        count += key * (key - 1) / 2
    return count

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/longest-subarray-with-equal-number-of-0s-1s-and-2s-official/ojquestion


def longestSubArrayWithEqual0s1sAnd2s(arr):
    n = len(arr)
    if n == 0:
        return 0

    map = {"0#0": -1}
    res = -sys.maxsize

    count0s = 0
    count1s = 0
    count2s = 0

    for i in range(0, n):
        if arr[i] == 0:
            count0s += 1
        elif arr[i] == 1:
            count1s += 1
        else:
            count2s += 1

        key = "" + (count1s - count0s) + "#" + (count2s - count1s)
        if key not in map.keys():
            map[key] = i

        if key in map.keys():
            res = max(res, i - map[key])
    return res

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-subarrays-with-equal-number-of-0s-1s-and-2s-official/ojquestion


def countSubArrayWithEqual0s1sAnd2s(arr):
    n = len(arr)
    if n == 0:
        return 0

    map = {"0#0": 1}

    count0s = 0
    count1s = 0
    count2s = 0

    for i in range(0, n):
        if arr[i] == 0:
            count0s += 1
        elif arr[i] == 1:
            count1s += 1
        else:
            count2s += 1

        key = "" + (count1s - count0s) + "#" + (count2s - count1s)
        if key not in map.keys():
            map[key] = 0
        map[key] += 1

    count = 0
    for key in map.keys():
        count += map[key] * (map[key] - 1) / 2
    return count

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/maximum-consecutive-ones-ii-official/ojquestion


def maxConsecutiveOnes(arr, k):
    n = len(arr)
    if n == 0:
        return 0

    countOf0s = 0
    j = 0
    res = -sys.maxsize
    #  ? Acquire
    for i in range(0, n):
        if arr[i] == 0:
            countOf0s += 1

        #  ? Release
        while j < i and countOf0s > k:
            if arr[j] == 0:
                countOf0s -= 1
            j += 1
        res = max(res, i - j + 1)
    return res

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/largest-subarray-with-contiguous-elements-official/ojquestion


def longestSubArrayWithContiguousElements(arr):
    n = len(arr)
    if n == 0:
        return 0

    res = 0
    for i in range(0, n):
        currMin = arr[i]
        currMax = arr[i]
        st = {arr[i]}

        for j in range(i+1, n):
            if arr[j] in st:
                break
            currMax = max(currMax, arr[j])
            currMin = min(currMin, arr[j])
            if j - i == currMax - currMin:
                res = max(res, j - i + 1)
    return res

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/smallest-subarray-with-all-occurrences-of-the-most-frequent-element-official/ojquestion


def smallestSubArrayWithHighestFrequency(arr):
    n = len(arr)
    if n == 0:
        return 0

    map = {}
    maxFreq = 0
    for ele in arr:
        if ele not in map.keys():
            map[ele] = 0
        map[ele] += 1
        maxFreq = max(maxFreq, map[ele])

    smallestMap = {}
    largestMap = {}
    for ele in arr:
        if map[ele] == maxFreq:
            smallestMap[ele] = -1
            largestMap[ele] = n

    for i in range(0, n):
        if arr[i] in smallestMap.keys() and smallestMap[arr[i]] == -1:
            smallestMap[arr[i]] = i
    for i in range(n-1, -1, -1):
        if arr[i] in largestMap.keys() and largestMap[arr[i]] == n:
            largestMap[arr[i]] = i

    res = 0
    for key in smallestMap.keys():
        res = max(res, largestMap[key] - smallestMap[key])

    for key in smallestMap.keys():
        if res == largestMap[key] - smallestMap[key]:
            return [ele, largestMap[key], smallest[key]]
    return [-1, -1, -1]

# *https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/smallest-substring-of-a-string-containing-all-characters-of-another-string-official/ojquestion


def minWindowSubString(s, ss):
    n = len(s)

    targetMap = {}
    for ch in ss:
        if ch not in targetMap.keys():
            targetMap[ch] = 0
        targetMap[ch] += 1

    map = {}
    j = 0
    res = n
    si = -1
    ei = n
    matchCount = 0

    #  ? Acquire
    for i in range(0, n):
        ch = s[i]
        if ch not in map[i]:
            map[ch] = 0
        map[ch] += 1

        if ch in targetMap.keys() and map[ch] <= targetMap[ch]:
            matchCount += 1

        #  ? Release
        while matchCount == len(ss):
            if res >= i - j:
                res = i-j
                si = i
                ei = j

            ch = s[j]
            map[ch] -= 1
            if ch in targetMap.keys() and map[ch] < targetMap[ch]:
                matchCount -= 1
            j += 1

    return "" if si == -1 or ei == n else s[i:j + 1]
