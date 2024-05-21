import csv
import pandas as pd
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def retrieve_data(url: str):
    DP_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    DP_driver.get(url)

    DP_driver.implicitly_wait(10)

    DP_product_names = [element.text for element in DP_driver.find_elements(By.CSS_SELECTOR, 'a.offerboxtitle')]
    DP_product_prices = [element.text for element in DP_driver.find_elements(By.CSS_SELECTOR, 'span[id^="offerprice-"]')]

    DP_res = list(zip(DP_product_names, DP_product_prices))

    with open('request-results.csv', 'w', newline='') as DP_file:
        DP_writer = csv.writer(DP_file)
        DP_writer.writerow(["Product Name", "Product Price"])
        DP_writer.writerows(DP_res)

    DP_driver.quit()
def export_data(export_file: str, data_path: str):
    # ISO-8859-1 for the special characters
    DP_data = pd.read_csv(data_path, encoding='ISO-8859-1') 
    DP_data.to_excel(f"{export_file}.xlsx", index=False)

def show_graph():
    DP_data = pd.read_csv('request-results.csv', encoding='ISO-8859-1')

    plt.figure(figsize=(10, 5))
    plt.bar(DP_data['Product Name'], DP_data['Product Price'])
    plt.title('Product Prices')
    plt.xlabel('Product Name')
    plt.ylabel('Product Price')
    # rotation for better visibility of the product names
    plt.xticks(rotation=90)
    plt.show()

def show_matrix():
    DP_data = pd.read_csv('request-results.csv', encoding='ISO-8859-1')
    return DP_data

def on_close(window):
    plt.close('all')
    window.destroy()