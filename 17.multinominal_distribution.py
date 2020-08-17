'''
Multinomial Distribution using Numpy random module and matplotlib.pylot by hey sushil:

Multinomial Distribution ka use binomial distribution jaisa hi hai but binomial distribution kewal 2 event ke liye work karta hai.

Jaise ki 0 ya 1 ya fir is case me baat kare to head ya teal ke liye.

But Multinomial me jab 2 se jada event hone ke chanse hote hai to iska use kiya data hai.

Isko hum is tarah bhi samjh sakte hai ki jaise python me hum condtion use karte hai but agar 2 condtion ho to kewal if aur else se kaam chal jata hai.

But jab 2 se jada condtion ho to multiple condtion ke liye elif ka use karte hai.

Wise hi yaha par probability ke case me jab aysi situaltion aye ki 2 se jada case bane ki probability hai. 

Example ke liye kah sakte hai ki hum coin ko uchal rahe hai but head ya teal ke alawa toss miss bhi ho sakta hai aur ayse case ke liye hi multinomial distribution use kiya jata hai.

Multinomial Distribution method ke arguments:

1. n - int or array like int value. Kitne event honge. Jaise dise ke case me 6 taraf hote hai
2. pvals - Ye float values hoti hain. kitni probability ho sakti hai. Jaise dice me koi bhi number ke aane ki probability: [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] hogi.
3. size - Ye int ya tuple value de sakte hain. matix measn hum kitnit bar dice ko uchalenge usko numpy me random ka use karke generate kar sakte hai.

Ye method last me return me numpy array wapas karega joki ek matrix hoga. Aue isko narray bhi kaha jata hai.
'''

import numpy.random as r
import matplotlib.pyplot as plt
# import seaborn as sns
# result of multinomial
mdResult = r.multinomial(20, [1/6.]*6, size=2)
print('\nmdResult: \n',mdResult)
# plt.hist use to show graph
'''
plt.hist() me aane wale arguments:

array result
scale: graph me hitrogram ki spacing ya density
dinsity: ye density
'''

count, bins, ignored = plt.hist(mdResult, 5, density=True)
# sns.distplot(r.multinomial(n=12, pvals=[1/6,1/6,1/6,1/6,1/6,1/6], size=1))
plt.show()

