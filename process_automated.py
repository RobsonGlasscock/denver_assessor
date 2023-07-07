%reset -f
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import datetime

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
