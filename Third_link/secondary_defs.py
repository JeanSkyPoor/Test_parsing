import requests
from bs4 import BeautifulSoup
import json


def get_soup_data(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def get_shop_forms(data) -> BeautifulSoup:
    shops = data.find_all('div', class_='shop')
    return shops
    

def save_json_file_third_link(data) -> None:

    json_object = json.dumps(data, indent = 4, ensure_ascii=False)
  
    with open("sample_third_link.json", "w") as outfile:
        outfile.write(json_object)


def get_address_and_name(shop):
    address = shop.find('p', class_='name').text.split('(')[0]
    name = shop.find('p', class_='name').text.split('(')[-1].replace(')','')
    if name == address:
        return address, 'No name'
    return address, name


def get_phone(shop) -> str:
    phone = shop.find('p', class_='phone').text.replace('(', '').replace(')', '').replace(' ', '')
    return phone

def get_all_info(shop) -> list:
    address, name = get_address_and_name(shop)
    phone = get_phone(shop)
    return [address, name, phone]


def create_json_before_save(data) -> dict:
    fast_dict = {
        "address": data[0],
        "name": data[1],
        'phones': data[2]
    }
    return fast_dict


def solve_third_link(data):
    fast_list = []
    for shop in data:
        created_info = get_all_info(shop)
        fast_list.append(create_json_before_save(created_info))
    
    save_json_file_third_link(fast_list)
