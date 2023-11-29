import requests
import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs
from collections import Counter

url = 'https://quotes.toscrape.com/tag/life/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div', {'class': 'quote'})
words = []
for quote in quotes:
    quote = quote.find_all('span', {'class': 'text'})
    for i in quote:
        i = i.text.replace(",", "").replace('.', '').replace(';', '')
        words += i.split()

word_counter = Counter(words)
print(*[word for word, count in word_counter.most_common(5)])