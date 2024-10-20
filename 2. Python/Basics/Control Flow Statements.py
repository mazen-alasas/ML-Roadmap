n, m = 5, 9
# if statement
if n > m:
    print("n is greater than m")
elif n < m or n == m: 
    print("n is less than or equal to m")

# using ternary operator
print("n is greater than m") if n > m else print("n is less than or equal to m")
print("n is greater than m" if n > m else "n is less than or equal to m")

# ternary operator using tuple
print((n, m) [n < m])       # will print n if n < m return false and m if n < m return true

# ternary operator using dictionary
print({True : "n is greater than m", False : "n is less than or equal to m"} [n > m])

mx = n if n > m else m
print(mx)


# for
for i in range(6):
    print(i, end = " ")
print()

# for with range
for i in range(1, 6, 2):
    print(i, end = " ")
print()

# nested
for i in range(1, 6):
    for j in range(1, 6):
        print(f"({i}, {j})", end = " ")
    print()
  
"""
(1, 1) (1, 2) (1, 3) (1, 4) (1, 5)
(2, 1) (2, 2) (2, 3) (2, 4) (2, 5)
(3, 1) (3, 2) (3, 3) (3, 4) (3, 5)
(4, 1) (4, 2) (4, 3) (4, 4) (4, 5)
(5, 1) (5, 2) (5, 3) (5, 4) (5, 5)
"""

# pass
for i in range(6):
    if i == 3:
        pass
    print(i, end = " ")
print()

# break
for i in range(6):
    if i == 3:
        break
    print(i, end = " ")
print()

# continue
for i in range(6):
    if i == 3:
        continue
    print(i, end = " ")
print()


# for with else
for i in range(6):
    print(i, end = " ")
else:
    print("\nFinished")



# for with string
str = "mazen"
for it in str:
    print(it, end = " ")
print()
# or
for i in range(len(str)):
    print(str[i], end = " ")
print()


# for with list
lst = [1, 2, 3]
for it in lst:
    print(it, end = " ")
print()
# or
for i, val in enumerate(lst):
    print(f"lst[{i}] = {val}", end = " ")
print()
# or
for i in range(len(lst)):
    print(lst[i], end = " ")
print()

# for with set
st = {1, 2, 3, 4, 5}
for it in st:
    print(it, end=" ")
print()


# for with tuple
tup = (1, 2, 3)
for it in tup:
    print(it, end = " ")
print()

# for with dictionary
dic = {"a" : 1, "b" : 2, "c" : 3}
for i in dic:
    print(f"dic[{i}] = {dic[i]}", end = " ")
print()
# dic[a] = 1  dic[b] = 2  dic[c] = 3
# or
for key, value in dic.items():
    print(f"dic[{key}] = {value}", end = " ")
print()

for it in dic.items():
    print(it, end = " ")
print()
# ('a', 1) ('b', 2) ('c', 3)


for it in dic.keys():
    print(it, end = " ")
print()

for it in dic.values():
    print(it, end = " ")
print()


l1 = [1, 2, 3]
l2 = [4, 5, 6]
for it in zip(l1, l2):
    print(it)
print()
"""
(1, 4)
(2, 5)
(3, 6)
"""

# or
for i, j in zip(l1, l2):
    print(f"{i} {j}")
print()

# create list using for
l = [it for it in range(10) if it % 2 == 0]
print(l)                            # [0, 2, 4, 6, 8]


# create list using zip by 
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [i + j for i, j in zip(l1, l2)]
print(l)                            # [5, 7, 9]


# while
i = 1
while i < 6:
    print(i, end = " ")
    i += 1
print()

# while with else
i = 1
while i < 6:
    print(i, end = " ")
    i += 1
else:
    print("\nFinished")

num = -2
while num:              # condition can be negative or positive but not zero
    # print(num)
    num += 1
print(num)

# infinite loop
# while True:
#     print("hi")
