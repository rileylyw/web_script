import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Set the path to the webdriver
s = Service('/Users/rileylee/Development/web_script/chromedriver')
webdriver_path = '/Users/rileylee/Development/web_script/chromedriver'

# Create a new Chrome browser
browser = webdriver.Chrome(service=s, options=chrome_options)

# Navigate to the website
browser.get('https://eapps-queue.td.gov.hk/?c=transportdep&e=retasprod&ver=v3-java-3.6.1&cver=44&man=RETAS%20Queue%20Action%20%28EN%29&cid=zh-TW&t=https%3A%2F%2Feapps.td.gov.hk%2Frepoes%2Fapp517_tc.html')

# Wait for the page to load
browser.implicitly_wait(10)

sys.exit()

# crontab -e
# min hr
# 58 23 * * * /usr/local/bin/python3 /Users/rileylee/Development/web_script/web_script.py