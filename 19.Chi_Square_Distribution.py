'''
Chi Square Distribution using NumPy Array and Matplotlib.pyplot:

Chi Square Distribution ka use kiya jata hai jab ek jaise 2 chijo ke beach me realtion nikalna ho tab is distribution ka use kiya jata hai.

Example se samjhte hain:

1. Maan lo ki ek ice cream shop pe aane walao logo me aadmi aur aurat kin flavor ko jada pasan kar rahe hain. Agar ye pata chal jaye to ice cream shop wala jada bikne wale ice cream ko stock kar ke rakh sakta hai.

2. Isi tarike se same type ka example hum cloth shop ke liye bhi le sakte hain. Jaha par ice cream ki jagah par cloth ki baat karte hain.

Chi Square Distribution method ke arguments:

df: number of degree of freedom and must be >0
size: scalar array ka shape
'''

import numpy.random as r
import matplotlib.pyplot as plt
import seaborn as sns

# chiVaraible = r.chisquare(df=2, size=(10,10))
# print('\nchiVaraible: \n',chiVaraible)

# sns.distplot(chiVaraible, hist=False)
# plt.show()


# show advance example
# pip install scipy
# pip list
from scipy import stats
import numpy as np

# np.linspace(star, end, randomNumber)
numpyMatrix = np.linspace(0, 10, 100)
# print('\nnumpyMatrix: ',numpyMatrix)
fig, ax = plt.subplots(1, 1)
print('\nfig: ',fig, ' \nax: ',ax)

# 4 alag line ke liye dots
linestypes = [':','--','-.','-']
deg_of_freedom = [1,4,7,6]

# for loop ka use kare line styel aur deg of freemo ko marg karna hai aur ek final matrix bana hai.
for df, ls in zip(deg_of_freedom, linestypes):
    ax.plot(numpyMatrix, stats.chi2.pdf(numpyMatrix, df), linestyle=ls)

# x aur y axis ka range set kar rahe hain
plt.xlim = (0, 10)
plt.ylim(0, 0.4)

# x aur y axis ka name aur output table ka name
plt.xlabel('Values')
plt.ylabel('Frequecy')
plt.title('Chi_square Distribution')

# show the graph
plt.legend()
plt.show()
