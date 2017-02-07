from bs4 import BeautifulSoup
from unidecode import unidecode
import requests
import smtplib
import csv
import time
start_time = time.time()

##################____PARAMETERS____###########################

nameOfCSV = 'search.csv'
sendEmailTo = 'support@freelancer.com'
maxNumOfSearch = 15
searchFilter = 0 #past month
"""
searchFilter options :
		0 = no filter
		1 = past hour
		2 = past 24 hours
		3 = past month
		4 = past year
		5 = Verbatim
"""
###############################################################

emailBody = ''
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('vivek.ku.mohanty@gmail.com','9437272069')
#http://stackoverflow.com/questions/20078816/replace-non-ascii-characters-with-a-single-space



def getSearchUrl(keyword, searchFilter_):
	r  = requests.get("https://www.google.co.in/search?q="+keyword+"&rct=j")
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	if(searchFilter_ == 0):
		return "https://www.google.co.in/search?q="+keyword+"&rct=j"
	if(searchFilter_ == 1):
		searchFilterText = 'Past hour'
	else:
		if(searchFilter_ == 2):
			searchFilterText = 'Past 24 hours'
		else:
			if(searchFilter_ == 3):
				searchFilterText = 'Past week'
			else:
				if(searchFilter_ == 4):
					searchFilterText = 'Past month'
				else:
					if(searchFilter_ == 5):
						searchFilterText = 'Past year'
					else:
						if(searchFilter_ == 5):
							searchFilterText = 'Verbatim'
	for link in soup.find_all('a'):
		if(link.text == searchFilterText):
			url = link.get('href')
			break
	return getUrl(url)


def getUrl(linkG):
	url = ''
	if(linkG.startswith('/url?q=')):
		post = linkG.split('url?q=')[1]
		url = post.split('&sa=')[0]
	else:
		if(linkG.startswith('/')):
			url = 'https://www.google.com'+linkG
	return url
def nextPage(keyword,i):
	#print(keyword)
	i_ = 0
	r = requests.get('https://www.google.co.in/search?q='+keyword+'&rct=j#q='+keyword+'&start=10')
	result_=''
	prevLink_ = ''
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	#result_ += '\n--------------------------------------------------------'
	for link in soup.find_all('a'):
		if(link.text=='Verbatim' or link.text=='Reset tools'):
			i_ = 1
			continue
		linkG=link.get('href')
		if(i<=maxNumOfSearch and (i_ == 1) and (link.text is not None) and (link.text <> 'Cached') and (link.text <> 'Similar') and (link.text <> 'More info')and (link.text <> '')):
			if(link.text == '1' or link.text == '2' or link.text == '3'):
				break
			if(link.text == 'Advanced search'):
				break
			if(getUrl(linkG) == prevLink_):
				continue
			if(linkG.startswith('/url?q=') or linkG.startswith('/search')):
				url = getUrl(linkG)
				if(url.startswith('http')):
					result_ += '\n' + str(i)+'. '+link.text
					result_ += '\n'+url
					result_ += '\n'
					i+=1
					prevLink_ = url
					#print (link.text)
					#print(linkG)
	#result_ += '\n--------------------------------------------------------'
	return result_

def searchInGoogle(url):
	url.replace(" ","%20")
	result = ''
	prevLink = ''
	r = requests.get(getSearchUrl(url,searchFilter))
	#r = requests.get("https://www.google.co.in/search?q="+url+"&rct=j")
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	i=1000
	result += '\n--------------------------------------------------------'
	for link in soup.find_all('a'):
		if(link.text=='Verbatim' or link.text=='Reset tools'):
			i=1
			continue
		linkG=link.get('href')
		#if(i<=20 and (link.text is not None) and (link.text <> 'Cached') and (link.text <> 'Similar') and (link.text <> 'More info')and (link.text <> '')):
		if(i<=maxNumOfSearch and (link.text is not None) and (link.text <> 'Cached') and (link.text <> 'Similar') and (link.text <> 'More info')and (link.text <> '')):
			if(link.text == '2'):
				result += nextPage(url+'&gws_rd=cr',i)
				break
			if(link.text == 'Advanced search'):
				break
			if(getUrl(linkG) == prevLink):
					continue
			if(linkG.startswith('/url?q=') or linkG.startswith('/search')):
				url = getUrl(linkG)
				if(url.startswith('http')):
					result += '\n' + str(i)+'. '+link.text
					result += '\n'+url
					result += '\n'
					i+=1
					prevLink = url
	result += '\n--------------------------------------------------------'
	return result


with open(nameOfCSV, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print ('Searching for : '+', '.join(row))
		emailBody += '\nSearch result for : '+', '.join(row)
		emailBody += searchInGoogle(', '.join(row))
		#time.sleep(2)
print(emailBody)
finalEmailBody = ''.join([i if ord(i) < 128 else ' ' for i in emailBody])
#mail.sendmail('vivek.ku.mohanty@gmail.com',sendEmailTo,finalEmailBody)

mail.close()
print("--- %s seconds ---" % (time.time() - start_time))
viv= raw_input("END")
