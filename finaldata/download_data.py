#get the data

from urllib.request import urlopen
import urllib.parse as up
import urllib.request as ur
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--country', default='united-states')
args = parser.parse_args()

#download all the csv.gz files on airbnb website only for Unted States and 2016. to filter the links on the airbnb webpage
# [http://insideairbnb.com/get-the-data.html] I used urllib library and to filter csv files to get only files for United States
#in 2016 I splits the url and download only these files.
url = 'http://insideairbnb.com/get-the-data.html'
from bs4 import BeautifulSoup as bs
K=0
html = urlopen(url).read()
soup = bs(html,"lxml")
tags = soup('a')
for tag in tags:
    href =(tag.get('href', None))

    try:

        if href.endswith("csv.gz") and href.find(args.country)!=-1 and href.split("/")[-3].split("-")[0]=="2016":

            ur.urlretrieve(href,href.split("/")[-4]+"_"+href.split("/")[-3]+"_"+href.split("/")[-1])
            print(href.split("/")[-4]+"_"+href.split("/")[-3]+"_"+href.split("/")[-1])

    except:

        continue

