import csv
from bs4 import BeautifulSoup
from selenium import webdriver  # firefx & chrome

# Code to scrape the data from Amazon
product_names = []
product_urls = []
product_prices = []
product_ratings = []
product_review_counts = []

driver = webdriver.Chrome()
page_number = 1
# url2 = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

while len(product_names) < 200:
    # url = f"https://www.amazon.in/s?k=bags&page={page_number}"
    url = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{page_number}"

    driver.get(url)

    # Extract the collection
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for item in soup.find_all("div", class_="s-result-item"):
        name = item.find(
            "span", class_="a-size-medium a-color-base a-text-normal")
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

    page_number += 1

# driver.quit()

# print all data
for i in range(len(product_names)):
    print(i, ") Product Name: ", product_names[i], "\n")
    print("product_urls: ", product_urls[i], "\n")
    print("product_prices: ", product_prices[i], "\n")
    print("product_ratings: ", product_ratings[i], "\n")
    print("product_review_counts: ", product_review_counts[i], "\n")


# Code to scrape the data from Amazon

# fieldnames = ['Name', 'URL', 'Price', 'Rating', 'Number of Reviews']

# Create the CSV file and write the header row
# with open('products.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()

#     # Loop through the list of products and write a row for each product
#     for product in products:
#         writer.writerow({'Name': product['name'],
#                          'URL': product['url'],
#                          'Price': product['price'],
#                          'Rating': product['rating'],
#                          'Number of Reviews': product['reviews']})

rows = list(zip(product_names, product_urls, product_prices,
            product_ratings, product_review_counts))

filename = "products2.csv"
header = ['Product Name', 'URL',  'Price', 'Rating', 'Review Count']

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
