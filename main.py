from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

uname = input("Username of instagram page: ")
url = "https://www.instagram.com/" + uname

driver = webdriver.Firefox()
driver.get(url)
elements = driver.find_elements_by_class_name("FFVAD")

img_counter = 2
for item in elements:
    pic_url = item.get_attribute("src")
    r = urllib.request.urlopen(pic_url)
    with open("./pics/" + str(img_counter) + ".jpg", "wb") as f:
        f.write(r.read())
    img_counter = img_counter + 1

driver.close()

