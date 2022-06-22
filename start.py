import math as m
# from math import *


# ? *************************************** DataTypes

print(help(type(0)))

integer = 20000000
print(integer, type(integer))

float = 20000000000.225
print(float, type(float))

complex = 25 + 60j
print(complex, type(complex))

boolean = True or False
print(boolean, type(boolean))

# *** A set is a collection which is unique, unordered, unchangeable*, and unindexed.
# *** *Set items are unchangeable, but you can remove items and add new items.
# ! Wrong set = {"1", 2, True, {25, 4}} -> Set can't be added in set
# ! Wrong set = {"1", 2, True, ["Nimrat", True]} -> List can't be added in set
set = {"1", 2, True, ('4478')}
print(set, type(set))
for ele in set:
    print(ele, ", ", end=" \n")
set.add(8787)
set.add(877)
set.add(878)
set.add(887)
set.add(787)
set.discard(7)
set.pop()
set.remove(66)
set.copy()
set.clear()

sc = {7, 87, 84, 875, 787, 48, 78, 9865, 65, 87}
set.difference(sc)
set.difference_update(sc)
set.intersection(sc)
set.intersection_update(sc)
set.isdisjoint(sc)
set.issubset(sc)
set.issuperset(sc)
set.symmetric_difference(sc)
set.symmetric_difference_update(sc)
set.union(sc)
set.update(sc)

# ? String(ordered sequence) are immutable in Python
str = "string" + 'string'
print(str, type(str))
print(str[0])
print(str[-1])  # ? print the last character of String

# ? Slicing of String and also same funda can be applied on list or tuple
print(str[2:4])  # 2 : inclusive and 4 : exclusive
print(str[2:4:1])  # 2 : inclusive and 4 : exclusive and 1 : jump
print(str[:4])  # 4 : exclusive
print(str[2:])  # 2 : inclusive

# for printing string in reverse order
print("reverse string : ", str[::-1])
print("reverse string : ", str[-1:0:-1])

print(str[0:5:-1])  # ""
print(str[-1:0:1])  # ""

for ch in str:
    print(ch, end=", ")
print()

for _ in str:
    print("cool")
print()


s1 = "abc"
s2 = 'def'
print(s1 + s2)
print(s1 * 5)  # for repeating the same string

str = ''' Hello Sir, 
            I want a help. 
            Please help
            
        Thanks and regarde.
        Tera baap.
        '''
print(str)

print(str.isalpha())  # is string contains only alphabets
print(str.isdigit())  # is string contains only digits
print(str.islower())
print(str.isupper())
print(str.lower())
print(str.upper())
print(str.lstrip())  # for removing left side whitespaces
print(str.rstrip())  # for removing right side whitespaces
print(str.split())  # split on the basis of whitespaces
print(str.partition('a'))
# split on the basis of separatot for only first instance
print(str.capitalize())
print(str.count('a'))
print(str.find('su'))


print("this is a string {}".format("Inserted"))
print("this is a string {} {} {}".format("a", "b", "c"))
print("this is a string {0} {0} {0}".format("a", "b", "c"))
print("this is a string {0} {2} {1}".format("a", "b", "c"))
print("this is a string {c} {a} {b}".format(a="a", b="b", c="c"))
result = 100/777
print("result is {r:10.3f}".format(r=result))
print(f"result is {result}")  # *** formatted string literals => f-strings


# ****************** list
l = [1, "2", '3', False, ('4478'), {25, 4}, ["Nimrat", True]]
print(l, type(l))
print(l[2])
l[2] = '2878791594'  # ? list are mutable in Python
print(l[2])
del l[5]
print(l[-1])  # ? print the last element of list
del l

# list Comrehension i.e., list = [expression loop condition]
l = [x for x in range(100) if x > 50]  # ** can't use  else in end
l = [x if x > 50 else 'Odd' for x in range(100)]
l = [x*y for x in range(100) for y in range(100)]
print(l)

l.append(800)
l.append(800)
l.append(800)
l.append(800)
l.append(800)
print(l)
l.append([40, 50])  # *** append [40,50] in the list as list element
l.extend([40, 50])  # ***  append 40,50 in the list as separate elements
print(l)
l.insert(50, 8080)
print(l)
l.sort()
print(l)
l.pop()  # remove the last index
print("l : ", l)
l.pop(25)
print(l)
l.reverse()
print(l)
print(l.index(82))
print(l.count(800))
l.remove(89)


print(len(l))  # same for string, tuple, dictionary
print(max(l))  # same for tuple
print(min(l))  # same for tuple
print(sum(l))  # same for tuple

sequence = "range(100)"
print(list(sequence))

l.clear()
print("l : ", l)

l(range(0, 48, 3))
print(l)

l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in l:
    print(item)  # ***** (1,2,3)
    print(a)  # **** 1
    print(b)  # **** 2
    print(c)  # **** 3


