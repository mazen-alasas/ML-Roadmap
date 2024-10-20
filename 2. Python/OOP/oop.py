class car1:
    color = "red"

c1 = car1()
print(c1.color)                     # red


class car2:
    color = 'blue'

c2 = c3 = car2
print(c2.color)                     # blue
c3.color = 'green'
print(c3.color)                     # green
print(c2.color)                     # green



# instance variable
class car:
    def __init__(self, color):
        self.color = color

    def change_color(self, color):
        self.color = color

    def show(self):
        print(self.color)

c4, c5 = car('yellow'), car('black')
c4.show()                           # yellow
c5.show()                           # black
c4.change_color('red')
c4.show()                           # red
c5.show()                           # black


class calc1:
    def __init__(self, a, b):
        self.a = a ** 2
        self.b = b ** 3

c6 = calc1(10, 5)
print(c6.a)
print(c6.b)              

class calc2:
    def __init__(self, a = 5, b = 3):
        self.a = a ** 2
        self.b = b ** 3

c7 = calc2()
print(c7.a)
print(c7.b) 





# fetures when declaring variables
a: int = 10
b: float = 10.5
c: str = "10"
d: bool = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

