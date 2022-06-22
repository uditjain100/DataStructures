# this in Java => self in Python
# null in Java => None in Python

from queue import *


class YouTubeChannel:
    name = 'Otaku'  # Class or Static Variable

    def __init__(self):
        self.id = "Ox4sEn8"  # Instance Variable
        self.numberOfSubScribers = 25

    def get_id(self):  # getters
        return self.id

    def set_id(self, _id):  # setters
        self.id = _id

    def printSubScribers(self):  # instance method
        print(self.numberOfSubScribers)

    @classmethod
    def printChannelName(cls):  # class method
        print(cls.name)

    @staticmethod
    def welcomeTag():  # static method
        print("Hey Guys, Weelcome To My YouTube Channel")

    def block(self):  # ***************** abstract method
        raise NotImplementedError("Subclass should implement it")


channel = YouTubeChannel()
channel.printSubScribers()

YouTubeChannel.printChannelName()
YouTubeChannel.welcomeTag()


class PlayList(YouTubeChannel):  # Inheritance
    pass


class Video(PlayList, YouTubeChannel):  # Method resolution Order (MRO)
    def __init__(self):
        PlayList.__init__()  # PlayList __init__ will be called as MRO is always left to Right
        YouTubeChannel.__init__()


# Duck Typing


class A:

    def __init__(self, a):
        self.value = a

    def speak(self):
        print("A is speaking")

    def __add__(self, other):  # + operator overloading
        return A(self.value + other.value)

    def __gt__(self, other):  # > operator overloading
        return self.value > other.value

    def __str__(self):  # similar to toString(String str) method in JAVA
        return str(self.value)

    def __len__(self):
        return 200

    def __del__(self):
        print("This object is deleted")


class B:

    def speak(self):
        print("B is speaking")


obj = A(5)
obj.speak()
print(obj + A(10))  # Synthetic Sugar
print(obj > A(10))
print(obj < A(10))
obj = B()  # Dynamic Typing
obj.speak()


class Trie:

    class Node:  # Inner Class
        def __init__(self, v):
            self.value = v
            self.children = [None for x in range(0, 2)]
            self.isWord = False

        def __init__(self):
            self.value = 0
            self.children = [None for x in range(0, 2)]
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
                curr = curr.children[bit]
            curr.isWord = True

    def insert(self, ele):
        curr = self.root
        for i in range(0, 32):
            bit = 0 if ((1 << i) & ele) == 0 else 1
            if curr.children[bit] == None:
                curr.children[bit] = Trie.Node()
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


trie = Trie()
trie.insert(252525)

print(trie.search(252525))
print(trie.search(252524))


class Pair:
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def __gt__(self, other):
        return self.first > other.first if self.first != other.first else self.second > other.second

    def __str__(self):
        return "(" + str(self.first) + ", " + str(self.second) + ")"


pq = PriorityQueue()
pq.put(Pair(1, 2))
pq.put(Pair(2, 3))
pq.put(Pair(3, 5))
pq.put(Pair(3, 0))
pq.put(Pair(8, 1))
pq.put(Pair(0, 5))
pq.put(Pair(9, 7))

res = list(pq.queue)
res.append(Pair(0, 111))

for p in res:
    print(type(p))
    print("(" + str(p.first) + ", " + str(p.second) + ")")
