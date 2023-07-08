%reset -f
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import datetime

pd.set_option('display.max_rows', None)
#########################
# All Firms
#######################

master_df = pd.DataFrame(None)

# descend into parent folder
pather = "/home/robson/wash_park_scrape/pywebcopy/"
os.chdir(pather)

os.listdir()

for i in os.listdir():
    dir_1 = pather + i + "/" + "www.redfin.com" + "/CO" + "/Denver/"

    try:
        os.chdir(dir_1)

        dir_descend = None
        # Find the single expected directory in the current path.
        for j in os.listdir():
            dir_descend = j

            # descend into that folder

            os.chdir(dir_descend)
            os.chdir("./home")

            file_str = os.listdir()

            f = open(file_str[0], "r")
            content = f.read()

            stringer = content[
                content.index("lastSoldPrice") : content.index("lastSoldDate")
                + 50
            ]
            # Construct DataFrame below and not that the scalar must still be contained in a single-item list.
            df = pd.DataFrame(
                data={
                    "address": j,
                    stringer.split("\\")[0]: [stringer.split("\\")[1]],
                    stringer.split("\\")[2]: [stringer.split("\\")[3]],
                }
            )

            df.rename(columns={df.columns[2]: "lastSoldDate"}, inplace=True)

            tmp = df["lastSoldDate"].loc[0]
            tmp = tmp[2:-1]
            tmp = int(tmp)
            tmp = tmp / 1000

            # convert epoch to date
            df["lastSoldDate"].iloc[0] = datetime.datetime.fromtimestamp(
                tmp
            ).strftime("%m-%d-%Y")
            # convert sale price to int
            df["lastSoldPrice"].iloc[0] = int(
                df["lastSoldPrice"].iloc[0][2:-1]
            )

            master_df = pd.concat([master_df, df])

    except:
        pass

master_df

master_df[master_df['address']=='942-S-Gaylord-St-80209']


# Find missing addresses 
os.chdir(pather)
os.listdir()

# Create a dataframe with addresses 
hand_df= pd.DataFrame(data=os.listdir(), columns=['address_hand'])
hand_df


hand_df[hand_df['address_hand']=='942-S-Gaylord-St-Denver-CO-80209']
hand_df[hand_df['address_hand']=='942-S-Gaylord--St-Denver-CO-80209']
hand_df[hand_df['address_hand']=='1175-S-Williams-St-Denver-CO-80209']


# Some houses were saved down by pywebcopy was a second hyphen between the street name and street. 

# remove the "-Denver-CO" from the address string. 

hand_df['address_hand']= hand_df['address_hand'].apply(lambda x: x.replace('-Denver-CO', ''))
hand_df

hand_df[hand_df['address_hand']=='942-S-Gaylord--St-80209']
# two hypens persists. Remove this below. 10th spot back will be a hypen if there are two 

hand_df['address_hand'][0]
hand_df['address_hand'][0][-10]

# Identify addresses that came in with double hyphens. 
hand_df['double_hypen']=hand_df['address_hand'].apply(lambda x: x[-10]=='-')

hand_df

# if double_hypen =true, the 10th position should be replaced with ''

# Scaffolding for index operations to remove the second hyphen if there are two hypens. 
# index 1738 is for 558-S-Gaylord--St-80209
hand_df['address_hand'].loc[1738]


hand_df['address_hand'].loc[1738][:-10]
hand_df['address_hand'].loc[1738][-10]
hand_df['address_hand'].loc[1738][-10:]

hand_df['address_hand'].loc[1738][:-9]
hand_df['address_hand'].loc[1738][-9]
hand_df['address_hand'].loc[1738][-9:]

hand_df['address_hand'].loc[1738][-1]


hand_df['address_hand'].loc[1738]

hand_df['address_hand'].loc[1738][:-9] + hand_df['address_hand'].loc[1738][-8:]

# Conditional logic to remove the duplicate hyphen. Note I ended up not using the double_hypen variable. 
hand_df['address_hand']= hand_df['address_hand'].apply(lambda x: x[:-9] + x[-8:] if x[-10]=='-' else x)

hand_df

# merge dataframes 

df_merged= pd.merge(hand_df, master_df, how='left', left_on='address_hand', right_on='address')
df_merged

# Any address without address, lastSoldPrice, and lastSoldDate was in the Google Maps address but not on RedFin. 
df_discrep=df_merged[df_merged['address'].isna()]

df_discrep

hand_df.shape
master_df.shape
df_discrep.shape

 # Logic check to see how many obs didn't merge and if this meets expections. p/f/r.  
hand_df.shape[0] - master_df.shape[0] == df_discrep.shape[0]

# 487 houses didn't merge with sales data. 

df_discrep[df_discrep['address']== '1175-S-Williams-St-80210']
master_df[master_df['address']== '1175-S-Williams-St-80210']
hand_df[hand_df['address_hand']== '1175-S-Williams-St-80210']

df_discrep[df_discrep['address']== '1175-S-Williams-St-80209']
master_df[master_df['address']== '1175-S-Williams-St-80209']
hand_df[hand_df['address_hand']== '1175-S-Williams-St-80209']


# Examine a few houses below. Note that for the 1175-S-Williams the link has the zipcode as 80210 but in the automated search that pulled the house the zipcode was 80209: 

# https://www.redfin.com/CO/Denver/1175-S-Williams-St-80210/home/34146228
# https://www.redfin.com/CO/Denver/983-S-Gaylord-St-80209/home/34129178
# https://www.redfin.com/CO/Denver/824-S-Franklin-St-80209/home/34127921

# Each of the above has a different layout from RedFin. There is an estimate but no sales transactions in the dataset. It only has year built, property type, lot size, and Redfin Estimate. This appears to be the reason these 487 houses. p/f/r.  

# Save the web scrape results as of around July 6th, 2023 to disk. 
df_discrep.to_csv('/home/robson/wash_park_scrape/recon/discrep.csv', index=False)

from datetime import datetime

master_df["lastSoldDate"] = master_df["lastSoldDate"].apply(
    lambda x: datetime.strptime(x, "%m-%d-%Y")
)


master_df["lastSoldPrice"] = master_df["lastSoldPrice"].astype(float)
pd.options.display.float_format = "{:,.0f}".format

master_df

master_df[master_df["lastSoldDate"] >= "2023-05-01"].sort_values(
    by="lastSoldDate", ascending=False
)
