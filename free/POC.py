from bs4 import BeautifulSoup

import requests

import csv
emailBody = ''
with open('names.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        url = ', '.join(row)
        r  = requests.get("https://www.google.co.in/search?q="+url+"&rct=j")
        #r  = requests.get("https://www.google.co.in/search?q="+url+"&espv=2&biw=1366&bih=589&source=lnt&tbs=cdr%3A1%2Ccd_min%3A2%2F4%2F2017%2Ccd_max%3A2%2F1%2F2017&tbm=nws")
        #https://www.google.co.in/search?q=cts&espv=2&biw=1366&bih=589&source=lnt&tbs=cdr%3A1%2Ccd_min%3A2%2F4%2F2017%2Ccd_max%3A2%2F1%2F2017&tbm=nws
        data = r.text
        soup = BeautifulSoup(data,"html.parser")
        i=0
        #print('--------------------------------------------------------')
        emailBody += '\n--------------------------------------------------------'
        for link in soup.find_all('a'):
            i+=1
            if(i>=25):
                #print(str(i)+' '+link.text)
                emailBody += '\n' + str(i)+' '+link.text
                linkG=link.get('href')
                if(linkG.startswith("/")):
                    #print('www.google.com'+linkG)
                    emailBody += '\nwww.google.com'+linkG
                else:
                    #print(linkG)
                    emailBody += '\n'+linkG
                #print("\n")
                emailBody += '\n'
print(emailBody)
viv= raw_input("END")
