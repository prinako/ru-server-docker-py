import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

load_dotenv('.env')

def get_all_cardapio(callback):
    ru_site_url = os.getenv('RUSITE')

    try:
        response_data = requests.get(ru_site_url)
        response_data.raise_for_status()

        cardapio_data = BeautifulSoup(response_data.content, 'html5lib')
        elem_selector = '#content-section > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr'

        data_keys = ['dia', 'almoco','jantar']

        parent_elems = cardapio_data.select(elem_selector)

        for parent_elem in parent_elems[1:]:

            cardapio_obj = {}

            for key, child_elem in zip(data_keys, parent_elem.find_all('td')):
                tb_data = child_elem.get_text().strip()
                p = [item.strip() for item in re.split(r'[;\n]+', tb_data.replace('\t', '').replace('VEGETARIANO:', '')) if item.strip()]

                cardapio_obj[key] = p

            cardapio_obj['dia'][1] = cardapio_obj['dia'][1].replace('/', '-') + f'-{datetime.now().year}'

            callback(cardapio_obj)

    except Exception as erro:
        print(erro)


def handle_menu_data(menu_data):
    print(menu_data)  # Replace this with your desired handling logic

get_all_cardapio(handle_menu_data)
