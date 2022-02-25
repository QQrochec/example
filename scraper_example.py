"""Скрипт, осуществляющий парсинг сайта
выводит список элементов одежды и цен"""
from bs4 import BeautifulSoup
import requests

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'


def log(soup):
    models = soup.find_all('h4', class_='card-title')
    prices = soup.find_all('h5')
    catalog = [{'model': models[i].text.strip(),
                'price': prices[i].text}
               for i in range(len(models))]
    return catalog


def req(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


soup = req(url)
catalog = log(soup)
for num, el in enumerate(catalog, start=1):
    print(f'{num}: {el["model"]} за {el["price"]}')

pages = soup.find('ul', class_='pagination')
links = pages.find_all('a', class_='page-link')

urls = [link.get('href')
        for link in links]
for i in range(len(urls)-1):
    new_url = url.replace('?page=1', urls[i])
    new_soup = req(new_url)
    catalog = log(new_soup)
    for num, el in enumerate(catalog, start=num):
        print(f'{num}: {el["model"]} за {el["price"]}')
