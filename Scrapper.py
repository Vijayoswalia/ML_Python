# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:20:51 2018

@author: Vijay
"""

import requests
import csv
from bs4 import BeautifulSoup


headers = {
   'User-Agent': 'Your Name, example.com',
   'From': 'email@example.com'
}


f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(1, 5):
   url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
   pages.append(url)


for item in pages:
   page = requests.get(item, headers= headers)
   soup = BeautifulSoup(page.text, 'html.parser')

   last_links = soup.find(class_='AlphaNav')
   last_links.decompose()

   artist_name_list = soup.find(class_='BodyText')
   artist_name_list_items = artist_name_list.find_all('a')

   for artist_name in artist_name_list_items:
       names = artist_name.contents[0]
       print (names)
       links = 'https://web.archive.org' + artist_name.get('href')

       f.writerow([names, links])



#https://www.consumercomplaints.in/airtel-b100013/page/2

