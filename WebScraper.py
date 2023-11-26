import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('div', class_="gs-c-promo")

for article in articles:
    title = article.find('h3').text.strip()
    link = article.find('a')['href']
    print(f"Title:  {title}\nLink: {link}\n---")


with open('news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for article in articles:
        title = article.find('h3').text.strip()
        link = article.find('a')['href']
        writer.writerow({'Title' : title, 'Link' : link})