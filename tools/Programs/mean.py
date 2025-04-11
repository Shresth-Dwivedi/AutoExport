import numpy as np
import statistics
import math

data = [2,24,6,3,5,8,10,12,3,5,6,25,23]
np = len(data)
total = 0
for num in data:
      total += num

mean_data = total/np

print("Mean of given data is", math.trunc(mean_data))
print("Mean of the data", statistics.mean(data))