# Multinomial Distribution

'''
IMP Points:

1. ye binomial ka bhai hai wo kewal 2 hi condtion ke bich me probability find karta tha, jaise 0 ya 1 or head or tels.
2. But Multinomial naam se hi pata chal raha hai ki 2 se jada case ke liye to jaise head aur tell to hoga but tie hone ke bhi chances hai tab kya hoga?
'''

from numpy import random as r
import seaborn as sns
import matplotlib.pyplot as plt

sns.distplot(r.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]))
print(r.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]))
plt.show()