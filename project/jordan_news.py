
# -*- coding: utf-8 -*-
from time import pthread_getcpuclockid
from bs4 import BeautifulSoup
import csv
import requests

links = []
items = []

for i in range(0,19,2):
    if i == 0:
        endpoint = f"https://jo24.net/category-1/page/0-0"
    else:
        endpoint = f"https://jo24.net/category-1/page/{i}0-0"

    get_response = requests.get(endpoint)
    print(i, get_response.content)
    print(i,"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    soup = BeautifulSoup(get_response.content, 'lxml')
    print(soup.prettify())
    print(i,"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    section = soup.find('div', {'class':'box-white-inner'})
    print(section)
    print(i,"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    for li in section.find_all('div', attrs={'class':'shadw-box'}):
        item = {}
        if li.a['href']:
            item['title'] = li.a.text
            item['link'] = li.a['href']



        items.append(item)
print(items)
filename = '/home/naga/dev/Jordan_News/project/jordan_news.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['title','link'], extrasaction='ignore' , delimiter = ';')
    w.writeheader()
    print(items)
    for item in items:
        w.writerow(item)
        print(item)
