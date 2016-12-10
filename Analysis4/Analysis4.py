#In this analysis I analyze the prices from calendar table for different months

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches

calendar=pd.read_csv('../finaldata/calendar_all.csv')


#Note that prices are available just for the time that the place is available
df2=calendar.dropna()
df2.loc[:,'date']=pd.to_datetime(df2['date'])

df2.index=df2['date']
price=df2['price'].groupby(pd.TimeGrouper(freq='M')).mean()
price_df=pd.DataFrame()
price_df["month"]=price.index.strftime('%Y-%B')
price_df["price"]=price.values
price_df.to_csv("price_month.csv")


plt.figure(figsize = (8, 3))
sns.barplot(x=price.index.strftime('%Y-%B'),y=price.values,color="salmon")
plt.xticks(rotation=90)
plt.xlabel('Month',fontsize=13)
plt.ylabel('Aerage Price in $',fontsize=13)
sns.plt.title('Average Price by Month - Sep 2016 to Sep 2017',fontsize=14)
ax = plt.gca()
ax.set_xticklabels(ax.get_xticklabels(),fontsize=13)
plt.savefig('barchart.png',bbox_inches='tight')
plt.show()
