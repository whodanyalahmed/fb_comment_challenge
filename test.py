from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep



browser =webdriver.Chrome("D:\\automate\\facebook_commentor\\driver\\chromedriver.exe")
# open link
browser.get('https://www.facebook.com/')
signup_elem = browser.find_element_by_id('email')
signup_elem.send_keys('daniahmedkhatri@yahoo.com')

login_elem = browser.find_element_by_id('pass')
login_elem.send_keys('State.320')

ins = browser.find_elements_by_tag_name('input')
for x in ins:
    if x.get_attribute('value') == 'Log In':
        x.click() # here logged in
        break
#then key here move to mobile version as that doesn't support javascript
browser.get('https://m.facebook.com')
el = browser.find_element_by_name('query')
el.send_keys('antony white')
el.send_keys(Keys.ENTER)
sleep(3)

temp= ''
ak = browser.find_elements_by_tag_name('a')
for a in ak:
    if a.get_attribute('href').endswith('search'):
        a.click()
        temp = a.get_attribute('href')[:a.get_attribute('href').find("?")]
        break

# CLICK TIMELINE
browser.get(temp+'?v=timeline')
sleep(10)


# find last post (occurance of comment)
as_el = browser.find_elements_by_tag_name('a')
for a in as_el:
    print(a.text)
    if 'omment' in a.text.strip():
        a.click()
        break
sleep(10)


# do actual comment
ins = browser.find_element_by_id('composerInput')
ins.send_keys('Best cars !')
# submit input
ins = browser.find_elements_by_tag_name('input')
for x in ins:
    if 'omment' in x.get_attribute('value'):
        x.click()
        break