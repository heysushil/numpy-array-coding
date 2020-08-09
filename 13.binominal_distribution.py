# binomal distribution

'''
Binomial distribution: (50/50)
 
jaise ke coin ko tose karne ki probability

random me hi ab bionomial method me following arguments pass honge:

1. n = number of tiral
2. p = probability (eg. 0.3)
3. size = ye matrix ki size ke liye hai
'''

# import reqired modules
from numpy import random as r
# pyplot of matplotlib to show graph
import matplotlib.pyplot as plt
# seabor lib jis ki ploting points ko pyplopt ko pass karenge
import seaborn as sns

toss = r.binomial(n=10, p=0.8, size=20)
print('\ntoss: \n',toss)

# noraml distribution matrix
sns.distplot(r.normal(loc=50, scale=5, size=1000), hist=False, label="noraml")

# finllay create matrix to plot in graph for binomial
sns.distplot(r.binomial(n=100, p=0.5, size=1000), hist=False, label="binomial")

# show the graph
plt.show()


'''
Binomual distribution agar chote result ke liey check kiya jaey to ye normal dist. jaise hi hoga.

But agar large number me binomial ka case find karna hai so waha par ye case noraml se best result dega.
'''