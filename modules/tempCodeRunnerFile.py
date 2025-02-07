from bs4 import BeautifulSoup
import requests
url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
headers={"user-Agent":"Mozilla/5.0"}
r=requests.get(url,headers)
soup=BeautifulSoup(r.text,"html.parser")
cnt=0
for i in soup.select("div.KzDlHZ"):
    if cnt<5:
        print(i.get_text(strip=True))
        cnt+=1
        