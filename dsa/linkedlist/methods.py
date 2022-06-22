from linkedlist import linkedList
from sys import *


def swap(curr, newCurr):
    temp = curr.value
    curr.value = newCurr.value
    newCurr.value = temp


def size(head):
    n = 0
    curr = head
    while curr != None:
        n += 1
        curr = curr.next
    return n

# **** When head of List is not given


def deleteNode(nodeToBeDeleted):
    if nodeToBeDeleted.next == None:
        return False
    nodeToBeDeleted.value = nodeToBeDeleted.next.value
    nodeToBeDeleted.next = nodeToBeDeleted.next.next
    return True


def deleteNodeHavingGreaterValueOnLeftSide(head):
    if head == None or head.next == None:
        return head

    curr = head
    currMax = curr.value

    while curr.next != None:
        if curr.next.value < currMax:
            curr.next = curr.next.next
        else:
            curr = curr.next
            currMax = max(currMax, curr.value)
    return head


def deleteNodeHavingGreaterValueOnRightSide(head):
    if head == None or head.next == None:
        return head

    head = reverse(head)
    curr = head
    currMax = curr.value

    while curr.next != None:
        if curr.next.value < currMax:
            curr.next = curr.next.next
        else:
            curr = curr.next
            currMax = max(currMax, curr.value)
    head = reverse(head)
    return head


def removeAtFromLast(head, k):
    n = size(head)
    k = n-k-1

    curr = head
    while curr != None and k > 1:
        k -= 1
        curr = curr.next
    if curr.next != None:
        curr.next = curr.next.next


def getMiddle(head):
    n = size(head)

    slow = fast = head
    if (n & 1) != 0:
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
    else:
        slow = None
        while fast != None and fast.next != None:
            slow = slow.next if slow != None else head
            fast = fast.next.next
    return slow


def reverse(head):
    if head == None or head.next == None:
        return head

    prev = None
    curr = head

    while curr != None:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next
    return prev


def reverseSubList(head, si, ei):

    n = size(head)

    prev = None
    next = None

    if si == 1 and ei == n:
        return reverse(head)
    elif si == 1:

        curr = head
        count = 0
        while curr != None and count < ei:
            count += 1
            curr = curr.next
        next = curr.next
        curr.next = None

        h = reverse(head)
        curr = h
        while curr.next != None:
            curr = curr.next
        curr.next = next

        head = h

    elif ei == n:

        curr = head
        count = 0
        while curr != None and count < si:
            count += 1
            curr = curr.next
        next = curr.next
        curr.next = None

        h = reverse(next)
        curr.next = h

    else:

        curr = head
        count = 0
        while curr != None and count < ei:
            if count == si - 2:
                prev = curr
            count += 1
            curr = curr.next

        next = curr.next
        h = prev.next
        prev.next = None
        curr.next = None

        h = reverse(prev.next)
        prev.next = h
        curr = h
        while curr.next != None:
            curr = curr.next
        curr.next = next
    return head


def reverseInGroupsOfSizeK(head, k):

    n = size(head)
    numberOfFullGroups = n / k
    sizeOfPartialGroup = n % k

    si = 1
    for i in range(0, numberOfFullGroups):
        head = reverseSubList(head, si, si + k)
        si += k

    if sizeOfPartialGroup != 0:
        head = reverseSubList(head, si, n)
    return head


def reverseData(head):
    if head == None or head.next == None:
        return head

    mid = getMiddle(head)
    newHead = mid.next
    mid.next = None

    newHead = reverse(newHead)

    curr = head
    newCurr = newHead

    while newCurr != None:
        swap(curr, newCurr)
        curr = curr.next
        newCurr = newCurr.next

    newHead = reverse(newHead)
    mid.next = newHead


def isPalindrome(head):
    if head == None or head.next == None:
        return True

    mid = getMiddle(head)
    newHead = mid.next
    mid.next = None

    newHead = reverse(newHead)

    curr = head
    newCurr = newHead

    while newCurr != None:
        if curr.value != newCurr.value:
            return False
        curr = curr.next
        newCurr = newCurr.next

    newHead = reverse(newHead)
    mid.next = newHead
    return True


def rotateList(head, k):
    if head == None or head.next == None:
        return head

    n = size(head)
    while k < 0:
        k += n
    k %= n

    if k == 0 or k == n-1:
        return head

    curr = head
    while curr != None and k > 0:
        curr = curr.next
        k -= 1

    newHead = curr.next
    curr.next = None

    head = reverse(head)
    newHead = reverse(newHead)

    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = newHead

    head = reverse(head)
    return head


