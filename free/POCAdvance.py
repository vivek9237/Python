from bs4 import BeautifulSoup
from unidecode import unidecode
import requests
import smtplib
import csv
import time
from random import randint
from time import sleep
import math
import ConfigParser
from functools import partial
from itertools import chain


start_time = time.time()

##################____PARAMETERS____###########################
class Helper:
	def __init__(self, section, file):
		self.readline = partial(next, chain(("[{0}]\n".format(section),), file, ("",)))
config = ConfigParser.RawConfigParser(allow_no_value=True)
with open("essconfig.cfg") as ifh:
	config.readfp(Helper("Foo", ifh))
nameOfCSV = str(config.get("Foo", "nameOfCSV"))
sendEmailTo = str(config.get("Foo", "sendEmailTo"))
maxNumOfSearch = int(config.get("Foo", "maxNumOfSearch"))
searchFilter = int(config.get("Foo", "searchFilter")) #past month
minWait = int(config.get("Foo", "minWait"))
maxWait = int(config.get("Foo", "maxWait"))
smtp = str(config.get("Foo", "smtp"))
port = int(config.get("Foo", "port"))
userName = str(config.get("Foo", "userName"))
password = str(config.get("Foo", "password"))
subject = str(config.get("Foo", "subject"))
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
"""mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('vivek.ku.mohanty@gmail.com','password')"""
#http://stackoverflow.com/questions/20078816/replace-non-ascii-characters-with-a-single-space


def introDelay():
	wait = randint(25,60)
	print("bot will wait for "+str(wait)+" secs")
	sleep(wait)

def getSearchUrl(keyword, searchFilter_):
	introDelay()
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
			print(searchFilterText+ " filter applied.")
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
def nextPage(nextPageUrl,page_num_,i):
	#print(keyword)
	page_num_ += 1
	j = 0
	introDelay()
	r = requests.get(nextPageUrl)
	result_=''
	prevLink_ = ''
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	#result_ += '\n--------------------------------------------------------'
	for link in soup.find_all('a'):
		if(link.text=='Verbatim' or link.text=='Reset tools'):
			j = 1
			continue
		linkG=link.get('href')
		if(i<=maxNumOfSearch and (j == 1) and (link.text is not None) and (link.text <> 'Cached') and (link.text <> 'Similar') and (link.text <> 'More info') and (link.text <> '')):
			if(link.text == str(page_num_)):
				result_ += nextPage(getUrl(linkG),page_num_,i)
				break
			if(link.text == 'Advanced search'):
				break
			if(getUrl(linkG) == prevLink_):
				continue
			if(linkG.startswith('/url?q=') or linkG.startswith('/search')):
				url = getUrl(linkG)
				if('google.com' in url):
					continue
				if(url.startswith('http')):
					result_ += '\n' + str(i)+'. '+link.text
					#print ('\n' + str(i)+'. '+link.text)
					result_ += '\n'+url
					#print('\n'+url)
					result_ += '\n'
					i+=1
					prevLink_ = url
					#print (link.text)
					#print(linkG)
	#result_ += '\n--------------------------------------------------------'
	return result_

def searchInGoogle(url):
	page_num = 1
	#print(url)
	url.replace(" ","%20")
	page_num += 1
	result = ''
	prevLink = ''
	introDelay()
	r = requests.get(getSearchUrl(url,searchFilter))
	#r = requests.get("https://www.google.co.in/search?q="+url+"&rct=j")
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	i=1000
	result += '\n--------------------------------------------------------'
	for link in soup.find_all('a'):
		#print("kana houchi")
		#print(link.text)
		#print(link.get('href'))
		if(link.text=='Verbatim' or link.text=='Reset tools'):
			i=1
			#print("Verbatim")
			print('Connection Successful')
			continue
		linkG=link.get('href')
		#if(i<=20 and (link.text is not None) and (link.text <> 'Cached') and (link.text <> 'Similar') and (link.text <> 'More info')and (link.text <> '')):
		if(i<=maxNumOfSearch and (link.text is not None) and (link.text <> 'Cached') and (link.text <> 'Similar') and (link.text <> 'More info')and (link.text <> '')):
			if(link.text == str(page_num)):
				result += nextPage(getUrl(linkG),page_num,i)
				#print("next page ku gala")
				break
			if(link.text == 'Advanced search'):
				#print("advance")
				break
			if(getUrl(linkG) == prevLink):
					continue
			if(linkG.startswith('/url?q=') or linkG.startswith('/search')):
				url = getUrl(linkG)
				if('google.com' in url):
					continue
				if(url.startswith('http')):
					result += '\n' + str(i)+'. '+link.text
					#print('\n' + str(i)+'. '+link.text)
					result += '\n'+url
					#print('\n' + str(i)+'. '+link.text)
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
print(emailBody)
finalEmailBody = ''.join([i if ord(i) < 128 else ' ' for i in emailBody])
#mail.sendmail('vivek.ku.mohanty@gmail.com',sendEmailTo,finalEmailBody)
#mail.sendmail('vivek.ku.mohanty@gmail.com','vivek.kumohanty@yahoo.com',finalEmailBody)

#mail.close()
print("--- %s seconds ---" % (time.time() - start_time))
print("Time taken = "+str(math.floor((time.time() - start_time)/60))+" mins and "+str(math.floor((time.time() - start_time)%60))+" secs")
viv= raw_input("END")
