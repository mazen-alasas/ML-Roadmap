t = (1, 9, 3, 4)
# or
tt = 5, 9, 6
print(type(t))              # <class 'tuple'>
print(type(tt))             # <class 'tuple'>
# ordered and unchangeable
print(t)                    # (1, 9, 3, 4)
print(t[3])                 # 4

# use this if you need to do change in it 
t1 = (1, 2, 3)
l1 = list(t1)
l1[1] = 9
t1 = tuple(l1)
print(t1)                   # (1, 9, 3)

# can contain different data types
t = (4, 50, 'ersf00', True)

# allows duplicate members
t = (1, 3, 1, 1)
print(max(t))               # maximum number in tuple


# can use the tuple() constructor to make list  tuple
t = tuple(["apple", "banana", "cherry"])
print(t)


# count()	                Returns the number of times a specified value occurs in a tuple
# index()	                Searches the tuple for a specified value and returns the position of where it was found



























