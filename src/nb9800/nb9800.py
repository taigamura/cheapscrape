import requests
from bs4 import BeautifulSoup
import json
import os

def get_config_path():
    return str(os.path.abspath(os.getcwd())) + "\\src\\nb9800\\config.json"

def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def get_target_item_number():
    with open(get_config_path(), "r") as f:
        data = json.load(f)
    return data["TARGET_ITEM_NUMBER"]

def scrape(url) -> bool:
    TARGET_ITEM_NUMBER = get_target_item_number()

    # get html
    soup = get_html(url)

    # extract all items
    items = soup.findAll("div", {"class": "text-small"})

    found = False
    found_item_price = None

    for item in items:
        item_metadata = item.findAll("b")
        item_number = item_metadata[0].next_sibling.strip()
        item_id = item_metadata[1].next_sibling.strip()
        item_price = item_metadata[2].next_sibling.strip()
        item_sales_info = item_metadata[3].next_sibling.strip()

        if (item_number == TARGET_ITEM_NUMBER and item_sales_info != ""):
            found = True
            found_item_price = item_price

    return found, found_item_price