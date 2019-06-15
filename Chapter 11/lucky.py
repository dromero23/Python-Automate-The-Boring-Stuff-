#! python3
# lucky.py - Opens Several Google search results 

import requests, sys, webbrowser, bs4

print('Googling..') #disply text while downloading the Google page

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status() # verify if url exist


# Retrive top search result links.

soup = bs4.BeautifulSoup(res.text,'html.parser')

# Open a browser tab for each result

linkElems = soup.select('.r a')

numOpen = min (5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com'+linkElems[i].get('href'))