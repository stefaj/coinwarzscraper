import urllib3
import csv
import time
from bs4 import BeautifulSoup

url = "http://www.coinwarz.com/cryptocurrency"

i = 0

while(True):

    print('iteration ' + str(i))
    print("Pulling data from CoinWarz")

    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('GET',url)
    page = r.data.decode('utf-8')
    soup = BeautifulSoup(page)
    rows = soup.find('table', {'id':'tblCoins'} ).find('tbody').find_all('tr')

    print("Parsing")

    stuffs = []
    # rows = [rows[0]]
    for row in rows:
        cells = row.find_all('td')
        rank = cells[0].get_text().split()[0]
        coinName = cells[1].find_all('a')[0].find_all('b')[0].get_text().split(' ')[0].split()[0]
        difficulty = cells[2].find_all('span')[-1].get_text().split()[0]
        exchange_rate = cells[4].find_all('a')[0].get_text().split()[0]
        volume = cells[5].find_all('span')[0].get_text().split()[0]
        profit = cells[6].get_text().strip().split(' ')[0].split()[0]
        stuffs.append([rank,coinName,difficulty,exchange_rate,volume,profit])
    
    print("Saving to file")

    with open('data/' + str(i) + '.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['rank', 'coin', 'difficulty', 'exchangeRate', 'volume', 'profit'])
        for r in stuffs:
            spamwriter.writerow(r) 
    
    print("Sleep 30 mins")
    time.sleep(60*30) # sleep 30 mins
    i += 1
