from traceback import print_tb
import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import date
import subprocess
URL = 'https://narutoboruto.wbijam.pl'
r = requests.get(URL)

def send_message(text):
    subprocess.Popen(['notify-send', text])

soup = BeautifulSoup(r.content, 'html5lib')
last_ep_title = ""
send_message("Started")
def update(soup):
    
    global last_ep_title
    data = soup.findAll('tr', attrs = {'class': 'lista_hover'})
    ep_list = []
    last_ep = 0
    for i,d in enumerate(data):
        if d['rel'] != "TŁUMACZENIE":
            last_ep = 0 if i-1<0 else i-1
            break
    
    text = (data[last_ep].text).split('\n')
    ep = {
            'translated': data[last_ep]['rel'] != 'TŁUMACZENIE',
            'title': text[1].strip(),
            'date': text[3].strip()
        }
    if last_ep_title == "":
        last_ep_title = ep['title']
    elif last_ep_title != ep['title']:
        send_message(f"Newest episode is available: {ep['title']}")
        last_ep_title = ep['title']
    print('Tytuł: ' + ep['title'])
    print("Kiedy: " + ep['date'])
    print("Czy można obejrzeć " + ("Tak" if ep['translated'] else "Nie") )
    print("\n")
    return ep


while True:
    today = date.today()
    formated_date = today.strftime("%d.%m.%Y")
    info = update(soup)
    if formated_date == info["date"]:
        print("Pause for 5 min")
        sleep(300)
    else:
        print("Pause for 6 hours")
        sleep(21600)