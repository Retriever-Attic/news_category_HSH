from unicodedata import category

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

from numpy.ma.core import append

category = ['Polotics' ,'Eoconomic' , 'Social' , 'World', 'IT']
df_title = pd.DataFrame()
for i in range(len(category)):
    url = "https://news.naver.com/section/10{}".format(i)
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
title_tags = soup.select('.sa_text_strong')
print(len(title_tags))
titles = []

for title_tag in title_tags:
    titles.append(title_tag.text)
print(titles)
df_section_title = pd.DataFrame(titles,columns=['title'])
df_section_title['category'] = category[i]
df_title = pd.concat([df_title,pd.DataFrame(titles)], ignore_index = True)


print(df_title.head())
print(df_title.info())
print(df_title['category'].value_counts())
df_title.to_csv('news_title.csv')
