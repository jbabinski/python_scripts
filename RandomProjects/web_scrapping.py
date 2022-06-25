# https://realpython.com/beautiful-soup-web-scraper-python/#step-2-scrape-html-content-from-a-page
import requests
import re
from bs4 import BeautifulSoup

r = requests.get('https://www.ef.pl/przewodnik-po-angielskim/listy-slow-angielskich/1000-slow/')

page = BeautifulSoup(r.content,
                     'html.parser')

raw_list = str(page.find("div", class_="field-item even")).split('<br/>')[1:-1]
clean_list = re.findall('[a-z]{3,}', ","
                        .join(raw_list)
                        )
