import requests
from urllib import request
import random
from bs4 import BeautifulSoup

def tut_spider(max_pages = 3):
    page = 1
    root_url = r'https://thenewboston.com'
    while page <= max_pages:
        url = r'{}/search.php?type=1&sort=pop&page={}'.format(root_url,
                                                              str(page))
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'user-name'}):
            href = r'{}/{}'.format(root_url,
                                   link.get('href'))
            title = link.string
            #print(title)
            #print(href)
            get_single_itm_data(href)
        page += 1

def get_single_itm_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    print(soup.find(id='page-title-span').string)
    print(soup.find('div', {'class': 'profile-block'}).img.get('src'))


tut_spider(1)
