st = {1, 5, 3, 4, 4, 5, 1, 9}
# sets
# unordered, unchangeable, and do not allow duplicate values
# print(st[0])                  # TypeError: 'set' object is not subscriptable 

# can contain different data types
st = {1, True, 0, 45, 'abc'};
print(st)                       # {0, 1, 'abc', 45}
# 0 = False & 1 = True
st = {'v', 'c', 'd', 'c', 'a'}  # {'v', 'd', 'a', 'c'}


# unchangeable, but you can remove items and add new items
# pop()	                        Removes an element from the set
st.pop()                        # remove first element

# add()	                        Adds an element to the set
st.add(6)                       # {1, 6, 45, 'abc'}

lst = list(st)                  # ['abc', 1, 6, 45]
lst[1] = 99
st = set(lst)                   # {1, 'abc', 99, 45}

st = {n for n in range(1, 11)}  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

st1 = {4, 5, 6, 9, 1}
st2 = {1, 7, 5, 4}
# set = firstSet or second      will take first true value if the first is empty will take the second one
s = st1 or st2                  # s = first set    
print(s)                        # {1, 4, 5, 6, 7, 9}

st1 = {4, 5, 6, 9, 1}
st2 = {1, 7, 5, 4}
# set = firstSet or second      will take first true value if the first is empty will take the second one
s = st1 and st2                 # s = first set    
print(s)                        # {1, 4, 5, 7}



st1 = {4, 5, 6, 9, 1}
st2 = {1, 7, 5, 4}
s = st1 | st2                   # {1, 4, 5, 6, 7, 9}
print(s)
# or
# union()	                    Return a set containing the union of sets
s = st1.union(st2)      
print(s)                        # {1, 4, 5, 6, 7, 9}


st1 = {4, 5, 6, 9, 1}
st2 = {1, 7, 5, 4}
s = st1 & st2                   # {1, 4, 5}
print(s)
# or
# intersection()	            Returns a set, that is the intersection of two other sets
s = st1.intersection(st2)  
print(s)                        # {1, 4, 5}


st1 = {4, 5, 6, 9, 1}
st2 = {1, 7, 5, 4}
s = st1 ^ st2                   
print(s)                        # {6, 7, 9}
# or
# symmetric_difference()	    Returns a set with the symmetric differences of two sets
s = st1.symmetric_difference(st2)
print(s)                        # {6, 7, 9}


st1 = {4, 5, 6, 9, 1}
st2 = {1, 7, 5, 4}
s = st1 - st2                   
print(s)                        # {9, 6}
t = st2 - st1
print(t)                        # {7}
# or
# difference()	                Returns a set containing the difference between two or more sets
s = st1.difference(st2)
print(s)                        # {9, 6}
t = st2.difference(st1)
print(t)                        # {7}

# copy()	                    Returns a copy of the set
s = st1.copy()
print(s)                        # {1, 4, 5, 6, 9}


# clear()	                    Removes all the elements from the set
# remove()	                    Removes the specified element
s.remove(4)
print(s)                        # {1, 5, 6, 9}

# update()	                    Update the set with the union of this set and others
st3 = {5, 6, 77, 91}
st4 = {5, 6, 7, 9, 104}
st3.update(st4)
print(st3)                      # {5, 6, 7, 104, 9, 77, 91}
print(st4)                      # {5, 6, 7, 104, 9}

# issubset()	                Returns whether another set contains this set or not
x = {'a', 1, 7, 8}
y = {4, 8, 6, 7, 1, 'a'}
z = x.issubset(y)
print(z)                        # True

# issuperset()	                Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "w", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)                        # False because 'b' is not in x

# isdisjoint()	                Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "cherry", "facebook"}
z = x.isdisjoint(y)
print(z)                        # False because x and y have a common element





















