import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver  # firefx & chrome
# from msedge.selenium_tools import Edge, EdgeOptions

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')

# Extract the data you want here

# print(soup)

# driver = webdriver.Firefox()
# options = EdgeOptions()
# options.use_chrome = True
# driver = Edge(options = options)
driver = webdriver.Chrome()

driver.get(url)

# Extract the collection
soup = BeautifulSoup(driver.page_source, 'html.parser')

# resultset = soup.find_all('div', {'data-component-type': 's-result-item'})
resultset = soup.find_all('div', {'data-component-type': 's-search-result'})

# print(soup)
# print(len(resultset))
# print(resultset) # Done

# product_names = []
# for item in soup.find_all("span", class_="a-size-medium a-color-base a-text-normal"):
#     product_names.append(item.text)

# for name in product_names:
#     print(name, "\n\t")

product_names = []
product_urls = []
product_prices = []
product_ratings = []
product_review_counts = []

for item in soup.find_all("div", class_="s-result-item"):
    name = item.find("span", class_="a-size-medium a-color-base a-text-normal")
    if name is not None:
        name = name.text
    else:
        name = ""

    url = item.find("a", class_="a-link-normal a-text-normal")
    if url is not None:
        url = url["href"]
    else:
        url = ""

    price = item.find("span", class_="a-offscreen")
    if price is not None:
        price = price.text
    else:
        price = ""

    rating = item.find("span", class_="a-icon-alt")
    if rating is not None:
        rating = rating.text
    else:
        rating = ""

    review_count = item.find("div", class_="a-section a-text-center")
    if review_count is not None:
        review_count = review_count.text
    else:
        review_count = ""

    product_names.append(name)
    product_urls.append(url)
    product_prices.append(price)
    product_ratings.append(rating)
    product_review_counts.append(review_count)

for i in range(len(product_names)):
    print(i, ") Product Name: ", product_names[i], "\n")
    print("product_urls: ", product_urls[i], "\n")
    print("product_prices: ", product_prices[i], "\n")
    print("product_ratings: ", product_ratings[i], "\n")
    print("product_review_counts: ", product_review_counts[i], "\n")

# driver.quit() # this might give some driver error, so dont use it

# convert this data to csv
rows = list(zip(product_names, product_urls, product_prices,
            product_ratings, product_review_counts))

filename = "products3.csv"
header = ['Product Name', 'URL',  'Price', 'Rating', 'Review Count']

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
