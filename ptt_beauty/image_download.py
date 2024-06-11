import requests
from bs4 import BeautifulSoup
import os

def download_img(url , save_path):

    print(f"正在下載圖片:{url}")
    response = requests.get(url)
    with open(save_path ,'wb') as file:
        file.write(response.content)
    print("-" *30)
def main():
    url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"
    headers ={"Cookie" : "over18=1"}
    response = requests.get(url , headers=headers)
    soup = BeautifulSoup(response.text ,"html.parser")

    spans = soup.find_all("span", class_="article-meta-value")
    title = spans[2].text
    dir_name = f"images/{title}"

    #1.建立圖片資料夾
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    #2.
    links = soup.find_all("img")
    #allow_file_name = ["jpg","png","jpeg","gif"]
    name = 0
    for link in links:
        src = link.get("src")
        if not src:
            continue
        file_name = f"test_{name}"
        name = name + 1
        print(f"url:{src}")
        download_img(src , f"{dir_name}/{file_name}.jpg")

if __name__ == "__main__":
    main()