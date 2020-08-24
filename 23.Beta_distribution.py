'''
Beta distribution using matplotlib.pyplot, numpy.random module and seaborn librarys by hey sushil (Chaudhary Sushil):

Probability theory ke andar aur statistics me isko continuous probability distribution familiy me rakha gaya hai.

Beta distribution ko [0, 1] interval ke beach me define kiya jata hai.

Beta distribution ko 2 possitive paramerters se denote kiya jata hai:
1. alpha
2. beta

Beta distribution ke andar ye dono parameters ye kaam karte hain:
1. Random varibale ke exponent ke roop me hota hai.
2. Durshra, ye distribution ke shape ko control karta hai.
3. Agar isko multiple varaible me generalize kiya jaye to uss case me ye- Dirichlet distributon ban jata hai.

Beta distribution ka use random variable ya matrix model ke andar ek limited length me hi kai shape me change kiya ja sake uske liye kiya jata hai.

Beta distribution ka best use random variables ke sath percantages and proportions nikalne me kiya jata hai.

Kuch important points:

1. Beta distribution, ek special case hai Dirichlet distribution ka.
2. Beta distribution, Gamma distribution se related hai.
3. Beta distribution, ka use Bayesian interface aur order statistics me bhi kiya jata hai.

Note: Beta function bhi hota hai but wo math me hota hai. Iss ko Eular integral of fist kind bhi kahte hain.
Ye special type ka function hai jo gamma function aur Binomial coefficent ke pass hota hai.

numpy.random.beta method arguments:
a: Float or array like float values and non-negative (for Alpha)
b: Float or array like float values and non-negative (for Beta)
size: int or tuple of int values in return

Reference Links:
1. https://en.wikipedia.org/wiki/Beta_distribution
'''

import numpy.random as r
import seaborn as sns
import matplotlib.pyplot as plt

# print('\n', r.beta(a=0.5, b=0.5, size=(10)))

# a and b both on same range
sns.distplot(r.beta(a=0.5, b=0.5, size=(100,100)), hist=False, label='a=0.5 b=0.5')

# a point high and b point low to show hight to low ratio
sns.distplot(r.beta(a=5, b=1, size=(100,100)), hist=False, label='a=5 b=1')

sns.distplot(r.beta(a=1, b=5, size=(100,100)), hist=False, label='a=1 b=5')

sns.distplot(r.beta(a=2, b=2, size=(100,100)), hist=False, label='a=2 b=2')

sns.distplot(r.beta(a=2, b=5, size=(100,100)), hist=False, label='a=2 b=5')

# plt mehtods to beutify the result
# plt.xlim(0,1)
# plt.ylim(0,2.5)
plt.xlabel('Range of X')
plt.ylabel('Frequcry of Y')
plt.title('Beta Distribution')

plt.show()