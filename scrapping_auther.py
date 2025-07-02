import requests # to fetch the web page
from bs4 import BeautifulSoup #for parsing HTML and to extract data from HTML
import csv # to read and write data to csv

url = "http://quotes.toscrape.com"  # url of webpage which we want to fetch
res = requests.get(url) # fetched webpage in res

if res.status_code == 200: # for checking that web page is available or not
    sup = BeautifulSoup(res.text,"html.parser")
    qts = sup.find_all("div",class_="quote")
    with open("data.csv","w",newline="",encoding="utf-8-sig") as f:  # new line for ensuring that new no gap between rows
        wrtr = csv.writer(f)
        wrtr.writerow(["Auth","Qt"]) #to write row 

        for q in qts:
            txt = q.find("span",class_="text").text   # in single "" tag name is mentioned and class_="" class is mentioned
            auth = q.find("small",class_="author").text
            wrtr.writerow([txt,auth])
    print("quote saved to data.csv")
else:  # if web page not fetched
    print("error while retriving data")


#encoding ensures that all data comes in text form not in non english character form
