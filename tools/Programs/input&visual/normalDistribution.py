import numpy as np
import matplotlib.pyplot as plt

mean = 100
std = 5
size = 100000
values = np.random.normal(mean, std, size)
plt.hist(values,200)
plt.axvline(values.mean(), color = 'g', linestyle= 'dotted' , linewidth=2)
plt.show()
