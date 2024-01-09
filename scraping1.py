import requests
from bs4 import BeautifulSoup as bs

link = 'https://lenouvelliste.com/'
response = requests.get(link)

if response.status_code == 200:
    print('Tout bagay ok!')
    parsePage = bs(response.content, 'html.parser')
    all_links_href = []

    for a in parsePage.find_all('a', href=True):
        href = a.get('href')
        all_links_href.append(href)
    
    print(all_links_href)
