from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import urllib.request
import time

def scroll(driver, links):

    # fetch all images visible
    last_urls = driver.find_elements_by_class_name("FFVAD")
    # save url from last image fetch
    last_url = last_urls[-1].get_attribute("src")
    
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        # fetch all images visible (if new loaded then they will be also saved)
        new_urls = driver.find_elements_by_class_name("FFVAD")
        # save image urls in "links" list
        for i in new_urls:
            link = i.get_attribute("src")
            if link not in links:
                links.append(link)

        # save url from new image fetch
        new_url = new_urls[-1].get_attribute("src")

        # compare last and new url to know if we are at the bottom of the
        # instagram profile page
        if last_url == new_url:
            break
        
        # catch up the last url
        last_url = new_url


if __name__ == "__main__":
    # get username and with that the url to the insta page
    uname = input("Username of instagram page: ")
    url = "https://www.instagram.com/" + uname

    # set a few options
    options = Options()
    options.set_preference('permissions.default.image', 2)
    options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
    options.headless = True

    # setup the firefox driver
    driver = webdriver.Firefox(options=options)
    # navigate to url
    driver.get(url)

    # declare link list
    links = []
    # scroll through the whole instagram profile page
    scroll(driver, links)

    # go through links, download and save images
    img_counter = 2
    for link in links:
        r = urllib.request.urlopen(link)
        with open("./pics/" + str(img_counter) + ".jpg", "wb") as f:
            f.write(r.read())
        img_counter = img_counter + 1

    # close Firefox driver
    driver.close()
