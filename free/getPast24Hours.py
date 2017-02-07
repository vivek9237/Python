from bs4 import BeautifulSoup

import requests

def getSearchUrl(keyword, searchFilter):
	r  = requests.get("https://www.google.co.in/search?q="+keyword+"&rct=j")
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	if(searchFilter == 0):
		return "https://www.google.co.in/search?q="+keyword+"&rct=j"
	if(searchFilter == 1):
		searchFilterText = 'Past hour'
	else:
		if(searchFilter == 2):
			searchFilterText = 'Past 24 hours'
		else:
			if(searchFilter == 3):
				searchFilterText = 'Past week'
			else:
				if(searchFilter == 4):
					searchFilterText = 'Past month'
				else:
					if(searchFilter == 5):
						searchFilterText = 'Past year'
					else:
						if(searchFilter == 5):
							searchFilterText = 'Verbatim'
	for link in soup.find_all('a'):
		if(link.text == searchFilterText):
			url = link.get('href')
			break
	return url
keyword = raw_input("Enter Search criteria: ")

print getSearchUrl(keyword , 4)



viv= raw_input("END")
