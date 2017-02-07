from bs4 import BeautifulSoup

import requests
import smtplib
import csv
emailBody = ''
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('vivek.ku.mohanty@gmail.com','9437272069')

def searchInGoogle(url):
    url.replace(" ","%20")
    result = ''
    r  = requests.get("https://www.google.co.in/search?q="+url+"&rct=j")
    data = r.text
    soup = BeautifulSoup(data,"html.parser")
    i=0
    result += '\n--------------------------------------------------------'
    for link in soup.find_all('a'):
        i+=1
        if(i>=25 and i< 25+1 ):
            result += '\n' + str(i)+' '+link.text
            linkG=link.get('href')
            if(linkG.startswith("/")):
                result += '\nhttps://www.google.com'+linkG
            else:
                result += '\n'+linkG
            result += '\n'
    result += '\n--------------------------------------------------------'
    return result


with open('search.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print ('Searching for : '+', '.join(row))
        emailBody += '\Search result for : '+', '.join(row)
        emailBody += searchInGoogle(', '.join(row))
print(emailBody)

#mail.sendmail('vivek.ku.mohanty@gmail.com','vivek.kumohanty@yahoo.com',emailBody)

mail.close()
viv= raw_input("END")
