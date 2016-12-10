import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--cityvar', default='boston')
args = parser.parse_args()

#Here I will do sentiment analysis on review table

#Sentiment analysis is a technique in natural language processing which aims to retrieve the "sentiment" of a piece
#of text—positive, negative, or neutral. This is an easy way of summarizing the contents of a piece of text,
#and one that is easily understood.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


reviews = pd.read_csv("../finaldata/reviews_all.csv", encoding = "ISO-8859-1",low_memory=False)

#reviews contain null values

reviews_df = [r for r in reviews['comments'] if pd.notnull(r)]

# using SentimentIntensityAnalyzer() function from nltk library give use a list of four values for each comment:
#compound, positivity, negativity and neutrality

pscore= reviews['comments'][reviews['city']==args.cityvar].apply(lambda x: sid.polarity_scores(x) if pd.notnull(x) else {'compound': 0.0, 'neg': 0.0, 'neu': 0.0, 'pos': 0.0} )

#creating a dataframe containing reviews and polarity scores
scored_reviews = pd.DataFrame()
scored_reviews[['comments','city']] = reviews[['comments','city']][reviews['city']==cityvar]
scored_reviews['compound'] = [score['compound'] for score in pscore]
scored_reviews['negativity'] = [score['neg'] for score in pscore]
scored_reviews['neutrality'] = [score['neu'] for score in pscore]
scored_reviews['positivity'] = [score['pos'] for score in pscore]

#writing the dataframe to csv

scored_reviews.to_csv(args.cityvar+"_polarity_scores.csv")

#creating a plot with 4 subplots, each for one of the polarity scores


fig, axes = plt.subplots(2, 2, sharex=False, sharey=False)

polarity= ['compound','neutrality','negativity','positivity']
color=["yellow", "red", "blue", "green"]
for i in range(2):
    for j in range(2):

        axes[i, j].hist(pd.Series(scored_reviews[polarity[i+j*2]]), color=color[i+j*2])
        axes[i,j].title.set_text(polarity[i+j*2])

plt.subplots_adjust(wspace=0.3, hspace=0.3)


fig.text(0.5, 0.02, 'Polarity Score', ha='center', va='center')
fig.text(0.02, 0.5, 'Count of Revirews for '+args.cityvar, ha='center', va='center', rotation='vertical')

plt.savefig(args.cityvar+'_subplots.png',bbox_inches='tight')

plt.show()
