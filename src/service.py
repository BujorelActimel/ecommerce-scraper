import requests # type: ignore
import csv
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

from bs4 import BeautifulSoup # type: ignore

# Scrape the products name and price from the given URL
def retrieve_data(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product_names = [element.text.strip() for element in soup.find_all('a', class_='offerboxtitle')]
    product_prices = [element.text.strip() for element in soup.find_all('span', id=lambda value: value and value.startswith('offerprice-'))]

    res = list(zip(product_names, product_prices))

    # Write the results to a CSV file
    with open('request-results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Product Price"])
        writer.writerows(res)

# Export the data from the given file to a excel file
def export_data(export_file: str, data_path: str):
    # ISO-8859-1 for the special characters
    data = pd.read_csv(data_path, encoding='ISO-8859-1') 
    data.to_excel(f"{export_file}.xlsx", index=False)

# Make a bar graph of the product prices
def show_graph():
    data = pd.read_csv('request-results.csv', encoding='ISO-8859-1')

    plt.figure(figsize=(10, 5))
    plt.bar(data['Product Name'], data['Product Price'])
    plt.title('Product Prices')
    plt.xlabel('Product Name')
    plt.ylabel('Product Price')
    # rotation for better visibility of the product names
    plt.xticks(rotation=90)
    plt.show()

def show_matrix():
    data = pd.read_csv('request-results.csv', encoding='ISO-8859-1')
    return data

def on_close(window):
    plt.close('all')
    window.destroy()