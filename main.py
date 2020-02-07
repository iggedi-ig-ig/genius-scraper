from bs4 import BeautifulSoup
from datetime import datetime
import requests
import sys
import os

if not os.path.exists('out/'):
    os.system('mkdir out')

to_scrape = open(sys.argv[1], 'r').readlines()

for link in [x.strip() for x in to_scrape]:
    name = link.split("/")[-1]

    resp = requests.get(link).content
    soup = BeautifulSoup(resp, 'html.parser')
    lyrics = soup.find('div', class_='lyrics')

    if lyrics is not None:
        lyrics = lyrics.getText()

        print(f'[{datetime.now().strftime("%X")}]: scraped {name}')
        with open(f'out/{name}.txt', "w") as file:
            file.write(lyrics)
