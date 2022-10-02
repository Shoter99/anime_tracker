import requests
from bs4 import BeautifulSoup
from time import sleep
URL = 'https://spyxfamily.wbijam.pl'
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
def update(soup):
    date = soup.findAll('tr', attrs = {'class': 'lista_hover'})
    ep_list = []
    for d in date:
        text = (d.text).split('\n')
        ep = {
            'translated': d['rel'] != 'TŁUMACZENIE',
            'title': text[1].strip(),
            'date': text[3].strip()
        }
        ep_list.append(ep)

    return ep_list

while True:
    print(update(soup))
    sleep(300)