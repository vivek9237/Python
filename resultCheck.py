from bs4 import BeautifulSoup
import webbrowser
import requests
#from twilio.rest import TwilioRestClient
url = "http://www.aai.aero/employment_news/Employee_Results.jsp"

r  = requests.get(url)
keyword = "7/2015"
count = 1
success = 0
data = r.text
soup = BeautifulSoup(data)
new =2
noResult = "file:///D:/pythonDwnlds/noResult.html"
yesResult = "file:///D:/pythonDwnlds/yesResult.html"
#def sendMessage(msgBody):
    #account_sid = "AC553028dece882cd42258cabd4e04b768"
    #auth_token = "5a49ff9269a17e5e933d89d0dc9bb938"
    #client = TwilioRestClient(account_sid, auth_token)
    #message = client.messages.create(to="+918622028912", from_="+16315150007", body= msgBody)
for link in soup.find_all('a'):
    if keyword not in link.text:
        continue
    print(link.text)
    print(link.get('href'))
    print("\n")
    for x in xrange(1):
        goUrl=link.get('href')
        if "aai.aero" not in link.get('href'):
            goUrl="http://www.aai.aero/employment_news/"+link.get('href')
        webbrowser.open(goUrl, new=new)
        count=0
        success=1
for y in xrange(success):
    webbrowser.open(yesResult, new=new)
    #sendMessage("Hi..AAI Result is out. Visit "+url+" for more. All the best.")
for z in xrange(count):
    webbrowser.open(noResult, new=new)
    #sendMessage("AAI Result not out. Scheduler will again run 2moro at this time.")
