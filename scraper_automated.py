%reset -f
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from time import sleep
import random
import os
import pywebcopy
from pywebcopy import save_webpage
from selenium.webdriver.common.by import By
from selenium import webdriver

df_addresses = pd.read_excel("adresses.ods")

"""TODO: Remove 
for k in df_addresses.columns:
    for i in df_addresses[k].dropna().to_list():
        print(
            "k is:",
            k,
            "\n",
            "i is:",
            int(i),
            "length is:",
            len(df_addresses[k].dropna().to_list()),
        )
"""


for k in df_addresses.columns:
    for i in df_addresses[k].dropna().to_list():
        try:
            browser = webdriver.Chrome()
            browser.get("https://redfin.com")
            # insert random sleep time for pull
            sleep(random.randint(2, 12))
            # input the address and then the enter key when fed into search box.
            text_str = (
                str(int(i))
                + " "
                + "S"
                + " "
                + k
                + " "
                + "St Denver CO 80209"
                + "\n"
            )
            # more random sleep time
            sleep(random.randint(4, 8))
            # find the search box
            userElem = browser.find_element(By.ID, "search-box-input")
            # feed in the text string with the appended enter key at the end into the box
            userElem.send_keys(text_str)

            # set variable qual to current url include a sleep interval to let the page load before linking to the url.
            sleep(random.randint(10, 12))

            url_string = browser.current_url

            # kwargs= {'bypass_robots':True, 'project_name': 'recognisable-name'}
            save_webpage(
                url=url_string,
                project_folder="/home/robson/wash_park_scrape/pywebcopy/",
                # replace spaces in text string with dashes and lop off the '/n'
                project_name=text_str[:-1].replace(" ", "-"),
                bypass_robots=True,
                debug=True,
                open_in_browser=False,
                delay=None,
                threaded=False,
            )

        except:
            pass

        browser.close()

