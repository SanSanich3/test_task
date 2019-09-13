#!/usr/bin/env python3
import argparse
import requests
import json
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument('-U', '--url', type=str, help='Target url')
url = parser.parse_args().url

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = set()

for link in soup.find_all('a'):
    href = link.get('href')
    if href.startswith('http'):
        links.add(href)

images = set()

for image in soup.find_all('img'):
    src = image.get('src')
    if src.startswith('http'):
        images.add(src)

data = {
    'links': list(links),
    'images': list(images)
}

with open('data.json', 'w') as write_file:
    json.dump(data, write_file)