def rotateSubList(head, k, si, ei):
    if head == None or head.next == None:
        return head

    n = size(head)
    while k < 0:
        k += (ei - si + 1)
    k %= (ei - si + 1)

    if k == 0 or k == (ei - si):
        return head

    prev = next = None

    if si == 1 and ei == n:
        rotateList(head, k)
    elif si == 1:

        count = 0
        curr = head
        while curr != None and count < ei:
            count += 1
            curr = curr.next

        next = curr.next
        curr.next = None

        head = rotateList(head, k)

        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = next

    elif ei == n:

        count = 0
        curr = head
        while curr != None and count < si:
            count += 1
            curr = curr.next

        prev = curr.next
        curr.next = None

        prev = rotateList(prev, k)

        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = prev

    else:

        count = 0
        curr = head
        while curr != None and count < ei:
            if count == si - 2:
                prev = curr
            count += 1
            curr = curr.next

        p = prev.next
        next = curr.next

        prev.next = None
        curr.next = None

        h = rotateList(p, k)

        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = h
        while curr.next != None:
            curr = curr.next
        curr.next = next
    return head

# ? size : size of each group and k : rotating factor


def rotateListInGroups(head, k, size):
    n = size(head)
    numberOfFullGroups = n / size
    sizeOfPartialGroup = n % size

    si = 1
    for i in range(0, numberOfFullGroups):
        head = rotateSubList(head, k, si, si + size)
        si += size

    if sizeOfPartialGroup != 0:
        head = rotateSubList(head, k, si, n)
    return head


def isCycleExist(head):
    slow = fast = head
    while fast != None or fast.next != None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


def cycleTailIntersection(haed):
    slow = fast = head
    while fast != None or fast.next != None:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next

    if slow != fast:
        return None

    slow = head

    while fast != None or fast.next != None:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next
    return slow


def intersectionPointOfTwoLL1(head1, head2):
    n1 = size(head1)
    n2 = size(head2)

    h1 = head1
    h2 = head2

    if n1 < n2:
        head1 = h2
        head2 = h1

    diff = abs(n1 - n2)

    curr1 = head1
    while curr1 != None and diff > 0:
        diff -= 1
        curr1 = curr1.next

    curr2 = head2

    while curr1 != None and curr2 != None:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    return None


def intersectionPointOfTwoLL2(head1, head2):
    curr = head1
    while curr.next != None:
        curr = curr.next

    curr.next = head1

    slow = fast = head2
    while fast != None or fast.next != None:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next

    if slow != fast:
        return None

    slow = head2

    while fast != None or fast.next != None:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next
    return slow


def add(head1, head2):

    if head1 == None:
        return head2
    if head2 == None:
        return head1

    stack1 = []
    stack2 = []

    curr1 = head1
    curr2 = head2

    while curr1 != None:
        stack1.append(curr1.value)
        curr1 = curr1.next
    while curr2 != None:
        stack2.append(curr2.value)
        curr2 = curr2.next

    nh = linkedList.LinkedList().Node(-1)
    nc = nh

    carry = 0
    while len(stack1) != 0 and len(stack2) != 0:
        sum = carry + stack1.pop() + stack2.pop()
        carry = sum / 10
        nc.next = linkedList.LinkedList().Node(sum % 10)
        nc = nc.next
    while len(stack1) != 0:
        sum = carry + stack1.pop()
        carry = sum / 10
        nc.next = linkedList.LinkedList().Node(sum % 10)
        nc = nc.next
    while len(stack2) != 0:
        sum = carry + stack2.pop()
        carry = sum / 10
        nc.next = linkedList.LinkedList().Node(sum % 10)
        nc = nc.next
    if carry != 0:
        nc.next = linkedList.LinkedList().Node(carry)

    return nh.next


def subtract(head1, head2):
    n1 = size(head1)
    n2 = size(head2)

    h1 = head1
    h2 = head2

    curr1 = head1
    curr2 = head2

    if n1 < n2:
        head1 = h2
        head2 = h1

    if n1 == n2:
        while curr1 != None:
            if curr1 < curr2:
                head1 = h2
                head2 = h1
                break

    borrow = 0
    nh = linkedList.LinkedList().Node(-1)
    nc = nh

    while curr1 != None and curr2 != None:
        diff = curr1.value - curr2.value
        currBorrow = borrow
        if diff < 0:
            diff += 10
            borrow = 1
        if currBorrow != 0:
            diff -= 1
        borrow = currBorrow
        nc.next = linkedList.LinkedList().Node(diff)
        nc = nc.next

    while curr1 != None:
        diff = curr1.value
        currBorrow = borrow
        if diff < 0:
            diff += 10
            borrow = 1
        if currBorrow != 0:
            diff -= 1
        borrow = currBorrow
        nc.next = linkedList.LinkedList().Node(diff)
        nc = nc.next

    return nh.next


