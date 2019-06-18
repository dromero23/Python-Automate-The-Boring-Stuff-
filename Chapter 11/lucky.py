#! python3 
# lucky. py - Open several Google search results

import requests, sys, webbrowser, bs4
from selenium import webdriver as wd 
import os
os.environ['MOZ_HEADLESS'] = '1'
print ('Googling...')

# The following is the equivalent of requests.get 
#note: the html from the requests is different from the browsers that is why 
#we are using selenium to get the html text
myurl = 'http://google.com/search?q=' + ' '.join(sys.argv[1:])
res = requests.get(myurl)
res.raise_for_status()
driver = wd.Firefox(executable_path = r'C:\Users\Daniel\Documents\Programs\Python\browserdrives\geckodriver.exe')
driver.get(myurl)


# Retrieve top search result links.
# the below is equivalent of soup = bs4.BeautifulSoup(res.text) 
soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
 
# Open a browser tab for each result.
links = soup.select('div.g div.r')
link = links[0].select('a')

numOpen = min(5, len(links))
for i in range(numOpen):
    webbrowser.open(links[i].find('a').get('href'))
	
