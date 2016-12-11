#Inside the Airbnb Dataset

![ish_wc_boston4](https://cloud.githubusercontent.com/assets/14946935/21078285/701a0a28-bf37-11e6-813f-f97008a4caab.jpg)


#####What can we learn about Airbnb rentals by modeling the prices, number of listings, and reviews written by guests? In this project I do a simple analysis on Airbnb dataset available on [Airbnb Website](http://insideairbnb.com/get-the-data.html)


##Table of contents


  * [Data Collection](#data-collection)
    * [Get the Data](#get-the-data)
    * [Concat the Data](#concat-the-data)
    * [Data Cleansing](#data-cleansing)
  * [Analysis](#analysis)
    * [Price Modeling](#price-modeling)
    * [Bedrooms and Bathrooms](#bedrooms-and-bathrooms)
    * [Sentiment Analysis](#sentiment-analysis)
    * [Price vs Time](#price-vs-time)
    * [Number of Reviews vs Price](#number-of-reviews-vs-price)
  * [Conclusion](#conclusion)


##Data Collection

I will download data from Airbnb webpage which has datasets across countries for multiple cities. After cleaning the raw data, I will concat all datasets in a CSV file.

###Get the Data

I use `urllib` library to scrape the [webpage](http://insideairbnb.com/get-the-data.html) and download all csv.gz file. User can filter the download by country name in the command line with `download_data.py -c --country`. For example to get the files only for **United States**:  




```bash
$ python download_data.py -c united-states
```

###Concat the Data

Here we concat all csv files across all cities for different file types. There are three types of files for each city: Listings, Reviews and Calendar. I save data in these three files: [listing_all.csv](https://github.com/mesfe/python_finalexam/blob/master/finaldata/listing_all_sample.csv), [reviews_all.csv](https://github.com/mesfe/python_finalexam/blob/master/finaldata/reviews_all_sample.csv), [calendar_all.csv](https://github.com/mesfe/python_finalexam/blob/master/finaldata/calendar_all_sample.csv).



###Data Cleansing

I do data cleansing on listing_all.csv:  

   * converting price datatype to int. Some of the prices is saved with dollar signs and commas  
   * spliting the amenities column to multiple columns with boolean values
   * encoding city column to dummy variables using `get_dummies` function and add it to the dataframe
   * fill null values with the median of the columns  
   
The dataframe is saved in [listing_all_clean.csv](https://github.com/mesfe/python_finalexam/blob/master/finaldata/listings_all_clean.csv).


##Analysis
###Price Modeling

In this analysis I calculate coeficients for price to see how different variables such as amenities and location effect the price
I use `sklearn` library to calculate coeficients. I will consider the effect of location and effect of amenities on the price.

**1- Effect of location(city) on the price**

<img width="650" alt="location" src="https://github.com/mesfe/python_finalexam/blob/master/Analysis1/cities_coefs.png" >


We see that location does have a strong effect on the price of a listing. Unsuprisingly Portland cost 55 dollars less than average and San francisco 25 dollars more than average to rent in!


**2- Effect of amenities on the price**

<img width="800" alt="amenities_positive" src="https://github.com/mesfe/python_finalexam/blob/master/Analysis1/positive_amenities_coefs.png" >



<img width="800" alt="amenities_negative" src="https://github.com/mesfe/python_finalexam/blob/master/Analysis1/negative_amenities_coefs.png" >


According to this analysis it's not always the case that more amenities is always better. The second plot which is about the negative impact of listing amenities on the price tell us if you are a host don't list **Lock on Bedroom** and **Free Street Parking** as your place's feauture!


###Bedrooms and Bathrooms
In this analysis I look at the market in terms of bedrooms and bathroom provided. To get the data set I first get the count of listings for the number of bathrooms and bedrooms and then pivot that table. Here is the heatmap for the dataframe filtered for bedrooms less than 5 and bathrooms less than 4:

<img width="800" alt="heatmap" src="https://github.com/mesfe/python_finalexam/blob/master/Analysis2/heatmap.png" >

Not surprisingly housing availability is clustered around the 1 bed 1 bath.

###Sentiment Analysis  
In this analysis I will do sentiment analysis on reviews table. To do sentiment analysis I will use COMMENTS column of Reviews table. So first filter data to get the not null values and also values for specific city given by user through command line with  with `analysis3.py -c --cityvar`.For example to do sentiment analysis for **Boston**:  


```bash
$ python analysis3.py -c boston
``` 
using `SentimentIntensityAnalyzer()` function from `nltk` library we can get a list of four polarity scores for each comment:
compound, positivity, negativity and neutrality

<img width="800" alt="subplots" src="https://github.com/mesfe/python_finalexam/blob/master/Analysis3/boston_subplots.png" >

According to this analysis almost none of the texts are classified as having significant amounts of negativity! 
In fact, a significant amount of them are given exactly 0.0 negativity. Although the compound score is supposed to be the best estimate of overall sentiment , the fact that negativities are ranked so lowly hints that we're doing a not so great job with this.

###Price vs Time

In this analysis I analyze the prices from calendar table for different months. To do this I group by prices for different months from calendar table.

<img width="900" alt="month_price" src="https://cloud.githubusercontent.com/assets/14946935/21078215/4f3fafe4-bf35-11e6-9673-249fba454f5c.png">

And here is a bar chart to show the results.

<img width="800" alt="barchart" src="https://github.com/mesfe/python_finalexam/blob/master/Analysis4/barchart.png" >

Looks like in the colder months the price is lower!

###Number of Reviews vs Price

In this analysis I will take a look at the number of reviews vs price. To do this first I count the number of listings from reviews table. Then I get the mean price for each listing from listings table, then merge these two dataframes. I will show the reaults in a scatter plot.

<img width="800" alt="scatter" src="https://github.com/mesfe/python_finalexam/blob/master/Analysis5/scatterplot.png" >

The result shows the more expensive a listing is the lower number of reviews are!

##Conclusion
If you want to host an airbnb do it in San francisco, get a place with one bedroom and one bathroom, decrease the price in winter and don't get too excited with positive reviews!


