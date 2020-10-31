from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import urllib.request
import time

# https://dev.to/mr_h/python-selenium-infinite-scrolling-3o12
def scroll(driver, links):
    # scroll_pause_time = 0

    last_urls = driver.find_elements_by_class_name("FFVAD")
    last_url = last_urls[-1].get_attribute("src")
    
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        new_urls = driver.find_elements_by_class_name("FFVAD")
        for i in new_urls:
            link = i.get_attribute("src")
            if link not in links:
                links.append(link)

        new_url = new_urls[-1].get_attribute("src")

        if last_url == new_url:
            break
        
        last_url = new_url


if __name__ == "__main__":
    uname = input("Username of instagram page: ")
    url = "https://www.instagram.com/" + uname

    options = Options()
    options.set_preference('permissions.default.image', 2)
    options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)

    driver = webdriver.Firefox()
    driver.get(url)

    links = []
    scroll(driver, links)
    print(links)
    # elements = driver.find_elements_by_class_name("FFVAD")
    # print(len(elements))

    img_counter = 2
    for link in links:
        r = urllib.request.urlopen(link)
        with open("./pics/" + str(img_counter) + ".jpg", "wb") as f:
            f.write(r.read())
        img_counter = img_counter + 1

    driver.close()