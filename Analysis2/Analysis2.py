#In this analysis I look at the market in terms of bedrooms and bathroom provided.
#I will draw a heatmap showing the number of airbnbs of various Bathroom/Bedroom configurations.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches

listing=pd.read_csv("../finaldata/listings_all_clean.csv", encoding = "ISO-8859-1")


#to get the data set I first get the count of listings for the number of bathrooms and bedrooms and then pivot that table
bedbath=listing[listing['price']<600].groupby(['bathrooms', 'bedrooms']).count()['price'].reset_index().pivot('bathrooms', 'bedrooms', 'price').sort_index(ascending=False)
bedbath.to_csv('listing_bed_bath.csv')
bedbath.ix[5:,0:5]


sns.heatmap(bedbath.ix[5:,0:5], fmt='.0f', annot=True, linewidths=0.5)
sns.plt.title('Count of Listings per number of Bedrooms and Bathrooms',fontsize=14)
plt.xlabel('Number of Bedrooms',fontsize=13)
plt.ylabel('Number of Bathrooms',fontsize=13)

plt.savefig('heatmap.png',bbox_inches='tight')
plt.show()
