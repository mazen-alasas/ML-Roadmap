# List
# https://www.youtube.com/watch?v=0yySumZTxJ0

lst = [15, 'mazen', True, 99.90]
print(lst)                          # [15, 'mazen', True, 99.9]

lst2d = [2, 4, [4, 6, 7]]           # [2, 4, [4, 6, 7]]
# print(lst2d)

strList = list("mazen")
a, b, c, d, e = strList
print(c)                            # z


lst = [1, 2, 3, 4, 5, 6, 8, 8, 9]
print(lst[3])                       # 4
# look at strings folder for indexes
lst[3] = 99                         # to ipdate

lst[4:6] = []
print(lst)                          # [1, 2, 3, 99, 8, 8, 9]

del lst[0]                          # remove by index
print(lst)                          # [2, 3, 99, 8, 8, 9]

lst.remove(8)                       # remove first 8
print(lst)                          # [2, 3, 99, 8, 9]

l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2
print(l3)                           # [1, 2, 3, 4]

print(3 * l1)                       # [1, 2, 1, 2, 1, 2]
listOfZeros = [0] * 100             # list of size 100 contains zeros

listOfStringa = [''] * 10

matrix = [[0] * 4] * 5              # 5 Rows, 4 Columns
"""
[[0, 0, 0, 0], 
 [0, 0, 0, 0], 
 [0, 0, 0, 0], 
 [0, 0, 0, 0], 
 [0, 0, 0, 0]]
"""

LengthOFlist = len(l3)              # number of elements
# print(LengthOFlist)
sumOfElemenntsInList = sum(l3)      # sum of elements (should be numbers) don't support chars or strings
average = sumOfElemenntsInList / LengthOFlist

mx = max(l3)
mn = min(l3)                        # work on chars and strings

l = [7, 9, 5, 6, 3, 4, 1, 1, 2, 7]
print(sorted(l))                    # [1, 1, 2, 3, 4, 5, 6, 7, 7, 9]
print(l)                            # [7, 9, 5, 6, 3, 4, 1, 1, 2, 7]
sortL = sorted(l)
print(sortL)                        # [1, 1, 2, 3, 4, 5, 6, 7, 7, 9]
print(l)                            # [7, 9, 5, 6, 3, 4, 1, 1, 2, 7]
l.sort()
print(l)                            # [1, 1, 2, 3, 4, 5, 6, 7, 7, 9]

reversedSortedList = sorted(l, reverse = True)
print(reversedSortedList)           # [9, 7, 7, 6, 5, 4, 3, 2, 1, 1]

l = "ds afa va svasv"
b = l.split()                       # ['ds', 'afa', 'va', 'svasv']

s = l.split(sep='a')                # ['ds ', 'f', ' v', ' sv', 'sv']
print(s)

sL = [1,2,3,4,5,6,4,8,9,5,2]
isHere = 78 in sL                   # False
isHere = 9  in sL                   # True
# in used with string s too



# add list to a nother
a = [4, 5, 6]
b = [1, 8, 9]
b.extend(a)                         # add list a to list b 
print(b)                            # [1, 8, 9, 4, 5, 6]
print(a)                            # [4, 5, 6]

a = [4, 5, 6]
b = [1, 8, 9]
b += a
print(b)                            # [1, 8, 9, 4, 5, 6]
print(a)                            # [4, 5, 6]


a = [4, 5, 6]
# append()	                        Adds an element at the end of the list
a.append(15)                        # add one element to list
a.append(10)
print(a)                            # [4, 5, 6, 15, 10]


b = [1, 8, 8, 9]
b.insert(1, 45)                     # addd one element by index to list
print(b)                            # [1, 45, 8, 8, 9]


# count()	                        Returns the number of elements with the specified value
ctr = b.count(8)                    # 2
print(ctr)


print(b.index(9))                   # return first index of given element
# if given value not in list will get error so use (in) operator to check if it exist or not first


# reverse()	                        Reverses the order of the list
b.reverse()                         # will reverse list b it self
# pop()	                            Removes the element at the specified position
b.pop()                             # remove last element
# if list is empty will get error
b.pop(2)                            # remove element in index 2


lst = list(range(20))               # list of numbers from 0, 19
lst = list(range(0, 20))            # list of numbers from 0, 19
lst = list(range(5, 20))            # list of numbers from 5, 19
lst = list(range(5, 20, 5))         # list of numbers from 5, 19 step = 5 >> [5, 10, 15]


lstOfSquares = [x ** 3 for x in range(10)] # every x in range 0 : 10 get ^3 and put in lst 
print(lstOfSquares)                 # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

lstD = [x * 2 for x in range(10)]   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(lstD)

lstOfPairs = [(x, y) for x in range(1, 4) for y in range(3, 0, -1)]
print(lstOfPairs)                   # [(1, 3), (1, 2), (1, 1), (2, 3), (2, 2), (2, 1), (3, 3), (3, 2), (3, 1)]
# or
lstOfPairs = [(x, y) for x in [1, 2, 3] for y in [3, 2, 1]]
print(lstOfPairs)                   # [(1, 3), (1, 2), (1, 1), (2, 3), (2, 2), (2, 1), (3, 3), (3, 2), (3, 1)]
# used to generate all Possibilities

listIterator = iter([9,2,4])
print(next(listIterator))           # 9
print(next(listIterator))           # 2
print(next(listIterator))           # 4
# print(next(listIterator))          # error
listIteratorUsingRange = iter(range(0, 21, 5))
print(next(listIteratorUsingRange)) # 0
print(next(listIteratorUsingRange)) # 5
print(next(listIteratorUsingRange)) # 10

st1, st2 = [1,5.5,'kn'], [5,7,9]
st2 = st1
print(st1)                          # [1, 5.5, 'kn']
print(st2)                          # [1, 5.5, 'kn']

x = [1,2,3]
y = x
x[1] = 9
print(y)                            # [1, 9, 3]


# copy()	                        Returns a copy of the list
x = [1,2,3]
y = x.copy()
x[1] = 9
print(y)                            # [1, 2, 3]


# search for enumerate function
# operator library ?? itemgetter ???????????


# clear()	                        Removes all the elements from the list

# extend()	                        Add the elements of a list (or any iterable), to the end of the current list
# index()	                        Returns the index of the first element with the specified value
# insert()	                        Adds an element at the specified position
# remove()	                        Removes the item with the specified value
