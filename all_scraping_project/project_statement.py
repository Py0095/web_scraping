import requests
from bs4 import BeautifulSoup
import csv

def scrape_lenouvelliste():
    url = 'https://lenouvelliste.com/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='lnv-featured-article')

        data_list = []

        for article in articles:
            title = article.find('h1').text.strip()

            # Use find instead of find_all, and get the first anchor tag
            link = article.find('a')['href'] if article.find('a') else None
            
            image = article.find('img')['src'] if article.find('img') else None
            description = article.find('p').text

            data_list.append([title, link, image, description])

        save_to_csv(data_list)
        print("Web scraping completed successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")

def save_to_csv(data_list):
    csv_file = 'lenouvelliste_data.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        csv_writer.writerow(['Title', 'Link', 'Image', 'Description'])
        
        csv_writer.writerows(data_list)

if __name__ == "__main__":
    scrape_lenouvelliste()
