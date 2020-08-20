'''
Pareto Distribution using matplotlib.pyplot, numpy.random module and seaborn librarys by hey sushil:

Pareto Distribution ka naam Itelian economist and sociologist, Vilfredo Pareto par pada hain. Isko Pareto principle bhi kahte hain.

Pareto Distribution ka use hota hai:

1. Social phenomena
2. Scientific phenomena
3. Geophysical phenomena

Pareto Distribution kya hai?

1. Pareto Distribution ko  80% 20% rule ke naam se jana jata hai.
2. Pareto Distribution kisi bhi range ke andar ke situation ko bata hai.

Pareto Distribution ke examples:

1. Customer support: Yaha par kaha jata hai ki 80% problem kewal 20% customer ko hi hoti hai.
2. Economics: World me 80% paisa 20% logo ke pass hi pada hai.
3. Human Size: Cities kam hai aur villages jada hain
4. File size: Internet me TCP Protocole use hota hai jisme few large file aur many more small files hoti hain.

Is tarike ke bahot sare example bataye ja sakte hain Pareto Distribution ke jo ki 80% 20% rule me best fit baithte hain.

Pareto Distribution ke best practical application:

1. Business Management: Is case me business me kiya gaya 20% effort jo specific alag alag business activiy karne par 80% result deta hai. Is tarike se important segments par focuss karke business ki efficency ko badhya ja sakta hai.

2. Company revenues: Is case me company dekhti hai ki 80% annual revenue kewal 20% current customers se hi aajata hai. Is tarike se company in customers ko satify karne me jada focuss karta hai. Isi tarkike se aane wale 80% compalin 20% customer se hi aate hain. Jinko resolve karne par company focuss karta hai. Aur unke satify hone par agle 20% customers ko satify karne me company lag jata hai.

3. Employee Evaluation: 80-20 ratio ka use kar ke compnay apne employee ke performance par bhi focuss karta hai. Jisme ki 80% work result company ke 20% employee se aata hai. Aur is tarike se company apne best 20% employee ko motivated rakhne ke liye rewards deta rahta hai. Aur baki employees ko hard work karne ka message bhi deta hai.

Is tarike se hi company me hone wali 80% problem company ke 20% employees ke dwara hi ki jati hai.

Pareto Distribution ki limitations:

1. 80-20 ka ratio jarui nahi hai ki hamesa 80 aur 20 me hi aaye. Ho sakta hai ki kabhi 90 aajaye to isse ye nahi ki 90+20 = 110 kar diya jaye.
2. Means Pareto Distribution ka use kar ke ye pata chal jata hai ki ratio ke behalf par kis area par jada focuss karne ki jarurat hai.
3. Pareto Distribution ya bahi bhi probabiliy ke case hamesa puri tarike se sahi nahi ho sakte hain.

numpy.random.pareto() method ke arguments:

1. a: shape parameter
2. size: shape of return array

Pareto me har value posstive hi milega.
'''

import numpy.random as r
import matplotlib.pyplot as plt
import seaborn as sns

pareto = r.pareto(a=1, size=(10))
# print('\n',pareto)

sns.distplot(r.pareto(a=1, size=(100)), hist=False, label=1)
sns.distplot(r.pareto(a=2, size=(100)), hist=False, label=2)
sns.distplot(r.pareto(a=3, size=(100)), hist=False, label=3)
sns.distplot(r.pareto(a=4, size=(100)), hist=False, label=4)

# plt
plt.xlabel('Range X')
plt.ylabel('Frequecy Y')
plt.show()

