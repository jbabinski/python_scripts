# for n, i in enumerate('asfv'):
#     print(n,' ',i)
# print(len(set('aaaaas')))
# https://realpython.com/beautiful-soup-web-scraper-python/#step-2-scrape-html-content-from-a-page
import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/Lista')
# print(r.json)

print(BeautifulSoup(r.content, 'html.parser'))
# print(r.text)