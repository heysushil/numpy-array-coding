'''
Exponential Distribution using NumPy and Matplotlib.pyplot by hey sushil:

Jab kabhi bhi next event ke hone ke time ko pata karne ki baat ho tab Exponential Distribution ka use kar ke probability nikali jati hai.

Kisi bhi kaam ke success ya fail hone ke kya chanse hai? Is ki probability Exponential Distribution se hi nikali jati hai.

Best examples:

1. Kisi user ke kisi website pe time spen karne ka duration. Lagbag jadatar user 1-4 sec spend karta hai ek site par. Usse bhi kam 4-8 sec spend karte hain aur sab se kam user 9+ sec spend karte hain kisi website par.

2. Store me line me wait karne walo ki probability? Jadatar log saman lete hi nikal jate hai. Kuch thodi der rukte hain. Usse bhi kam kafi der store me khali ghumte rahte hain.

Exponential Distribution methos argumetns:

scale: number of values
size: number of users or out matrix
'''

import numpy.random as r
import seaborn as sns
import matplotlib.pyplot as plt

# Exponential Distribution values
expovalues = r.exponential(scale=15, size=1000)
# print('\nExpovalues: \n',expovalues)

sns.distplot(expovalues, kde=False, color='darkgreen')
plt.title('Exponetial Distribution Result for Store', fontsize=18, y=1.012)
plt.xlabel('Custome spend time on store', labelpad=15)
plt.ylabel('Total numebr of customers', labelpad=15)
plt.show()



