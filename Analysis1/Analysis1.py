#In this analysis I calculate coeficients for price to see how different variables such as amenities and location effect the price

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches



listing=pd.read_csv("../finaldata/listings_all_clean.csv", encoding = "ISO-8859-1")

#Prices more than $600 looks unreasonable and probably fake for Airbnb
fitters = listing[listing['price'] <= 600].ix[:, listing.columns != 'city']


#calculating coeficients using sklearn library

from sklearn.linear_model import LinearRegression
clf = LinearRegression()


y = fitters['price']
clf.fit(fitters.drop('price', axis='columns'), y)
coefs = list(zip(clf.coef_, fitters.drop('price', axis='columns')))


#save data to a csv
df = pd.DataFrame(coefs)
df.columns=['coef','amenities']

df.to_csv('coefs.csv')

#effect of city on the price

cities = np.unique(listing['city'])
cities_effects = [v for v in coefs if v[1] in cities]

pd.Series(data=[n[0] for n in cities_effects],
          index=[n[1] for n in cities_effects]).sort_values().plot(kind='bar')

ax = plt.gca()
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right',fontsize=14)

plt.xlabel('City',fontsize=14)
plt.ylabel('Price Change in $',fontsize=13)
plt.title('Price changes for Cities',fontsize=16)

plt.savefig('cities_coefs.png',bbox_inches='tight')
plt.show()


#positive effect of amenities on the price.
amenity_effects = [v for v in coefs[1:-4] if v[0]>10  ]
pd.Series(data=[n[0] for n in amenity_effects],
          index=[n[1] for n in amenity_effects]).sort_values().plot(kind='bar')

ax = plt.gca()
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right',fontsize=13)
plt.xlabel('Amenities',fontsize=14)
plt.ylabel('Price Change in $',fontsize=13)
plt.title('Positive Effect of Amenities on price (limited to effects +$10)',fontsize=16)
plt.savefig('positive_amenities_coefs.png',bbox_inches='tight')


plt.show()



#negative effect of amenities on the price.
amenity_effects = [v for v in coefs[1:-4] if v[0]<-10  ]
pd.Series(data=[n[0] for n in amenity_effects],
          index=[n[1] for n in amenity_effects]).sort_values().plot(kind='bar')

ax = plt.gca()
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right',fontsize=13)
plt.xlabel('Amenities',fontsize=14)
plt.ylabel('Price Change in $',fontsize=13)
plt.title('Negative Effect of Amenities on price (limited to effects -$-10)',fontsize=16)
plt.savefig('negative_amenities_coefs.png',bbox_inches='tight')
plt.show()


