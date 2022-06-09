import requests
from bs4 import BeautifulSoup
import json

def create_request_and_return_json_first_link(link) -> list:
    r = requests.get(link).json()['searchResults']
    return r


def get_address_from_json_first_link(data) -> str:
    """
    return correct address form like '195027, Санкт-Петербург, Брантовская дорога, 3'
    """
    address = data['storePublic']['contacts']['streetAddress']['ru'] 
    return address


def get_latlon_from_json_first_link(data) -> list:
    """
    return correct latlon form like [59.940197, 30.41823]
    """
    latlon = data['storePublic']['contacts']['coordinates']['geometry']['coordinates'] 
    return latlon


def get_name_from_json_first_link(data) -> str:
    """
    return correct name form like 'KFC Охта Молл Санкт-Петербург'
    """
    name = data['storePublic']['title']['ru'] 
    return name


def get_phone_from_json_first_link(data) -> dict:
    """
    return raw phone data like {'number': '+79218976467', 'extensions': []}
    """
    phone = data['storePublic']['contacts']['phone'] 
    return phone


def get_working_hour_from_json_first_link(data) -> list:
    """
    return raw working_hours data form like [{'weekDay': 1, 'weekDayName': 'Monday', 'timeFrom': '10:00:00', 'timeTill': '21:45:00'},...
    """
    working_hours = data['storePublic']['openingHours']['regularDaily'] 
    return working_hours

def transform_phone_data_first_link(phones) -> list:
    """
    return correct data phones form like ['+79218976467', ['+awdaw', 'awdawd']]
    """
    keys = phones.keys()
    fast_list = []
    for i in keys:
        fast_list.append(phones[i])

    if fast_list[1] == []:
        fast_list.pop(1)
        
    return fast_list



def pop_raw_info_from_json_first_link(data) -> list:
    """
    return list [address, latlon, name, phones, working_hours]
    """
    for i in data[:1]: # не забыть убрать ограничение на записи
        address = get_address_from_json_first_link(i)
        latlon = get_latlon_from_json_first_link(i)
        name = get_name_from_json_first_link(i)
        phones = get_phone_from_json_first_link(i)
        working_hours = get_working_hour_from_json_first_link(i)
        return [address, latlon, name, phones, working_hours]





