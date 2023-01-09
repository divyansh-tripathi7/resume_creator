from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
from openAIchat import *

browser = webdriver.Chrome()

url = "https://www.overleaf.com/latex/templates/resume-cv/fbwkrgfrcsby"

username = "dummylogger123@gmail.com"

password = "YouGotIt@1"

browser.get(url)

selectorCSS = "#main-content > div > div > div:nth-child(1) > div.row.cta-links > div > a.btn.btn-primary.cta-link"
browser.find_element("css selector", selectorCSS).click()

emailCss = "#email"
passCSS = "#password"
loginCss = "#main-content > div.card.login-register-card > form > div.actions > button"

browser.find_element("css selector", emailCss).send_keys(username)
browser.find_element("css selector", passCSS).send_keys(password)
sleep(5)
browser.find_element("css selector", loginCss).click()
sleep(15)

## captcha maang rha h kya kru bhaiii


# selectorClass = 
selector2 = "#editor > div:nth-child(2) > div > div.cm-scroller > div.cm-content.cm-lineWrapping > div:nth-child(5) > span.tok-keyword"

body = browser.find_element("css selector", selector2)

# body.send_keys(Keys.CONTROL + "a")
body.send_keys(Keys.CONTROL + "a")
body.send_keys(Keys.CONTROL + "x")

text = codeOverLeaf
# sleep(3)
selectorClear = "#editor > div:nth-child(2) > div > div.cm-scroller > div.cm-content.cm-lineWrapping > div"
body = browser.find_element("css selector", selectorClear)
body.send_keys(text)

sleep(5)


