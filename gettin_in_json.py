import requests
from bs4 import BeautifulSoup
import json

res  = requests.get("http://quotes.toscrape.com")
if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    qts = soup.find_all("div",class_= "quote")
    data = []
    for q in qts:
        qt = q.find("span",class_="text").text
        auth = q.find("small",class_="author").text
        data.append({
              "qt": qt,
              "auth":auth
        })
    with open("data2.json","w",encoding="utf-8-sig") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)  #ensure_ascii ensures that special characters does not does not come with
    print(data)
else:
    print("error")