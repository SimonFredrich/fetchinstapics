from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import urllib.request
import time

# https://dev.to/mr_h/python-selenium-infinite-scrolling-3o12
def scroll(driver):
    # scroll_pause_time = 0

    last_urls = driver.find_elements_by_class_name("FFVAD")
    new_urls = []
    
    print("holla")
    print(driver.execute_script("return document.body.scrollHeight"))

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # # Wait to load page
        # time.sleep(scroll_pause_time)
        time.sleep(5)

        print("hlow")
        print(driver.execute_script("return document.body.scrollHeight"))

        if (len(last_urls) == len(new_urls)):
            break

        last_urls = new_urls


if __name__ == "__main__":
    uname = input("Username of instagram page: ")
    url = "https://www.instagram.com/" + uname

    options = Options()
    options.set_preference('permissions.default.image', 2)
    options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)

    driver = webdriver.Firefox()
    driver.get(url)
    scroll(driver)
    elements = driver.find_elements_by_class_name("FFVAD")

    img_counter = 2
    for item in elements:
        pic_url = item.get_attribute("src")
        r = urllib.request.urlopen(pic_url)
        with open("./pics/" + str(img_counter) + ".jpg", "wb") as f:
            f.write(r.read())
        img_counter = img_counter + 1

    driver.close()