def oddEven(head):
    if head == None or head.nexxt == None:
        return head

    head1 = head
    head2 = head.next

    curr1 = head1
    curr2 = head2

    while curr1 != None and curr2 != None and curr2.next != None:
        curr1.next = curr1.next.next
        curr2.next = curr2.next.next

        curr1 = curr1.next
        curr2 = curr2.next

    curr1.next = head2
    return head


def swapPairWise(head):
    if head == None or head.nexxt == None:
        return head

    head1 = head
    head2 = head.next

    curr1 = head1
    curr2 = head2

    while curr1 != None and curr2 != None and curr2.next != None:
        curr1.next = curr1.next.next
        curr2.next = curr2.next.next

        curr1 = curr1.next
        curr2 = curr2.next

    nh = linkedList.LinkedList().Node(-1)
    nc = nh

    curr1 = head1
    curr2 = head2

    while curr1 != None and curr2 != None:
        nc.next = curr2
        nc = nc.next
        curr2 = curr2.next

        nc.next = curr1
        nc = nc.next
        curr1 = curr1.next

    if curr1 != None:
        nc.next = curr1
    return nh.next


def reOrder(head):
    if head == None or head.next == None:
        return head

    mid = getMiddle(head)
    newHead = mid.next
    mid.next = None

    newHead = reverse(newHead)

    nh = linkedList.LinkedList().Node(-1)
    nc = nh

    curr1 = head
    curr2 = newHead

    while curr1 != None and curr2 != None:
        nc.next = curr1
        nc = nc.next
        curr1 = curr1.next

        nc.next = curr2
        nc = nc.next
        curr2 = curr2.next

    if curr1 != None:
        nc.next = curr1
    return nh.next


def intersectionOf2SortedLists(head1, head2):
    if head1 == None or head2 == None:
        return None

    curr1 = head1
    curr2 = head2

    nh = linkedList.LinkedList().Node(-1)
    nc = nh

    while curr1 != None and curr2 != None:
        if curr1.value < curr2.value:
            curr1 = curr1.next
        elif curr1.value > curr2.value:
            curr2 = curr2.next
        else:
            nc.next = linkedList.LinkedList().Node(curr1.value)
            nc = nc.next
            curr1 = curr1.next
            curr2 = curr2.next
    return nh.next


def unionOf2SortedLists(head1, head2):
    if head1 == None or head2 == None:
        return None

    curr1 = head1
    curr2 = head2

    nh = linkedList.LinkedList().Node(-1)
    nc = nh

    while curr1 != None and curr2 != None:
        nc.next = linkedList.LinkedList().Node(-1)
        if curr1.value < curr2.value:
            nc.value = curr1.value
            curr1 = curr1.next
        elif curr1.value > curr2.value:
            nc.value = curr2.value
            curr2 = curr2.next
        else:
            nc.value = curr2.value
            curr1 = curr1.next
            curr2 = curr2.next
        nc = nc.next
    return nh.next


def merge2SortedLists(head1, head2):
    if head1 == None or head2 == None:
        return None

    curr1 = head1
    curr2 = head2

    nh = linkedList.LinkedList().Node(-1)
    nc = nh

    while curr1 != None and curr2 != None:
        if curr1.value < curr2.value:
            nc.next = linkedList.LinkedList().Node(curr1.value)
            curr1 = curr1.next
        elif curr1.value > curr2.value:
            nc.next = linkedList.LinkedList().Node(curr2.value)
            curr2 = curr2.next
        else:
            nc.next = linkedList.LinkedList().Node(curr1.value)
            nc = nc.next
            nc.next = linkedList.LinkedList().Node(curr2.value)
            curr1 = curr1.next
            curr2 = curr2.next
        nc = nc.next
    return nh.next


def mergeKSortedLists(lists):
    mergeKSortedLists(lists, 1, len(lists))


def mergeKSortedLists(lists, si, ei):
    if si == ei:
        return lists[si]
    if si + 1 == ei:
        return merge2SortedLists(lists[si], lists[ei])

    mid = si + (ei - si) / 2
    left = mergeKSortedLists(lists, si, mid)
    right = mergeKSortedLists(lists, mid + 1, ei)

    return merge2SortedLists(left, right)


def mergeSort(head):
    if head == None or head.next == None:
        return head

    mid = getMiddle(head)
    newHead = mid.next
    mid.next = None

    left = mergeSort(head)
    right = mergeSort(newHead)

    return merge2SortedLists(left, right)


