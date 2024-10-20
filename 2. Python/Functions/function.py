
def sum2numbers (n, m):
    ans = n + m
    return ans

print(sum2numbers(9, 7))


def maxi (a, b):
    return a if a > b else b

mx = maxi                        # store function in variable
print(mx(7, 6))


def max_elements(listt):         # pass (list or tuple or set or string) to function
    return max(listt)

lst = [1, 4, 3, 84, 5, 20, 7, 8, 9]
print(max_elements(lst))


def sum_elements(*elements):     # *elements to pass any number of arguments (list or tuple or set or string)
    return sum(elements)

print(sum_elements(*lst))

def print_values(**elements):    # **elements to pass any number of arguments (dictionary)
    for key in elements:
        print(key, end = " ")
    print()

dct = {"mazen": 45, "ahmed": 21, "alasas": 41}
print_values(**dct)
# or pass key and values in same line
print_values(mazen = 45, ahmed = 21, alasas = 41)


# defult values
def sum2numbers (n, m = 10):        # recommended to use defult values
    ans = n + m
    return ans

print(sum2numbers(9)) 


# variable scope 
# global variable
glo = 9
def assign ():
    glo = 5

assign()
print(glo)                          # 9


# to access global variable
def assign ():
    global glo
    glo = 5

assign()
print(glo)                          # 5


# lambda function for simple operations
# var = lambda arg1, arg2: expression(return value)
increment_val = lambda x: x + 10
val = 5
print(increment_val(val))           # 15

aTimesB = lambda x, y: x * y
print(aTimesB(5, 6))                # 30

aPowerB = lambda x, y: x ** y
print(aPowerB(5, 6))                # 15625


# use lambda function with filter to create new list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_lst = list(filter(lambda x: x % 2 == 0, lst))
print(even_lst)                     # [2, 4, 6, 8, 10]



# use lambda function with map to create new list
# map iterates over every element in the (list or tuple or set or string) and applies the function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_lst = list(map(lambda x: x ** 2, lst))
print(square_lst)                   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# use lambda function with reduce to calculate sum
# reduce iterates over every element and applies the function
# from functools import reduce
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_lst = reduce(lambda x, y: x + y, lst)
# print(sum_lst)                      # 55

# fibonaci sequence iteratively
def fib(n):
    a, b = 0, 1
    fibo_list = []
    for i in range(n):
        fibo_list.append(a)
        a, b = b, a + b
    return fibo_list

print(fib(10))

# recursive function

# fibonaci sequence recursively
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(10))              # 55

# factorial
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))              # 120


# knapsack problem (weight, items) -> https://codeforces.com/group/MWSDmqGsZm/contest/223339/submission/251571661
val, wgt = [], []
def knapsack(w, n):
    if n <= 0 or w <= 0:
        return 0
    if wgt[n - 1] > w:
        return knapsack(w, n - 1)
    return max(val[n - 1] + knapsack(w - wgt[n - 1], n - 1), knapsack(w, n - 1))

n, w = input().split()
n, w = int(n), int(w)
for i in range(n):
    wt, vt = input().split()
    wgt.append(int(wt))
    val.append(int(vt))
print(knapsack(w, n))