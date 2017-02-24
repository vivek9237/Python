from bs4 import BeautifulSoup
from unidecode import unidecode
import requests
import smtplib
import csv
import time
import sys
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
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('bot.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
#cmdargs = str(sys.argv)
start_time = time.time()
count = 0
##################____PARAMETERS____###########################
class Helper:
	def __init__(self, section, file):
		self.readline = partial(next, chain(("[{0}]\n".format(section),), file, ("",)))
config = ConfigParser.RawConfigParser(allow_no_value=True)
with open("essconfig.cfg") as ifh:
	config.readfp(Helper("Foo", ifh))
nameOfCSV = str(config.get("Foo", "nameOfCSV"))#raw_input("Enter the csv file name : ")
sendEmailTo = str(config.get("Foo", "sendEmailTo"))
maxNumOfSearch = int(config.get("Foo", "maxNumOfSearch"))
searchFilter = int(config.get("Foo", "searchFilter"))
minWait = int(config.get("Foo", "minWait"))
maxWait = int(config.get("Foo", "maxWait"))
smtp = str(config.get("Foo", "smtp"))
port = int(config.get("Foo", "port"))
userName = str(config.get("Foo", "userName"))
password = str(config.get("Foo", "password"))
subject = str(config.get("Foo", "subject"))#str(sys.argv[2])#raw_input("Enter the Subject of the mail : ")
outputFileName = "SearchResults"#str(sys.argv[3])#raw_input("Enter the output file name without extension: ")
key= str(config.get("Foo", "key"))
###############################################################
for i in sys.argv:
    count += 1
    if(str(i)=='-csvfile'):
        nameOfCSV = str(sys.argv[count])
    if(str(i)=='-subject'):
        subject = str(sys.argv[count])
    if(str(i)=='-outputfile'):
        outputFileName = str(sys.argv[count])
    if(str(i)=='-help'):
        print("\n**************HELP**************")
        print("\n*Arguments that can be passed -")
        print("\n\t-csvfile <csvFileName.csv>")
        print("\n\t-subject <Subject for Email>")
        print("\n\t-outputfile <outputFileName>")
        print("\n*Search Filters -")
        print("\n\t0 = no filter")
        print("\n\t1 = past hour")
        print("\n\t2 = past 24 hours")
        print("\n\t3 = past month")
        print("\n\t4 = past year")
        print("\n\t5 = Verbatim")
        print("\n**************END**************")
        exit()

def getKey():
	webpage = urllib2.urlopen("http://just-the-time.appspot.com/")
	internettime = webpage.read()
	dateOnline = internettime.split('-')
	year = int(dateOnline[0])
	month = int(dateOnline[1])
	if(year == 2017 and month<3):
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
		logger.info("Mail Sent.")
	except:
		logger.info("Error while sending mail.")


def introDelay():
	wait = randint(minWait,maxWait)
	logger.info("bot will wait for "+str(wait)+" secs")
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
			logger.info(searchFilterText+ " filter applied.")
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
	#logger.info(keyword)
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
					logger.info ('\n' + str(i)+'. '+link.text)
					result_ += '\n'+url
					logger.info('\n'+url)
					result_ += '\n'
					i+=1
					prevLink_ = url
					logger.info (link.text)
					logger.info(linkG)
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
			#logger.info('Connection Successful')
			continue
		linkG=link.get('href')
		if(i<=maxNumOfSearch and (link.text is not None) and (link.text <> 'Cached') and (link.text <> 'Similar') and (link.text <> 'More info')and (link.text <> '')):
			if(link.text == str(page_num)):
				result += nextPage(getUrl(linkG),page_num,i)
				#logger.info("next page ku gala")
				break
			if(link.text == 'Advanced search'):
				#logger.info("advance")
				break
			if(getUrl(linkG) == prevLink):
					continue
			if(linkG.startswith('/url?q=') or linkG.startswith('/search')):
				url = getUrl(linkG)
				if('google.com' in url):
					continue
				if(url.startswith('http')):
					result += '\n' + str(i)+'. '+link.text
					logger.info('\n' + str(i)+'. '+link.text)
					result += '\n'+url
					logger.info('\n' + str(i)+'. '+link.text)
					result += '\n'
					i+=1
					prevLink = url
	result += '\n--------------------------------------------------------'
	return result


def executeProg():
	logger.info('Program started!')
	emailBody = ''
	with open(nameOfCSV, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			logger.info ('Searching for : '+' '.join(row))
			emailBody += '\nSearch result for : '+' '.join(row)
			emailBody += searchInGoogle(' '.join(row))
	finalEmailBody = ''.join([i if (ord(i) < 128) else ' ' for i in emailBody])
	logger.info(finalEmailBody)
	logger.info("preparing searchResults.txt file..")
	f= open(outputFileName+".txt","w+")
	f.write(finalEmailBody)
	f.close
	logger.info("file prepared.")
	#sendEmail(sendEmailTo,userName,password,subject,str(finalEmailBody))
	logger.info("--- %s seconds ---" % (time.time() - start_time))
	logger.info("Time taken = "+str(int(math.floor((time.time() - start_time)/60)))+" mins and "+str(int(math.floor((time.time() - start_time)%60)))+" secs")




if(__name__=="__main__"):
	if(key == getKey()):
		executeProg()
		logger.info('Program Ended!')
	else:
		logger.info("Program Expired.")

