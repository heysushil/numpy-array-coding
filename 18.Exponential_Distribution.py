'''
Exponential Distribution:


'''

import numpy.random as r
# import seaborn as sns
import matplotlib.pyplot as plt

data = r.exponential(3, 10000)
count, bins, ignored = plt.hist(data, 14, density=True)
plt.show()
