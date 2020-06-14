from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time,sys,os
from sys import platform
print("\n\nProcessing.....")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


if platform == "linux" or platform == "linux2":
    # linux
    path = resource_path('driver/chromedriver')
else:
    path = resource_path('driver/chromedriver.exe')
    # Windows...


browser =webdriver.Chrome(path)
# open link
# link = input("Enter link: ")
# req=driver.get('https://www.facebook.com/permalink.php?story_fbid=285099952677276&id=100035318194986')

# while(True):
# if(driver.title == "Facebook" or driver.title == "Log in to Facebook | Facebook"):
browser.get('https://www.facebook.com/')
signup_elem = browser.find_element_by_id('email')
signup_elem.send_keys('youremail')

login_elem = browser.find_element_by_id('pass')
login_elem.send_keys('yourpass')

ins = browser.find_elements_by_tag_name('input')
for x in ins:
    if x.get_attribute('value') == 'Log In':
        x.click() # here logged in
        break
#then key here move to mobile version as that doesn't support javascript
time.sleep(5)
# enter post link here make sure to edit www. to m. to use mobile view
browser.get('https://m.facebook.com/enter post link here make sure link starts with m')
time.sleep(5)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
count = 0
while(count <= 1000):
    browser.find_element_by_id("composerInput").send_keys(str(count)+"\n")
    time.sleep(5)
    browser.find_element_by_css_selector("button._52jg").click()
    time.sleep(5)
    count += 1

browser.close()
print("Complete...")