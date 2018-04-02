# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:41:25 2018

@author: Vijay
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:20:51 2018

@author: Vijay
"""

import requests
import csv
from bs4 import BeautifulSoup



f = csv.writer(open('player-names.csv', 'w'))
f.writerow(['Name','Link'])

pages = []
url = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2017'
page = requests.get(item)
soup = BeautifulSoup(page.text, 'html.parser')






#https://www.consumercomplaints.in/airtel-b100013/page/2

