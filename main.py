from bs4 import BeautifulSoup
import requests

URL = 'https://www.amazon.sg/Soundcore-Wireless-Playtime-Bluetooth-Comfortable/dp/B086MZ9HQT/'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept-Language': 'en-US,en;q=0.5'
}
r = requests.get(url=URL, headers=HEADER)
soup = BeautifulSoup(r.text, features='lxml')

price = float(soup.find(name='span', class_='a-offscreen').getText()[2:])
