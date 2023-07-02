%reset -f
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os


#####################
# Single firm 
###############
# descend into parent folder
pather = "/home/robson/wash_park_scrape/pywebcopy"
os.chdir(pather)

# For all property addresses that exist this is the pattern. 
os.chdir("681-S-Gaylord-St-Denver-CO/www.redfin.com/CO/Denver/")

%pwd
%ls
# There will be one folder that is a slight variation on the address: 681-S-Gaylord-St-80209 rather than 681-S-Gaylord-St-Denver-CO

dir_descend = None
# Find the single expected directory in the current path. 
for i in os.listdir():
    dir_descend = i

# descend into that folder
os.chdir(dir_descend)
# then move into home
os.chdir("./home")

os.listdir()

file_str= os.listdir()


f = open(file_str[0], "r")
content = f.read()


# Find indices to string matches.
content.index("lastSoldPrice")
type(content.index("lastSoldPrice"))
content.index("lastSoldDate")


content[content.index("lastSoldPrice") : content.index("lastSoldDate") + 50]

stringer= content[content.index("lastSoldPrice") : content.index("lastSoldDate") + 50]

stringer
stringer.split('\\')
stringer.split('\\')[0]

# Create a master_df 
master_df = pd.DataFrame(None)

# Construct DataFrame below and not that the scalar must still be contained in a single-item list. 
df= pd.DataFrame(data={stringer.split('\\')[0]: [stringer.split('\\')[1]],stringer.split('\\')[2]: [stringer.split('\\')[3]] })

df.rename(columns={df.columns[1]: 'lastSoldDate'}, inplace=True)
df

master_df=pd.concat([master_df, df])
master_df

#########################
# All Firms 
#######################

master_df= pd.DataFrame(None)

# descend into parent folder
pather = "/home/robson/wash_park_scrape/pywebcopy/"
os.chdir(pather)

os.listdir()

for i in os.listdir():
    # print(i)
    dir_1= pather+ i +'/' + 'www.redfin.com' + '/CO' + '/Denver/'
    print(dir_1)
    try: 
    
        os.chdir(dir_1)
        print(os.listdir())
    
        dir_descend = None
        # Find the single expected directory in the current path. 
        for j in os.listdir():
            dir_descend = j
            print('j is:',j)
            print('curent dir is:', os.getcwd())
            # descend into that folder

            os.chdir(dir_descend)
            print('list of current dir:', os.listdir())
            os.chdir('./home')

            print(os.getcwd(), os.listdir())
            file_str= os.listdir()
            print('file string is:',file_str)
    
            f = open(file_str[0], "r")
            content = f.read()

            stringer= content[content.index("lastSoldPrice") : content.index("lastSoldDate") + 50]
            # Construct DataFrame below and not that the scalar must still be contained in a single-item list. 
            df= pd.DataFrame(data={stringer.split('\\')[0]: [stringer.split('\\')[1]],stringer.split('\\')[2]: [stringer.split('\\')[3]] })

            df.rename(columns={df.columns[1]: 'lastSoldDate'}, inplace=True)    
            master_df= pd.concat([master_df, df])

    except:
        pass 

master_df
######### scaffoldilng ########
os.listdir()[0]



dir_descend = None
# Find the single expected directory in the current path. 
for i in os.listdir():
    dir_descend = i

# descend into that folder
os.chdir(dir_descend)

%pwd
# then move into home
os.chdir("./home")

os.listdir()

file_str= os.listdir()


f = open(file_str[0], "r")
content = f.read()


# Find indices to string matches.
content.index("lastSoldPrice")
type(content.index("lastSoldPrice"))
content.index("lastSoldDate")


content[content.index("lastSoldPrice") : content.index("lastSoldDate") + 50]

stringer= content[content.index("lastSoldPrice") : content.index("lastSoldDate") + 50]

stringer
stringer.split('\\')
stringer.split('\\')[0]

# Construct DataFrame below and not that the scalar must still be contained in a single-item list. 
df= pd.DataFrame(data={stringer.split('\\')[0]: [stringer.split('\\')[1]],stringer.split('\\')[2]: [stringer.split('\\')[3]] })

df.rename(columns={df.columns[1]: 'lastSoldDate'}, inplace=True)
df


df

master_df
df

master_df.append(df)
df.loc[0]

pd.concat([master_df, df])

pd.DataFrame.from_records
############################################################

for i in os.listdir():
    if ".html" in i:
        print(i)
        webpager = i

webpager

f = open(webpager, "r")
content = f.read()

type(content)

# Find indices to string matches.
content.index("lastSoldPrice")
type(content.index("lastSoldPrice"))
content.index("lastSoldDate")


content[content.index("lastSoldPrice") : content.index("lastSoldDate") + 50]


######################
soup.find_all("table")

soup.find_all("span")


# https://stackoverflow.com/questions/16248723/how-to-find-spans-with-a-specific-class-containing-specific-text-using-beautiful


soup.find_all("span", {"class": "sold-price"})
soup.find_all("span", {"class": "Last Sold Price"})
soup.find_all("span", {"label": "Last Sold Price"})
soup.find_all("span", {"class": "priceInfo"})

soup.find(942500)

dicter = json.loads(webpager)
webpager

soup.body.findAll(string="priceInfo")
