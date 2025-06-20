import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('Quotes-scraped.csv', 'w')
csv_write = csv.writer(csv_file)
csv_write.writerow(["Author", "Quote"])


# source = requests.get("https://quotes.toscrape.com/").text
# soup = BeautifulSoup(source, 'lxml')

source = "https://quotes.toscrape.com/page/{}/"


for site_page in range(1, 5):
  url = source.format(site_page)
  base = requests.get(url).text
  soup = BeautifulSoup(base, 'lxml')

  quotes = soup.find_all('div', class_= 'quote')


  for quote in quotes:
    author = quote.find('small', class_= 'author')
    print(author.text)
    print()

    quote_text = quote.find('span', class_= 'text')
    print(quote_text.text)
    print()
    csv_write.writerow([author.text, quote_text.text])

  print()

csv_file.close()
