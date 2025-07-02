from bs4 import BeautifulSoup
import csv
import requests

url = "http://quotes.toscrape.com"
sap = "/"

with open("all.csv","w",newline="",encoding="utf-8-sig") as f:
    wrtr = csv.writer(f)
    wrtr.writerow(["Author","Quote"])
    while sap:
        res = requests.get(url+sap)
        if(res.status_code != 200):
            print("error 1")
            break
        soup = BeautifulSoup(res.text,"html.parser")
        qte = soup.find_all("div",class_="quote")
        for q in qte:
            txt = q.find("span",class_="text").text
            auth = q.find("small",class_="author").text
            wrtr.writerow([auth,txt])
        next = soup.find("li",class_="next")
        if next:
            sap = next.find("a")["href"]
            print(sap)
        else:
            sap = None
print("finish")