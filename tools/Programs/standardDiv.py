import numpy as np
import statistics
import math

data = [2,24,6,3,5,8,10,12,3,5,6,25,23]
np = len(data)
total = 0
for num in data:
	total += num
mean_data = total/np
total_sqr = 0

for num in data:
	total_sqr += (num-mean_data)**2

stddiv = (total_sqr/(np-1))**0.5
print("The mean of the data is: ", stddiv)
print("The std is: ", statistics.stdev(data))