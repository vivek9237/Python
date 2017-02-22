from bs4 import BeautifulSoup
from unidecode import unidecode
import requests
import smtplib
import csv
import time
import urllib2
from datetime import datetime
from random import randint
from time import sleep
import math
import ConfigParser
from functools import partial
from itertools import chain
import email
import os
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio


start_time = time.time()

##################____PARAMETERS____###########################
class Helper:
	def __init__(self, section, file):
		self.readline = partial(next, chain(("[{0}]\n".format(section),), file, ("",)))
config = ConfigParser.RawConfigParser(allow_no_value=True)
with open("essconfig.cfg") as ifh:
	config.readfp(Helper("Foo", ifh))
nameOfCSV = raw_input("Enter the csv file name : ")#str(config.get("Foo", "nameOfCSV"))
sendEmailTo = str(config.get("Foo", "sendEmailTo"))
maxNumOfSearch = int(config.get("Foo", "maxNumOfSearch"))
searchFilter = int(config.get("Foo", "searchFilter"))
minWait = int(config.get("Foo", "minWait"))
maxWait = int(config.get("Foo", "maxWait"))
smtp = str(config.get("Foo", "smtp"))
port = int(config.get("Foo", "port"))
userName = str(config.get("Foo", "userName"))
password = str(config.get("Foo", "password"))
subject = raw_input("Enter the Subject of the mail : ")#str(config.get("Foo", "subject"))
outputFileName = raw_input("Enter the output file name without extension: ")
key= str(config.get("Foo", "key"))
###############################################################



def getKey():
	webpage = urllib2.urlopen("http://just-the-time.appspot.com/")
	internettime = webpage.read()
	dateOnline = internettime.split('-')
	year = int(dateOnline[0])
	month = int(dateOnline[1])
	if(year == 2017 and month<1):
		return 'QDS2-DVD4-SAD4-NXJ3'
	else:
		return 'HSHD-WEED-FJEK-WKWM'


def sendEmail(toAdd,username,password,subject,emailBody):
	try:
		server = smtplib.SMTP(smtp,port)
		server.ehlo()
		server.starttls()
		server.login(username,password)
		msg = email.MIMEMultipart.MIMEMultipart()
		msg['From'] = username
		msg['To'] = toAdd
		msg['Subject'] = subject
		msg.attach(MIMEText(emailBody))
		#msg.attach(MIMEText('\nsent via python', 'plain')) # just a way to say.. Ha! I use Python.
		server.sendmail(username,toAdd,msg.as_string())
		server.quit()
		print("Mail Sent.")
	except:
		print("Error while sending mail.")


def introDelay():
	wait = randint(minWait,maxWait)
	print("bot will wait for "+str(wait)+" secs")
	sleep(wait)

def getSearchUrl(keyword, searchFilter_):
	r  = requests.get("https://www.google.co.in/search?q="+keyword+"&rct=j")
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	if(searchFilter_ == 0):
		return "https://www.google.co.in/search?q="+keyword+"&rct=j"
	#introDelay()
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
	#introDelay()
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
	url.replace(" ","%20")
	page_num += 1
	result = ''
	prevLink = ''
	introDelay()
	r = requests.get(getSearchUrl(url,searchFilter))
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	i=1000
	result += '\n--------------------------------------------------------'
	for link in soup.find_all('a'):
		if(link.text=='Verbatim' or link.text=='Reset tools'):
			i=1
			#print('Connection Successful')
			continue
		linkG=link.get('href')
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


def executeProg():
	emailBody = ''
	with open(nameOfCSV, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			print ('Searching for : '+' '.join(row))
			emailBody += '\nSearch result for : '+' '.join(row)
			emailBody += searchInGoogle(' '.join(row))
	finalEmailBody = ''.join([i if (ord(i) < 128) else ' ' for i in emailBody])
	print(finalEmailBody)
	print("preparing searchResults.txt file..")
	f= open(outputFileName+".txt","w+")
	f.write(finalEmailBody)
	f.close
	print("file prepared.")
	sendEmail(sendEmailTo,userName,password,subject,str(finalEmailBody))
	print("--- %s seconds ---" % (time.time() - start_time))
	print("Time taken = "+str(int(math.floor((time.time() - start_time)/60)))+" mins and "+str(int(math.floor((time.time() - start_time)%60)))+" secs")




if(__name__=="__main__"):
	if(key == getKey()):
		executeProg()
	else:
		print("Program Expired.")
