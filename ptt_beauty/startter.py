import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"
headers ={"Cookie" : "over18=1"}
response = requests.get(url , headers=headers)
soup = BeautifulSoup(response.text ,"html.parser")

spans = soup.find_all("span", class_="article-meta-value")
print(spans[2].text)