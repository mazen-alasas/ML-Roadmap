import re               # Regular Expression
# https://www.w3schools.com/python/python_regex.asp
# https://www.youtube.com/watch?v=bnSYeYFRCaA

s1 = "mazen"
s2 = 'alasas'
# s1[0]     first char
# s1[-1]    last char
# s2 * 3    repeat
# s[3] * 4 


print(s1[2:])           # zen
print(s1[2:4])          # ze
print(s1[:4])           # maze
print(s1[:])            # mazen


# steps
nums = "0123456789"
print(nums[::2])        # 02468
print(nums[3:10:2])     # 3579
print(nums[2::3])       # 358
print(nums[:7:4])       # 04
print(nums[-1:4:-1])    # 98765
print(nums[::-1])       # 9876543210


print(list(nums))
numbers = "48769991468798542"
print(sorted(numbers))              # to sort string or numbers
print(set(numbers))                 # like set in c++ but not sorted


sentance = "mazen ahmed alasas"
print(sentance.split())             # ['mazen', 'ahmed', 'alasas']
print(sentance.split('a'))          # ['m', 'zen ', 'hmed ', 'l', 's', 's']
print(sentance.partition('a'))      # ('m', 'a', 'zen ahmed alasas') first
print(sentance.rpartition('a'))     # ('mazen ahmed alas', 'a', 's') last
email = "mazen@gmail.com"
print(email.split('@gmail.com'))    # ['mazen', '']
print(email.partition('@'))         # ('mazen', '@', 'gmail.com')


print(email.find('!'))              # -1
print(email.find('a'))              # 1
print(email.rfind('a'))             # 8
print(email.index('a'))             # 1
#print(email.index('!'))             # error
email = email.replace('a', 't')     # replace each first char by second one

print(email.count('t'))             # 2

print("mazen ahmed".capitalize())   # Mazen ahmed
print("mazen ahmed".title())        # Mazen Ahmed
print("mazen ahmed".upper())        # MAZEN AHMED
print("MazEn AhmeD".swapcase())     # mAZeN aHMEd


print("MAZEN".center(20))           # '       MAZEN        '
print("mazen".ljust(10))            # add spaces يمين
print("mazen".rjust(10))            # add spaces شمال
print("mazen".ljust(10, '*'))       # add stars يمين
print("479852".zfill(10))           # 0000479852


print("8".isalpha())                
print("@".isascii())
print("8".isalnum())
print("y".isnumeric())
print(" ".isspace())
print("Mazen Ahmed".istitle())      # True
print("Mazen ahmed".istitle())      # False


print(' csdc csas '.strip())        # 'csdc csas'
print('**csdccsas '.strip('*'))     # 'csdccsas'     
print(' csdc csas '.lstrip())       # 'csdc csas '
print(' csdc csas '.rstrip())       # ' csdc csas'
'''
gmail = "mazen@gmail.com"
if gmail.endswith('@gmail.com'):
    user = gmail.rstrip('@gmail.com')
    print(user)
'''
st = '''mazen
ahmed
alasas'''
print(st.splitlines())                  # ['mazen', 'ahmed', 'alasas']


a, b = 'sda', 'ertq'
print(a, b)                             # sda ertq
print(a, end = ' ') 
print(b)                                # sda ertq


name = 'mazen'
print("hi %s, welsome .." %name)        # hi mazen, welsome ..
price = 2000
print("the price = %d and taxes = %d" %(price, 0.05 * price))      # the price = 2000 and taxes = 100
print('numbers %5d' %9)                 # numbers     9
print('numbers %05d' %9)                # numbers 00009


print("Mazen".startswith('maz'))        # False
print("Mazen".startswith('Maz'))        # True
print("Mazen".endswith('en'))           # True


names = ', '.join(('mazen', 'ahmed'))   # take only strings
print(names)                            # mazen, ahmed
print(','.join('mazen'))                # m,a,z,e,n


print("my name is {} and i'm {} years old".format("mazen", 22))
print("my name is {0} and i'm {1} years old".format("mazen", 22))
print("my name is {1} and i'm {0} years old".format("mazen", 22))
print("my name is {l} and i'm {r} years old".format(l = "mazen", r = 22))
print("my name is {r} and i'm {l} years old".format(l = "mazen", r = 22))
PI = 3.1459945621724739854427787272521
print("pi = {0:.3f}".format(PI))        # 3 digit
print("{:s} {:d} years old".format("i'm", 22))
print('|' + "{:^10}".format("hi") + '|')# |    hi    |



# Learn RegEx
text = "To email Guido, try guido@python.org or guido@google.com"
email = re.compile('\w+@\w+\.[a-z]{3}') # match
print(email.findall(text))

email3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
print(email3.findall(text))

email4 = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+).(?P<suffix>[a-z]{3})')
match = email4.match('guido@python.org')
print(match.groupdict())





# capitalize()	                    Converts the first character to upper case
# casefold()	                    Converts string into lower case
# center()	                        Returns a centered string
# count()	                        Returns the number of times a specified value occurs in a string
# encode()	                        Returns an encoded version of the string
# endswith()	                    Returns true if the string ends with the specified value
# expandtabs()	                    Sets the tab size of the string
# find()	                        Searches the string for a specified value and returns the position of where it was found
# format()	                        Formats specified values in a string
# format_map()	                    Formats specified values in a string
# index()	                        Searches the string for a specified value and returns the position of where it was found
# isalnum()	                        Returns True if all characters in the string are alphanumeric
# isalpha()	                        Returns True if all characters in the string are in the alphabet
# isascii()	                        Returns True if all characters in the string are ascii characters
# isdecimal()	                    Returns True if all characters in the string are decimals
# isdigit()	                        Returns True if all characters in the string are digits
# isidentifier()	                Returns True if the string is an identifier
# islower()	                        Returns True if all characters in the string are lower case
# isnumeric()	                    Returns True if all characters in the string are numeric
# isprintable()	                    Returns True if all characters in the string are printable
# isspace()	                        Returns True if all characters in the string are whitespaces
# istitle()	                        Returns True if the string follows the rules of a title
# isupper()	                        Returns True if all characters in the string are upper case
# join()	                        Joins the elements of an iterable to the end of the string
# ljust()	                        Returns a left justified version of the string
# lower()	                        Converts a string into lower case
# lstrip()	                        Returns a left trim version of the string
# maketrans()	                    Returns a translation table to be used in translations
# partition()	                    Returns a tuple where the string is parted into three parts
# replace()	                        Returns a string where a specified value is replaced with a specified value
# rfind()	                        Searches the string for a specified value and returns the last position of where it was found
# rindex()	                        Searches the string for a specified value and returns the last position of where it was found
# rjust()	                        Returns a right justified version of the string
# rpartition()	                    Returns a tuple where the string is parted into three parts
# rsplit()	                        Splits the string at the specified separator, and returns a list
# rstrip()	                        Returns a right trim version of the string
# split()	                        Splits the string at the specified separator, and returns a list
# splitlines()	                    Splits the string at line breaks and returns a list
# startswith()	                    Returns true if the string starts with the specified value
# strip()	                        Returns a trimmed version of the string
# swapcase()	                    Swaps cases, lower case becomes upper case and vice versa
# title()	                        Converts the first character of each word to upper case
# translate()	                    Returns a translated string
# upper()	                        Converts a string into upper case
# zfill()	                        Fills the string with a specified number of 0 values at the beginning