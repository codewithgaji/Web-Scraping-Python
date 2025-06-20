from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('Books-Scraped.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Product Image", "Price", "Stock Availability"])

source = "https://books.toscrape.com/catalogue/page-{}.html"


for pages in range(1, 5):
   url = source.format(pages)
   base_url = requests.get(url).text
   soup = BeautifulSoup(base_url, 'lxml')
   products_article = soup.find_all('article', class_='product_pod')

   for products in products_article:
     prod_title = products.find('h3').text
     print(prod_title)
     print()
     prod_img = products.find('img')['src']
     prod_id = f"books.toscrape.com/{prod_img}"
     print(prod_id)
     print()

     prod_price = products.find("p", class_= "price_color").text
     print(prod_price)

     prod_availability = products.find('p', class_= 'instock availability').text
     print(prod_availability)
     csv_writer.writerow([prod_title, prod_id, prod_price, prod_availability])

   print()

csv_file.close()
print("All Data has been saved successfully!")




# source = requests.get("https://books.toscrape.com/").text
# soup = BeautifulSoup(source, 'lxml')









# prodfull_id = f"Img1{prod_id}"
