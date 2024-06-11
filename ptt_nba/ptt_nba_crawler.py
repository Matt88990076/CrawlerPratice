import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ptt.cc/bbs/NBA/index.html"
#反爬蟲的解決方式，模仿使用者
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
response = requests.get(url , headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("div" , class_="r-ent")
data_list =[]
for a in articles:
    data = {}
    title = a.find("div" , class_="title")
    #因中間可能會有刪文的，會遇到錯誤不會繼續跑下去，故改成if 是否存在title
    if title and title.a:
        title = title.a.text
    else:
        title = "no標題"
    data ["標題"] = title

    popular = a.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["人氣"] = popular

    date = a.find("div" , class_ ="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date
    data_list.append(data)
df = pd.DataFrame(data_list)
df.to_excel("ptt_nba.xlsx" , index=False , engine="openpyxl")
#with open("ptt_nba_data.json" ,"w",encoding="utf-8") as file:
#    json.dump(data_list , file ,ensure_ascii=False ,indent=4)








#print(data_list)
    #print(f"標題:{title} 人氣:{popular} 日期:{date}")
        #判斷url是否有抓到
#if response.status_code == 200:
#    with open("output.html",'w',encoding='utf_8')as f:
#        f.write(response.text)
#    print("寫入成功")
#else:
#    print("寫入失敗")