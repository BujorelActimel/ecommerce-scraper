import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def retrieve_data(url: str):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)

    driver.implicitly_wait(10)

    product_names = [element.text for element in driver.find_elements(By.CSS_SELECTOR, 'a.offerboxtitle')]
    product_prices = [element.text for element in driver.find_elements(By.CSS_SELECTOR, 'span[id^="offerprice-"]')]

    res = list(zip(product_names, product_prices))

    with open('request-results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Product Price"])
        writer.writerows(res)

    driver.quit()
def export_data(export_file: str, data_path: str):
    # ISO-8859-1 for the special characters
    data = pd.read_csv(data_path, encoding='ISO-8859-1') 
    data.to_excel(f"{export_file}.xlsx", index=False)

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