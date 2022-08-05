import json
import time
from gmail import client
from nb9800 import nb9800

def get_url(config_path):
    with open(config_path, "r") as f:
        data = json.load(f)
    return data["url"]

def send_email(config_path, url, process_name):
    to = get_receiver_email(config_path)
    sender = get_sender_email(config_path)
    subject = process_name
    msgHtml = url
    msgPlain = url
    client.SendMessage(sender, to, subject, msgHtml, msgPlain)

def get_receiver_email(config_path):
    with open(config_path, "r") as f:
        data = json.load(f)
    return data["receiver_email"]

def get_sender_email(config_path):
    with open(config_path, "r") as f:
        data = json.load(f)
    return data["sender_email"]

if __name__ == "__main__":
    config_path = nb9800.get_config_path()
    url = get_url(config_path)

    found = False
    while not found:
        found, item_price = nb9800.scrape(url)
        print(found, item_price)
        time.sleep(5)

    send_email(config_path, url, f"NB9800 in Stock! @{item_price}")