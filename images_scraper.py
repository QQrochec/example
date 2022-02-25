"""Парсит изображения с первой странцы"""
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
images = soup.find_all('img', class_='card-img-top img-fluid')

for num in range(len(images)):
    link = 'https://scrapingclub.com' + images[num]['src']
    with open(f'image{num}.png', 'wb+') as file:
        file.write(requests.get(link).content)
