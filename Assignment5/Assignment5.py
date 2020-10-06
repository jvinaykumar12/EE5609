
import matplotlib.pyplot as plt
import numpy as np
import math

x   = np.linspace(-15,15,10)
y1  = -((4*x)+3)/5
y2  = (1+3*x)/2
plt.plot(x,y1, label = '(4 5)x = -3')
plt.plot(x,y2, label = '(3 -2)x = -1')

plt.axis("equal")
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid() 