# ? Creation of Python tuple without the use of parentheses is known as Tuple Packing.
t = (1, "2", True, False, '4', ('4478'), {25, 4}, ["Nimrat", True])
print(t, type(t))
print(t[5])  # **** they are ordered
print(t[-2])
print(t.count(1))
print(t.index('4'))
# ! t[2] = 164651 -> Tuples are immutable
print(tuple(sequence))

# ? Dictionary
d = {"1": 2, True: ('4478'), 36: {25, 4}, "again": ["Nimrat", True]}
print(d, type(d))
print(d[True], d.get("again"))

d[3] = "ads;lkj"  # dictionary are mutable in Python

for key in d:
    print("(", key, " : ", d[key], ")", end=", ")
print()


for key, value in d.items():
    print(items)
    print(key)
    print(value)

for item in d.iteritems():
    print(item)
for k in d.iterkeys():
    print(k)
for v in d.itervalues():
    print(v)

print(d.viewitems())
print(d.viewkeys())
print(d.viewvalues())

d = {x: x**2 for x in range(20)}
d = {k: v**2 for k, v in zip(['a', 'b', 'c'], range(3))}

# Practice
user = {"name": "raju", "age": 25,
        "year": 2000, "isNewUser": True, "foods":  []}
print(user)

# ? ******************************************************* Operators

a = 50
b = 15

print(a / b)
print(a // b)  # for quotient
print(a % b)  # for remainder

print(a * b)
print(a ** b)  # power

# ! ++ or -- are not their in Python

a += b
a -= b
a *= b
a /= b
a //= b
a **= b

print(a, b)

print(a > b)
print(a < b)

# ? Both are same
print(1 < 2 > 3)  # * False
print(1 < 2 and 2 > 3)  # * False

print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

print('2' == 2)  # *** False
print(2.0 == 2)  # *** True

x = True
y = False

print(x and y)
print(x or y)
print(not y)

a = 10
b = 15

print(a & b)
print(a | b)
print(a ^ b)  # Bitwise XOR
print(~a)


hex(27)
bin(93)
pow(60, 2)
pow(60, 60, 99)
abs(-999)
round(96.39787)
round(79.92987989, 3)


# ? ******************************************************* User Input

# ? input() take any argument as String
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print(a, b)

# ? ******************************************************* Loops

# Most Common Template
n = int(input())
l = []
for i in range(n):  # Here, n is inclusive
    l.append(int(input()))

for i in range(0, n, 1):  # Here, n is exclusive and 1 : jump
    print(l[i], end=", ")
print()
for ele in l:  # same for tuple, string, set
    print(ele, end=", ")
print()

for ele in l:
    # ** nothing to do
    pass


a = 0
while(a < 10):
    a += 1
    if a == 4:
        continue
    if a == 8:
        break
    print(a, end=", ")
else:
    print()

# ? ******************************************************* Conditional Statement

a = 4
if a == 4:
    print("a mil gya")
elif a == 5:
    print("a tu tho gya")
else:
    print("chl chod tu bhai hai apna")

# ? ******************************************************* Modules
# math, random, string

print(dir(m))
print(m.pi)

# ? ******************************************************* function


def calculateSum(seq, m=5):
    return sum(seq) * m


res1 = calculateSum([x for x in range(10)])
res2 = calculateSum([x for x in range(10)], 10)
print(res1, res2)


def myfunc(*args):
    print(args)


myfunc(10, 20, 30, 40, 50, 60)
myfunc(10, 20, 30)
myfunc(10, 20, 30, 40)


def myfunction(**kwargs):
    print(kwargs)


myfunction(a=0, b=1)
myfunction(a=0, b=1, c=2)


def myfun(*args, **kwargs):
    print(args)
    print(kwargs)


myfun(10, 20, 30, a='0', b='1')


# ********** lambda

def square(num): return num ** 2  # ? -> lambda num: num ** 2


l = list(map(square, [1, 2, 3, 4, 5, 6, 7, 98, 9]))
print(l)
l = list(map(lambda num: num ** 2, [1, 2, 3, 4, 5, 6, 7, 98, 9]))
print(l)


def less100(num): return 1 if num < 100 else 0


l = list(filter(less100, [874, 1874, 681, 87,
         86, 41, 6, 7, 1687, 187, 87, 654]))
print(l)
l = list(filter(lambda num: 1 if num < 100 else 1, [
         874, 1874, 681, 87, 86, 41, 6, 7, 1687, 187, 87, 654]))
print(l)

# ? ******************************************************* File Handling


with open("demo.txt", 'r') as f:
    for line in f:
        print(line)
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.read(15))
    f.seek(10)
    print(f.read(15))

l = ["a", "b", "d", "e"]
with open("demo.txt", 'w') as f:
    f.writelines(l)

with open("demo.txt", 'a') as f:
    f.writelines(l)
