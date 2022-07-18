import requests
from bs4 import BeautifulSoup
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import gmail_client
import json

def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def send_email(url, process_name):
    to = get_receiver_email()
    sender = get_sender_email()
    subject = process_name
    msgHtml = url
    msgPlain = url
    gmail_client.SendMessage(sender, to, subject, msgHtml, msgPlain)

def get_receiver_email():
    with open("./config.json", "r") as f:
        data = json.load(f)
    return data["receiver_email"]

def get_sender_email():
    with open("./config.json", "r") as f:
        data = json.load(f)
    return data["sender_email"]

def get_target_item_number():
    with open("./config.json", "r") as f:
        data = json.load(f)
    return data["TARGET_ITEM_NUMBER"]

def get_url():
    with open("./config.json", "r") as f:
        data = json.load(f)
    return data["url"]

TARGET_ITEM_NUMBER = get_target_item_number()

url = get_url()

# get html
soup = get_html(url)

# extract all items
items = soup.findAll("div", {"class": "text-small"})

for item in items:
    item_metadata = item.findAll("b")
    item_number = item_metadata[0].next_sibling.strip()
    item_id = item_metadata[1].next_sibling.strip()
    item_price = item_metadata[2].next_sibling.strip()
    item_sales_info = item_metadata[3].next_sibling.strip()

    if(item_number == TARGET_ITEM_NUMBER and item_sales_info != ""):
        send_email(url, f"Item in Stock! @{item_price}")  