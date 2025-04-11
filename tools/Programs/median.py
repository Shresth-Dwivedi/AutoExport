import numpy as np
import statistics
import math

data = [2,24,6,3,5,8,10,12,3,5,6,25,23]
data.sort()
np = math.trunc(len(data)/2.0)
median_loc = np
median_data = data[median_loc]
print("Median Loc: ", median_loc)
print("The sorted data is: ", median_data)
print("Mean of the data: ", statistics.median(data))