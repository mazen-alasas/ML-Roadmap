import matplotlib.pyplot as plt
import numpy as np
import random
from itertools import count
from matplotlib.animation import FuncAnimation

x_vals = []
y1, y2 = [], []

index = count()

def animate(i):
    x_vals.append(next(index))
    y1.append(random.randint(0, 10))
    y2.append(random.randint(0, 10))

    plt.cla()   # clear axis
    
    plt.plot(x_vals, y1)
    plt.plot(x_vals, y2)

    plt.legend(['y1', 'y2'])

ani = FuncAnimation(plt.gcf(), animate, interval = 1000) # in millisecond

plt.show()