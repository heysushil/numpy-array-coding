'''
Zipf Distribution using matplotlib.pyplot, numpy.random module and seaborn librarys by hey sushil:

Zipf Distribution ka use karke sample data find kiya jata hai. Ye discrete distribution hai. Discrete distribution ki family me kafi populer distributions hai jaise ki Binomial, Multinomial, Poisson etc.
Discrete distribution wo hai jisme ek lambi random number ki list hoti hai. Jise ki non-negative integer values.

Zipf Distribution ke baareme important points:

1. Isko waise Zita Distribution bhi kahte hain.
2. Issi ko Discreate Pareto Distribution bhi kahte hain
3. Is discrete distribution ka use:
    a. Linguistics
    b. Insurance
    c. Modeling of rare events

Zipf Distribution ka Example:

1. Kisi bhi collection me nth common term 1/n time ayga wo bhi us collection ke sabse common termse mese.
2. English me 5th common word 1/5th time kisi bhi santance me sunne ko mil jayega.
3. English me 'The' word ka use sabse jada hota hai. Uske bad sabse jada use kiye jane wala word hai 'of' aur bhi so on. Isska matlab hai hi ye kram ayse hi chalta hai.
4. Agar isko last tak le kar jaya jaye to graph me base star ke result me hame plane line show hoga. Means bahot bade result me sab equal ho jayega.

numpy.random.zipf() method ke arguments:

1. a: distribution parameter
2. size: return array shap

Zipf Distribution se related aur kuch baate:

1. Zipf's law ko probability me kuch ayse dekha jata hai ki, yaha par kise event ki hone ki frequency (f) hoti hai aur uska rank (r) hota hai.
2. Iss law ko American linguist George Kingsly Zipf (1902-1950) ne diya tha.
3. Iss law ko unhone ne English me kisi bhi word ke aane ki frequecy ko janne ke liye iss law ko diya tha. Joki aaj bahot hi popular aur Machine Learning me bahot jada useful hai.
4. Wise hi Zipf ne 1949 me issi law me ye bhi claim kiya tha ki, desh me maujud sab se bada sahar, dusre sahar se doguna bada hai aur 3rd wala se tiguna bada hai and so on. Lekin ye law kewal wahin par fit batha iska use language me ya kcuh aur case me sahi fit nahi bathta hai.

Jada jankari ke liye:
1. https://www.sciencedirect.com/topics/computer-science/zipf-distribution
2. https://www.nngroup.com/articles/zipf-curves-and-website-popularity/
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176592/
4. https://plus.maths.org/content/mystery-zipf
'''

import numpy.random as r
import matplotlib.pyplot as plt
import seaborn as sns

zipf = r.zipf(a=2, size=(1000))
# print('\n',zipf)
# print('\n',zipf[zipf<10]);exit()
sns.distplot(zipf, hist=False)

plt.xlabel('Rank X')
plt.ylabel('Frequencey Y')
plt.title('Zipf Distribution')
# plt.xlim(0,100)
# plt.ylim(0,100)

plt.show()