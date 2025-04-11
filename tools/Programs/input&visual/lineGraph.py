import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)

plt.plot(x,2*x+1,"-r",label = "y=2x+1")
plt.plot(x,2*x-1,"-g",label = "y=2x-1")
plt.legend("Graph of fx")

plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = "upper left")
plt.show()