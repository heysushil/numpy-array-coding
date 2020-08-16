# normal distribution

'''
Mr. Gussian

Use for: IQ score / Hearbeat etc

random.normal()

normal method ke ander total 3 arguemtns pass honge:
1. loc: (Mean)
2. scale: (Stander deviation) 
3. size: shpe of the returning array
'''

# creat a matix using random noral of 2*3

from numpy import random as r
# graph me point waise outpute show karne ke liye matplotlib ka pyplot module use karna hoga.
import matplotlib.pyplot as plt
import seaborn as sns

# getNomalMatrix = r.normal(size=(2, 3))
getNomalMatrix = r.normal(loc=1010, scale=2, size=(1000))

# sns.distplot(r.normal(loc=5, scale=1,size=1000), hist=False)
sns.distplot(r.normal(loc=1010, scale=20, size=(1000)), hist=False)

# print('\ngetNomalMatrix: \n',getNomalMatrix)

plt.show()


'''
Noraml distribution ka shape ek bell jaisa hai so isli liye isko Bell Curve bhi kahte hai.
'''