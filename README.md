----------------------
##Command Line Arguments
----------------------

.. class:: no-web

    .. image:: https://github.com/mesfe/python_finalexam/blob/master/Analysis1/cities_coefs.png
        :alt: HTTPie compared to cURL
        :width: 100%
        :align: center

-------->download_data.py:

Example: python ./download_data.py -c united-states -f 2016-10-20 -t 2016-12-20

-c | -f | -t


    -c - get the country name. 
    -f - get the fromdate in this pattern: '%Y-%m-%d' 
    -s - get the todate in this pattern: '%Y-%m-%d' 

---------> Analysis_3.py


Example: python ./Analysis3.py -c boston

-c 
    -c - get the city name you want to do sentiment analysis on


-----------------
##download_data.py
-----------------

Download all the csv.gz files on airbnb website only for the country and time range giving by user. To filter the links on the airbnb webpage
http://insideairbnb.com/get-the-data.html] I used urllib library and to filter csv files to get only files for given country and time range
I splits the url and download only these files.


-------------
##concat_data.py
-------------

Here we concat all csv files across all cities for different file types. There are three types of files for each city: Listings, Reviews and Calendar.
This code concats all of the cities data for each file type and writes to listing_all.csv, reviews_all.csv, calendar_all.csv.

------------
##data_cleansing.py
------------

data cleansing on listings file:

1- converting price datatype to int. Some of the prices is saved with dollar signs and commas
2-clean the amenities column. Amenities column is saved as a set so we need to get the members of this set in a list
	In this step we want to know about presence or absence of amenities a home offers. To do that we create a dictionary of 
	all amenities offered by all homes then compare each home with this list and give True and False values
3- Select only those columns we need for analysis
4- add amnities_matrix which cotains data about presence and absence of amenities for each listing to features dataframe
5-some of the columns in the dataframe are saved as strings of the form "t" or "f". Map them to boolean values
6-Encode city column to dummy variables using get_dummies function and add it to feautures dataframe
7-fill null values with the median of the columns
8- Write the data frame to listings_all_clean.csv



-------------
##Analysis1.py
-------------

In this analysis I calculate coeficients for price to see how different variables such as amenities and location effect the price
I use sklearn library to calculate coeficients
This analysis has two parts:
1- Effect of location(city) on the price
2- Effect of amenities on the price

I draw a bar chart to show these analysis

-------------
##Analysis2.py
-------------

In this analysis I look at the market in terms of bedrooms and bathroom provided. 
To get the data set I first get the count of listings for the number of bathrooms and bedrooms and then pivot that table.
I will draw a heatmap showing the number of airbnbs of various Bathroom/Bedroom configurations. 
Not surprisingly housing availability is clustered around the 1 bed 1 bath, with dorms and such having less and large rentals having more. 

-------------
##Analysis3.py
-------------

In this analysis I will do sentiment analysis on reviews table.Sentiment analysis is a technique in natural language 
processing which aims to retrieve the "sentiment" of a piece of text—positive, negative, or neutral. This is an easy way of 
summarizing the contents of a piece of text, and one that is easily understood.
To do sentiment Analysis I will use COMMENTS column of Reviews table. So first filter data to get the not null values and also 
values for specific city given by user through command line.
using SentimentIntensityAnalyzer() function from nltk library we can get a list of four polarity scores for each comment:
compound, positivity, negativity and neutrality
I will draw a plot with 4 subplots, each for one of the polarity scores.
According to this analysis almost none of the texts are classified as having significant amounts of negativity! 
In fact, a significant amount of them are given exactly 0.0 negativity.
Although the compound score is supposed to be the best estimate of overall sentiment , the fact that negativities are ranked so lowly 
hints that we're doing a not so great job with this.

-------------
##Analysis4.py
-------------

In this analysis I analyze the prices from calendar table for different months. To do this I group by prices for different months from calendar table
and show the result in a bar chart.
Looks like in the colder months the price is lower

-------------
##Analysis5.py
-------------
In this analysis I will take a look at the number of reviews vs price. To do this first I count the number of listings from reviews table.
Then I get the mean price for each listing from listings table, then merge these two dataframe. I will show the reaults in a scatter plot.
The result shows the more expensive a listing is the lower number of reviews are!




