from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os

# create a list of files in the directory

list_dir = os.listdir(
    "/home/robson/OneDrive/C/wash_park/wash_park_scrape/Gaylord"
)

os.chdir("/home/robson/OneDrive/C/wash_park/wash_park_scrape/Gaylord")

list_dir[0]

with open(list_dir[0]) as fp:
    soup = BeautifulSoup(fp, "html.parser")

soup


#####################
# EASTON #
####################

from bs4 import BeautifulSoup
import os 

%pwd

# os.chdir("./easton")

os.listdir()

os.chdir('./easton')

for i in os.listdir():
    if ".html" in i:
        print(i)
        webpager = i

webpager

f= open(webpager, 'r')
content= f.read()

type(content)

# Find indices to string matches. 
content.index('lastSoldPrice')
type(content.index('lastSoldPrice'))
content.index('lastSoldDate')


content[
content.index('lastSoldPrice'):
content.index('lastSoldDate')+50
]




######################
soup.find_all('table')

soup.find_all('span')


# https://stackoverflow.com/questions/16248723/how-to-find-spans-with-a-specific-class-containing-specific-text-using-beautiful


soup.find_all('span', {'class': 'sold-price'})
soup.find_all('span', {'class': 'Last Sold Price'})
soup.find_all('span', {'label': 'Last Sold Price'})
soup.find_all('span', {'class': 'priceInfo'})

soup.find(942500)

dicter= json.loads(webpager)
webpager

soup.body.findAll(string='priceInfo')
