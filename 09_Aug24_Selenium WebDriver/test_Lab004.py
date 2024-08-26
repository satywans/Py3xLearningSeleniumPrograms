import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    chrome_options = Options()
    chrome_options.add_extension("/Users/Satywan/Downloads/adblock.crx")
    # You have to start the Chrome with an extension
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.youtube.com")
    driver.maximize_window()
    time.sleep(10)