def partitionList(head, idx):
    if head == None or head.next == None:
        return [None, head, None]

    pivot = 0
    temp = None
    curr = head
    prev = None
    while curr != None:
        prev = curr
        if idx == 1:
            temp = curr.next
            curr.next = curr.next.next
        curr = curr.next
        idx -= 1
    pivot = temp.value
    prev.next = temp

    nh1 = linkedList.LinkedList().Node(-1)
    nh2 = linkedList.LinkedList().Node(-1)
    nc1 = nh1
    nc2 = nh2

    curr = head
    while curr != None:
        next = curr.next
        if curr.value <= pivot:
            nc1.next = curr
            nc1 = nc1.next
        else:
            nc2.next = curr
            nc2 = nc2.next
        curr.next = None
        curr = next
    return [nh1.next, pivot, nh2.next]


def merge(left, middle, right):
    if left == None and right == None:
        return [middle, middle]
    elif left == None:
        middle.next = right[0]
        return [middle, right[1]]
    elif right == None:
        left[1].next = middle
        return [left[0], middle]
    else:
        left[1].next = middle
        middle.next = right[0]
        return [left[0], right[1]]


def quickSort(head):
    if head == None or head.next == None:
        return [head, head]

    n = size(head)
    mid = n/2

    partition = partitionList(head, mid)

    left = quickSort(partition[0])
    right = quickSort(partition[2])

    return merge(left, partition[1], right)


def removeDuplicatesFromSortedList(head):
    if head == None or head.next == None:
        return head

    curr = head
    while curr.next != None:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


def removeDuplicatesFromUnortedList(head):
    if head == None or head.next == None:
        return head

    head = mergeSort(head)

    curr = head
    while curr.next != None:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


def clone(head):
    nh = linkedList.LinkedList().Node(-1)

    curr1 = head
    curr2 = nh
    while curr1 != None:
        curr2.next = linkedList.LinkedList().Node(curr.value)
        curr1 = curr1.next
        curr2 = curr2.next

    return nh.next


def twoSum(head, target, nodeToBeIgnored: []):
    if head == None or head.next == None:
        return [[None, None]]

    head = mergeSort(head)

    n = size(head)
    nh = clone(head)

    curr1 = head
    curr2 = nh

    map = {}
    while curr1 != None:
        map[curr1] = curr2
        curr1 = curr1.next
        curr2 = curr2.next

    nh = reverse(nh)

    curr1 = head
    curr2 = nh

    idx1 = 1
    idx2 = n

    res = []

    while curr1 != None and curr2 != None:
        while curr1 != None and curr1 in nodeToBeIgnored:
            curr1 = curr1.next
        while curr2 != None and map[curr2] in nodeToBeIgnored:
            curr2 = curr2.next
        if curr1 == None or curr2 == None:
            break
        sum = curr1.value + curr2.value
        if sum < target:
            curr1 = curr1.next
            idx1 += 1
        elif sum > target:
            curr2 = curr2.next
            idx2 -= 1
        else:
            if idx1 == idx2:
                break
            res.add[curr1, map[curr2]]
            curr1 = curr1.next
            idx1 += 1
            curr2 = curr2.next
            idx2 -= 1

            while idx1 < idx2 and curr1 != None and curr1.value == curr1.next.value:
                curr1 = curr1.next
            while idx1 < idx2 and curr2 != None and curr2.value == curr2.next.value:
                curr2 = curr2.next
    return res


def threeSum(head, target):
    if head == None or head.next == None or head.next.next == None:
        return [[None, None, None]]

    head = mergeSort(head)

    res = []

    curr = head
    while curr.next.next != None:

        if curr != head and curr != None and curr.next != None and curr.value == curr.next.value:
            curr = curr.next
        if curr == None or curr.next == None or curr.next.next == None:
            break

        next = curr.next
        curr.next = None

        ans = twoSum(next, target - curr.value)
        for arr in ans:
            res.append(curr)
            res.append(arr[0])
            res.append(arr[1])

        curr.next = next
        curr = next
    return res


def fourSum(head, target):
    if head == None or head.next == None or head.next.next == None or head.next.next.next == None:
        return [[None, None, None, None]]

    head = mergeSort(head)

    res = []

    curr = head
    while curr.next.next.next != None:

        if curr != head and curr != None and curr.next != None and curr.value == curr.next.value:
            curr = curr.next
        if curr == None or curr.next == None or curr.next.next == None:
            break

        next = curr.next
        curr.next = None

        ans = threeSome(next, target - curr.value)
        for arr in ans:
            res.append(curr)
            res.append(arr[0])
            res.append(arr[1])
            res.append(arr[2])

        curr.next = next
        curr = next
    return res
