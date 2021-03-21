import json
import sys
import time

from os import walk
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

_, _, files = next(walk(sys.path[0]))

offline_path = sys.path[0] + '/offline.jpg'
online_path = sys.path[0] + '/online.jpg'

for file in files:
	if 'offline' in file:
		offline_path = sys.path[0] + '/' + file
	elif 'online' in file:
		online_path = sys.path[0] + '/' + file

cookie_path = sys.path[0] + '/cookies.json'

def save_cookie():
	driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
	driver.implicitly_wait(0.5)
	driver.get('https://twitter.com/login')
	upload = WebDriverWait(driver, 600).until(
	lambda driver: driver.find_element_by_xpath(
		'(//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"])')
	)
	with open(cookie_path, 'w') as file:
		json.dump(driver.get_cookies(), file)
	driver.quit()

if 'cookies.json' not in files:
	print('Cookies not found. Opening browser, please log in.')
	save_cookie()

def load_cookie(driver):
	with open(cookie_path, 'r') as file:
		cookies = json.load(file)
	for cookie in cookies:
		driver.add_cookie(cookie)

def get_img():
	if sys.argv[1] == 'offline':
		return offline_path
	return online_path

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path="/usr/bin/geckodriver")
driver.implicitly_wait(0.5)
driver.get('https://twitter.com/settings/profile')
load_cookie(driver)
upload = WebDriverWait(driver, 10).until(
	lambda driver: driver.find_element_by_xpath(
		'(//input[@class="r-8akbif r-orgf3d r-1udh08x r-u8s1d r-xjis5s r-1wyyakw"])[2]')
)
upload.send_keys(get_img())
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(5)
driver.quit()
