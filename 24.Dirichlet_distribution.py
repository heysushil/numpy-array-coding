'''
Dirichlet distribution using matplotlib.pyplot, numpy.random module and seaborn librarys by hey sushil (Chaudhary Sushil):

Probability and statistics me Dirichlet distribution, continuous multivariate probabiltiy distribution family ka member hai.

Multivariate Meaning: Multivariate Random variables ya random vector, mathematical values ka full list hota hai. Issme bhi wo values jo yata unkown hai ya unki value incomplete hai. Ayse data collection ko Multivarate kahte hain.

Dirichlet distribution ka use text mining me kiya jata hai.

Dirichlet distribution ko samjhne ke liye pahle inki jankari hona bahot jaruri hai: 
1. binomial distribution
2. multinomial distribution
3. gamma function
4. beta distribution 

aur inke relationships ko janan jaruri hai.

1 and 2 points ko jante ho.
3. Gamma Function: Hum gamma distribution ki nahi balki function ki baat kar rahe hain. Because gamma distribution ka iss method se direct koi lena dena nahi hai.
But Gamma function ko bahot acche se define kiya gaya hai kisi bhi complex number ko handel karne ke liye.
Gamma function ke pass kuch spacial properties hain jinka use beta and Dirichlet distribution properties ko define karne me use kiya jata hai.


Dirichlet distribution ke jaruri points:

1. Ye posative real number vector hai.
2. Beta distribution ka multivariate generalization hai.
3. Iska use Bayesian statistics me prior distribution ki tarah kiya jata hai.
4. K-dimentional vector ka set, jiski entry positive real number ke [0,1] ke interval ke beach me kiya jata hai.

numpy.random.dirichlet arguments:
alpha: Float sequence aur length k
size: random numbers matrix

Reference Links:
1. https://leimao.github.io/blog/Introduction-to-Dirichlet-Distribution/
2. https://en.wikipedia.org/wiki/Dirichlet_distribution
'''

import numpy.random as r
import matplotlib.pyplot as plt

s = r.default_rng().dirichlet((10, 5, 3), 20).transpose()

# print('\ns: ', s);exit()

plt.barh(range(20), s[0])
plt.barh(range(20), s[1], left=s[0], color='g')
plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
plt.title('Length of String Using Dirichlet Distribution')

plt.show()