%reset -f

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import sleep
import random
import os
import pywebcopy
from pywebcopy import save_webpage
######### laptop############
''' TODO '''
from selenium.webdriver.common.by import By


# Add 682 S. Gaylord which is a non-existant address to see what the downloaded .html file looks like. 
integer_hold = [681, 682, 695]
# for i in range(600, 700, 1):
for i in integer_hold:
    browser = webdriver.Chrome()
    browser.get("https://redfin.com")
    # insert random sleep time for pull
    sleep(random.randint(2, 12))
    # input the address and then the enter key when fed into search box.
    text_str = str(i) + " " + "S Gaylord St Denver CO" + "\n"
    # more random sleep time
    sleep(random.randint(4, 8))
    # find the search box
    '''TODO '''
    # userElem = browser.find_element_by_id("search-box-input")
    ############# laptop################
    userElem= browser.find_element(By.ID,'search-box-input' )
    # feed in the text string with the appended enter key at the end into the box
    userElem.send_keys(text_str)

    """ No longer needed since using pywebcopy: 

    # write out each file with the appropriate address.
    file_str = str(i) + " " + "S Gaylord St Denver CO.html"
    with open(file_path + "/" + file_str, "w") as f:
        f.write(browser.page_source)
    # last random sleep
    sleep(random.randint(10, 20))
    """

    # set variable qual to current url include a sleep interval to let the page load before linking to the url. 
    sleep(random.randint(10, 12))

    url_string = browser.current_url
    print('the integer hold is:', integer_hold, '/n'
          'the url string is:', url_string)

    # kwargs= {'bypass_robots':True, 'project_name': 'recognisable-name'}
    save_webpage(
        url=url_string,
        project_folder="/home/robson/wash_park_scrape/pywebcopy/",
        # replace spaces in text string with dashes and lop off the '/n'
        project_name=text_str[:-1].replace(' ', '-'),
        bypass_robots=True,
        debug=True,
        open_in_browser=False,
        delay=None,
        threaded=False,
    )

    browser.close()
    '''TODO: add a line to close the browser? '''

# the path for properties that exist contains .../www.redfin.com/CO 
# whereas the path for non-existant properties contains .../www.redfin.com/city

text_str[:-1]

browser.find

""" Ended up not being able to use this. It seemed like the CTRL + S never hit the webpage 
and only the ENTER and TAB calls were fed into the page. The plan below was to use CTRL + S to then save the page but this failed. 

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


### Use below to click on webpage before saving? ###########
clickable = browser.find_element_by_id("serach-box-input")
ActionChains(browser).click(clickable).perform()

# os.chdir("./tester")


save_me = (
    ActionChains(browser)
    .key_down(Keys.CONTROL)
    .key_down("s")
    .key_up(Keys.CONTROL)
    .key_up("s")
    .key_down(Keys.F1)
    .key_up(Keys.F1)
    .key_down(Keys.F2)
    .key_up(Keys.F2)
    .key_down(Keys.TAB)
    .key_up(Keys.TAB)
    .key_down(Keys.TAB)
    .key_up(Keys.TAB)
    .key_down(Keys.ENTER)
    .key_up(Keys.ENTER)
)


save_me = (
    ActionChains(browser)
    .key_down(Keys.CONTROL)
    .key_down("s")
    .key_up(Keys.CONTROL)
    .key_up("s")
    .key_down(Keys.F1)
    .key_up(Keys.F1)
    .key_down(Keys.F2)
    .key_up(Keys.F2)
    .key_down(Keys.TAB)
    .key_up(Keys.TAB)
    .key_down(Keys.TAB)
    .key_up(Keys.TAB)
    .key_down(Keys.ENTER)
)


save_me = (
    ActionChains(browser)
    .key_down(Keys.CONTROL)
    .key_down("s")
    .key_up(Keys.CONTROL)
    .key_up("s")
    .key_down(Keys.F1)
    .key_up(Keys.F1)
    .key_down(Keys.F2)
    .key_up(Keys.F2)
    .key_down(Keys.TAB)
    .key_up(Keys.TAB)
    .key_down(Keys.ENTER)
)


save_me = (
    ActionChains(browser)
    .key_down(Keys.ENTER)
    .key_up(Keys.ENTER)
    .key_down(Keys.CONTROL)
    .key_down("s")
    .key_up(Keys.CONTROL)
    .key_up("s")
)


save_me = ActionChains(browser).key_down(Keys.CONTROL).key_down("s")


# Above will show the popup to save the file into robson/Downloads but when the ENTER is hit it just brings the pictures up rather than saving into the Downloads folder...


save_me.perform()
"""
