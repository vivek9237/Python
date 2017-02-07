from bs4 import BeautifulSoup

import requests

url = raw_input("Enter Search criteria: ")

r  = requests.get("https://www.google.co.in/search?q=104-272-41-00&rct=j#q=tcs&start=10")

data = r.text

soup = BeautifulSoup(data,"html.parser")

for link in soup.find_all('a'):
    print(link.text)
    
    print(link.get('href'))
    print("\n")
viv= raw_input("END")
