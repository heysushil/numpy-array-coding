# Uniform Distribution or Rectangular Distribution

'''
Imp points:

1. yaha par har ek event ke hone ki same probability hoti hai.
2. uniform method ke arg: 
    a = lower bound (0.0)
    b = upper bound (1.0)
    size = matrix size
'''

from numpy import random as r
import seaborn as sns
import matplotlib.pyplot as plt

# uniformMatrix = r.uniform(0.2,0.4,size=(10))
uniformMatrix = r.uniform(size=(10))
print('\n\n',uniformMatrix,'\n')

sns.distplot(r.uniform(size=(1000)), hist=False)

plt.show()