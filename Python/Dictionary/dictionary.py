# map
# https://www.youtube.com/watch?v=u0yr9B3nH8c

# store data values in key:value pairs
# changeable and do not allow duplicates keys
# name = {key : value, key : value, key : value ,.......etc}
d = {'mazen' : 45, 'ahmed' : 21, 'khaled' : 41}
print(d)
d = {'mazen' : 45, 'ahmed' : 21, 'khaled' : 41, 'mazen' : 18}
print(d)                        # {'mazen': 18, 'ahmed': 21, 'khaled': 41}   take last value (18) of key (mazen)
d = {'mazen' : 45, 'ahmed' : 21, 'khaled' : 41, 'abdo' : 18}
print(d)                        # {'mazen': 45, 'ahmed': 21, 'khaled': 41, 'abdo': 18}


dq = {n : n ** 2 for n in range(10)}
print(dq)                       # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
dq = {n : 'ha' * n for n in range(5)}
print(dq)                       # {0: '', 1: 'ha', 2: 'haha', 3: 'hahaha', 4: 'hahahaha'} 


print(dq[2])                    # haha
print(d['ahmed'])               # 21

dq[4] = 'stop'                  # to update value of dq[4], if there is no key = 4 it will add it with value = 'stop
print(dq)                       # {0: '', 1: 'ha', 2: 'haha', 3: 'hahaha', 4: 'stop'}

# get()	                        Returns the value of the specified key
print(dq.get(3))                # hahaha
print(d.get('khaled'))          # 41
# if there is a duplicate key it will return the last value
print(dq.get(5, "ay haga"))     # ay haga
# if there is no key (5) return "ay haga"       

print(len(dq))                  # 5


# copy()	                    Returns a copy of the dictionary
newdq = dq.copy()
print(newdq)                    # {0: '', 1: 'ha', 2: 'haha', 3: 'hahaha', 4: 'stop'}


# fromkeys()	                Returns a dictionary with the specified keys and value
st = (1,5,9,16)
dqOfst = dict.fromkeys(st)
print(dqOfst)                   # {1: None, 5: None, 9: None, 16: None}
dqOfst[5] = 5454545
print(dqOfst)                   # {1: None, 5: 5454545, 9: None, 16: None}


# keys()	                    Returns a list containing the dictionary's keys
lstOfkeys = list(dq.keys())
print(lstOfkeys)                # [0, 1, 2, 3, 4]


# values()	                    Returns a list of all the values in the dictionary
lstOfVal = list(dq.values())
print(lstOfVal)                 # ['', 'ha', 'haha', 'hahaha', 'stop']


# items()	                    Returns a list containing a tuple for each key value pair
lstOfFullItem = list(dq.items())
# list of tuples
print(lstOfFullItem)            # [(0, ''), (1, 'ha'), (2, 'haha'), (3, 'hahaha'), (4, 'stop')]


tupleOftuples = tuple(dq.items())
print(tupleOftuples)            # ((0, ''), (1, 'ha'), (2, 'haha'), (3, 'hahaha'), (4, 'stop'))


setOftuples = set(dq.items())
print(setOftuples)              # {(1, 'ha'), (3, 'hahaha'), (0, ''), (2, 'haha'), (4, 'stop')}


#                     0  1  2  3                0  1  2  3
mulDq = {'numbers' : (1, 2, 3, 4), 'address' : (5, 6, 7, 8)}
print(mulDq)                    # {'numbers' : (1,2,3,4), 'address' : (5,6,7,8)}

print(mulDq['numbers'][2])      # 3



# ask by key not value like map in c++
isHere = 'khaled' in d
print(isHere)                   # True
isHere = 41 in d
print(isHere)                   # False


# ask by value
isHere = 41 in d.values()
print(isHere)                   # True



del(dq[2])                      # will remove key and value of 2
print(dq)                       # {0: '', 1: 'ha', 3: 'hahaha', 4: 'stop'}

# clear()	                    Removes all the elements from the dictionary
dq.clear() 
print(dq)                       # {}

del(dq)                         # to remove dictionary itself with everything in it
# print(dq)                     # NameError: name 'dq' is not defined. Did you mean: 'd'?


# pop()	                        Removes the element with the specified key
# popitem()	                    Removes the last inserted key-value pair
# setdefault()	                Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	                    Updates the dictionary with the specified key-value pairs
