import time, logging,selenium, sys
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
def main():
	if len(sys.argv)<3:
		print('Correct usage: clEmail.py [email] [subject]')
		sys.exit()
	browser = wd.Firefox(executable_path = r'C:\Users\Daniel\Documents\Programs\Python\browserdrives\geckodriver.exe')
	browser.get('https://gmail.com')
	try: 
		linkElem = browser.find_element_by_link_text('Sign in')
		linkElem.click() 
		browser.switch_to.window(browser.window_handles[1])
	except selenium.common.exceptions.NoSuchElementException:
		logging.debug('Saved gmail session..')
	#opens a new tab; switch to the other tab
	emailElem = browser.find_element_by_id('identifierId')
	emailElem.send_keys('email')
	emailElem.send_keys(Keys.ENTER)
	time.sleep(15)
	passElem = browser.find_element_by_css_selector("input[aria-label='Enter your password']")
	passElem.send_keys('password')
	passElem.send_keys(Keys.ENTER)
	time.sleep(15)
	composeElem = browser.find_element_by_css_selector('div.T-I.J-J5-Ji.T-I-KE.L3')
	composeElem.click()
	time.sleep(15)
	repElem = browser.find_element_by_id(':rp')
	repElem.send_keys(sys.argv[1])
	time.sleep(5)
	bodyElem = browser.find_element_by_css_selector("div[aria-label='Message Body']")
	bodyElem.send_keys(sys.argv[2])
	time.sleep(1)
	time.sleep(5)
	sendElem = browser.find_element_by_xpath("//div[text()='Send']")
	sendElem.click()
	print('Sent')
	browser.quit()

if __name__=='__main__':
	main()