'''
Rayleigh Distribution using matplotlib.pyplot, numpy.random module and seaborn librarys by hey sushil:

Rayleigh Distribution kya hai?

1. Ye continuous probability distribution hai.
2. Rayleigh Distribution ka use signal processing ke liye hota hai. 
3. Rayleigh Distribution, Weibull Distribution ka special case hai jisme scale paramether 2 rakhna hoga.
4. Iske alawa Rayleigh Distribution me agar scale 1 ho aur yahi same case Chi-square distribution me df(degree of freedom) 2 kare to ye ek jaise honge.

Rayleigh Distribution 4 field me alag alag tarikese use me aata hai. Ye kaon-kaon se hain ye dekhte hain:

1. Communications: To model multiple paths of dense scattered signals reaching a receiver.
2. Physical sciences: To model wind speed, wave heights and sound/light radiation.
3. Engineering: To measure the lifetime of an object, where the lifetime depends on the object’s age. 
For example: resistors, transformers, and capacitors in aircraft radar sets.
4. Medical: Imaging science, to model noise variance in magnetic resonance imaging.

numpy.random.rayleigh() ke arguments:

1. scale: (Standard deviation defualt 1.0) Isse kitna flat distribution hoga ye decide karte hain.
2. size: Matrix or array ka shape kitna rakhoge.
'''

import numpy.random as r
import matplotlib.pyplot as plt
import seaborn as sns

ray = r.rayleigh(size=(10))
# print('\nRay: ',ray)

# seaborn
sns.distplot(r.rayleigh(size=(100)), hist=False, label='1.0')
sns.distplot(r.rayleigh(scale=2.0, size=(100)), hist=False, label='2.0')
sns.distplot(r.rayleigh(scale=3.0, size=(100)), hist=False, label='3.0')
sns.distplot(r.rayleigh(scale=4.0, size=(100)), hist=False, label='4.0')

# plt
plt.xlabel('Rang of x')
# plt.xlim(0, 10)
# plt.ylim(0,0.5)
plt.ylabel('Range of y')
plt.title('Rayleigh Distribution')
plt.show()
