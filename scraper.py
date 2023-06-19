from selenium import webdriver

browser = webdriver.Chrome()
type(browser)
browser.get("https://redfin.com")


userElem = browser.find_element_by_id("search-box-input")

# input the address and then the enter key into the search box.
userElem.send_keys("681 S Gaylord St Denver CO" + "\n")

# find the url after entering the address.
browser.current_url

from bs4 import BeautifulSoup
import requests

u = requests.get(browser.current_url)
soup = BeautifulSoup(u.text, "html.parser")

soup
