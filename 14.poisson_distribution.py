# Poisson Distribution

'''
Jab koi din me 2 bar khana kha raha hai to kya probability banti hai ki wo din me 3rd time khana kahayega ya nahi?

random me possion method me follow hone wale arguments:

lam = rate or number of occurence
size = shape of matirx
'''

# improt random by numpy
from numpy import random as r
# for graph view use pyplot
import matplotlib.pyplot as plt
# seabor lib
import seaborn as sns

possion = r.poisson(lam=2, size=10)
print('\npossion: \n',possion)

# use  possion into seaborn
# sns.distplot(r.poisson(lam=2, size=1000), kde=False)

# create nomal dist
sns.distplot(r.normal(loc=5, scale=7, size=1000), hist=False, label="normal")

# binomial dist
sns.distplot(r.binomial(n=1000, p=0.01, size=1000), hist=False, label="binomial")
# create poisson
sns.distplot(r.poisson(lam=10, size=1000), hist=False, label="poisson")

# show by plytlo
plt.show()


'''
Diff b/w Normal n Possion:

1. normal continus ke liey hota hai aur isme possitve and negative 2no values hotei hain.
2. Possion non-negative values hoti hai aur isi liye isko disceat ki familiy me rakha jaata hai.


Diff b/w Binomial n Possion:

1. binomal 50/50 jaise case ke liye best hai. but yes kuch cases me 2no ka result same jaise ho sakte
2. binomal me hume n aur p milta hai jo agar hum possion jaise result ko pana cahe to simple n*p ye lagbhag possion ke lam ke barabr ho jayega ga aur isliye hi kuch cases me 2no same lag sakte hai
'''

