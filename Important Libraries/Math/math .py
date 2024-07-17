import math
# import math as m
# from math import nameOfFunction1, name
# from math import *

# operators
print(6 + 2)                    # 8     addition
print(6 - 2)                    # 4     subtraction
print(6 * 2)                    # 12    multiplication
print(6 / 2)                    # 3.0   float division
print(6 // 2)                   # 3     integer division
print(6 % 2)                    # 0     modulus
print(7 / 2)                    # 3.5
print(7 // 2)                   # 3
print(7 % 2)                    # 1
print(divmod(7, 2))             # (3, 1)
print(divmod(6, 2))             # (3, 0)
print(2 ** 3)                   # 8     power
print(pow(2, 3))                # 8
print(abs(-2))                  # 2     absolute value


# comparisons operators
print(6 > 2)                    # True
print(6 < 2)                    # False
print(6 == 2)                   # False
print(6 != 2)                   # True
print(6 >= 2)                   # True
print(6 <= 2)                   # False
print(9 > 6 > 2)                # True      جامد
print(9 > 6 < 2)                # False
print(9 > 6 == 2)               # False


factVal = math.factorial(5)
gammaVal = math.gamma(5)        # gamma(n) = factorial(n - 1)
                                # gamma return float
lnVal = math.log(5, 2)          # 2 is the base
lnValBase2 = math.log2(5)
squarRoot = math.sqrt(49)


deg = math.degrees(30)          # radians to degrees
rad = math.radians(60)          # degrees to radians


# note :
# every parameter to Trigonometric functions should be in (radians) .. 
sinVal = math.sin(rad)
cosVal = math.cos(rad)
tanVal = math.tan(rad)
...
# Inverse Trigonometric Functions (sin^-1, cos^-1 ..)
sin1 = math.asin(sinVal)
cos1 = math.acos(cosVal)
tan1 = math.atan(tanVal)


# constant values
PI = math.pi    # 3.141592653589793
EXP = math.e    # 2.718281828459045
TAU = math.tau  # 6.283185307179586
INF = math.inf  # infinity
NAN = math.nan  # not a number

# copy sign
print(math.copysign(3, -4))     # -3


ceilVal = math.ceil(4.2)        # 5
floorVal = math.floor(4.9)      # 4


# for more
# https://docs.python.org/3/library/math.html
