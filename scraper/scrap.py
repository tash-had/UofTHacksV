import os, time, getpass
from timeit import default_timer as timer
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Parse/Download images off H&M

chromedriver = '/Users/Rahul/Downloads/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.set_window_size(1024, 768)
driver.maximize_window()
driver.get('http://www2.hm.com/en_ca/men/shop-by-product/basics.html?product-type=men_basics%2Cmen_basics&sort=stock&offset=0&page-size=104')
time.sleep(1)
elem = driver.find_element_by_css_selector('a[target="_blank"]')
image_elem = driver.find_element_by_class_name('product-item-link')
# actionChain = ActionChains(driver)
# actionChain.context_click(elem).perform()
