from bs4 import BeautifulSoup
import requests
import smtplib
import os

URL = 'https://www.amazon.sg/Soundcore-Wireless-Playtime-Bluetooth-Comfortable/dp/B086MZ9HQT/'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept-Language': 'en-US,en;q=0.5'
}
EMAIL = os.environ.get('my_email')
PASSWORD = os.environ.get('password')
RECIPIENT = os.environ.get('recipient')


r = requests.get(url=URL, headers=HEADER)
soup = BeautifulSoup(r.text, features='lxml')

price = float(soup.find(name='span', class_='a-offscreen').getText()[2:])

if price < 120:
    with smtplib.SMTP('smtp-mail.outlook.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=RECIPIENT,
                            msg='Amazon price tracker,'
                                f'Hope this reaches you, the current price of the wireless earbuds is S${price}')