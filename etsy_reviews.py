from bs4 import BeautifulSoup as bs
from selenium import webdriver
import urllib
from urllib.request import Request, urlopen
import ssl
import time
import numpy
import requests, bs4

import pandas as pd
df=pd.DataFrame()

#Getting links of every page and storing it in a list
lin=[]
for i in range(1,251):
    lk="https://www.etsy.com/in-en/c/jewelry/earrings/ear-jackets-and-climbers?ref=pagination&page="+str(i)
    lin.append(lk)

#Storing links of every item in a list and then storing them in a database   
links=[]
for n in lin:
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(n, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    for item in soup.find_all("ul",{"class": "responsive-listing-grid wt-grid wt-grid--block wt-justify-content-flex-start wt-list-unstyled wt-pl-xs-0 tab-reorder-container"}):
        for link in item.findAll("a"):
            links.append(link.get('href'))
df=df.append(links)

df.to_csv(r'C:\Users\Admin\Desktop\urlll.txt')
len(df)


#Reading the csv file containing url of every item
import pandas as pd
df=pd.read_csv(r'C:\Users\Admin\Desktop\urlll.txt')
dff=pd.DataFrame()    

df=list(df["0"])

dd=pd.read_csv(r'C:\Users\Admin\Desktop\khushi.txt')
dd.head()
dd=pd.unique(dd['https://www.etsy.com/in-en/listing/802149211/ear-climber-ear-crawler-earrings-nature?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-1&plkey=df53140a446a69e5b0a0a6a6254b33203124eda0%3A802149211&pro=1&col=1'])
done=list(dd)

links=[]
for i in df:
    if i not in done:
        links.append(i)
        
link=df[df.index(done[-1])+1: ]
len(df),len(done)+len(link)

for lin in link:
    try:
        dff=pd.DataFrame()
        headers = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(lin, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
    

        tata=[]
        for item in soup.findAll('div',{"class":'wt-grid wt-grid--block wt-mb-xs-0'}):
            total=item.select("div.wt-grid__item-xs-12 ")
            for i in total:
                ta=i.findAll("p",{"class":"wt-text-truncate--multi-line wt-break-word"})
                if len(ta)<1:
                    tata.append("")
                else:
                    tata.append(ta)

    #Getting the name of person and date of review
        name=[]
        date=[]
        for i in total:
            a=i.find("p").text
            a=a.strip().split()
            name.append(" ".join(a[:-3]))
            date.append(" ".join(a[-3:]))


    #Getting the review of product
        review=[]
        for i in tata:
            try:
                review.append(i[0].text.strip())
            except:
                review.append("")

    #Getting the ratings of product
        rating=[]
        for item in soup.findAll('span',{"class":"wt-display-inline-block wt-mr-xs-1"}):
            rr=item.text.strip().split("\n")
            rating.append(rr)

        rating=rating[2:]
        rating

    #
        if len(name)==len(date)==len(review)==len(rating):
            print(True)
            done.append(lin)
            print(len(done))
            for i in range(len(name)):
                semi={'Name':name[i], 'Date':date[i], 'Review':review[i], 'Rating':rating[i][0] ,"URL":lin}
                dff=dff.append(semi,ignore_index=True)
        else:
            print("error",lin)
            continue
        #append_df_to_excel(r"C:\Users\Admin\Desktop\khushin1.xlsx", dff,header=False ,index=False)
        dff.to_csv(r"C:\Users\Admin\Desktop\khushi.txt", mode='a', header=False)
    except:
        print("error",lin)
        
done=pd.DataFrame(done)
append_df_to_excel(r"C:\Users\Admin\Desktop\khushiurl.xlsx", done,header=False, index=False)        
























