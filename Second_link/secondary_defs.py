import requests
from bs4 import BeautifulSoup
import json

def create_request_json(link):
    r = requests.get(link).json()
    return r

def create_request_and_return_soup(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')

    return soup


def find_table(soup):

    return soup.find_all('tr', class_='mp-pharmacy-element')


def get_address(json, id):
    address = json[id]["address"]
    city = json[id]["city_name"][0]
    full_address = '{}, {}'.format(address, city)
    return full_address

def get_id(i):
    id = i.get('data-mp-id')
    return id


def get_latlon(json, id):
    lat = json[id]['lat']
    lon = json[id]['lng']
    return [lat, lon]


def get_phones(i):
    phones = i.find('td', class_='mp-table-address').text.split('tel. ')[1].replace('Infolinia: ', '-').split('-')
    return phones


def get_working_hours(i):
    working_hours = i.find('td', class_='mp-table-hours').find_all('span')
    fast_list =[]

    while len(working_hours)!=0:
        first_item = working_hours.pop(0).text
        second_item = working_hours.pop(0).text
        fast_list.append([first_item, second_item])
    
    new_list = []
    for i in fast_list:
        s = ' '.join(i)
        new_list.append(s)
    return new_list


def get_name(json, id):
    name = json[id]["title"]
    return name
    

def create_dict(address, latlon, name, phones, working_hours):
    fast_dict = {
        "address": address,
        "latlon": latlon,
        "name": name,
        "phones": phones,
        "working_hours": working_hours
    }
    return fast_dict

def save_json_file_second_link(data) -> None:

    json_object = json.dumps(data, indent = 4, ensure_ascii=False)
  
    with open("sample_second_link.json", "w", encoding='utf-8') as outfile:
        outfile.write(json_object)


def solve_second_link(soup, json):
    finded_elements = find_table(soup)
    fast_list = []
    for i in finded_elements:        
        id = get_id(i)
        address = get_address(json, id)
        latlon = get_latlon(json, id)
        name = get_name(json, id)
        phones = get_phones(i)
        working_hours = get_working_hours(i)

        created_dict = create_dict(address, latlon, name, phones, working_hours)
        fast_list.append(created_dict)
    
    save_json_file_second_link(fast_list)           
