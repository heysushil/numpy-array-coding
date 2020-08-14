# Logistic Distribution

'''
IMP Points

1. ye growth ko show karne ke liye use hota hai.
2. ye bahot jaruri hai because aage chal ke ye ml aur neural networking me use hoga.
3. ye continuous probability distribution hai
4. isme 2 parameters hote hain pdf (probability density function) and cdf (cumulative density function)

Logistic distribution arg: 
    loc: mean , deafult me ye 0 (zero)
    scale: standard deviation, default value is 1
    size: matrix 
'''

from numpy import random as r
import seaborn as sns
import matplotlib.pyplot as plt

logistcVar = r.logistic(loc=1, scale=2, size=(2,3))
print('\n\n',logistcVar,'\n')

# use seaborn to get plto point
# sns.distplot(r.logistic(loc=1, scale=1, size=(100)), hist=False)
# use plt.show() to show graph
sns.distplot(r.normal(loc=1, scale=2, size=(100)), hist=False, label='noraml')
sns.distplot(r.logistic(loc=1, scale=1, size=(100)), hist=False, label='logstic')
plt.show()


'''
Diff b/w Logistc and Normal Distribution

1. logict jo hai ye normal ke comapristion me thoda log distance tak result deta hai.
2. logistic and noraml both center pont result will be like same.
'''