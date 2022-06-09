from operator import add
import requests
from bs4 import BeautifulSoup
import json

def create_request_and_return_json_first_link(link):
    r = requests.get(link).json()['searchResults']
    return r


def pop_raw_info_from_json(data):
    for i in data[:1]:
        address = i['storePublic']['contacts']['streetAddress']['ru'] #195027, Санкт-Петербург, Брантовская дорога, 3
        latlon = i['storePublic']['contacts']['coordinates']['geometry']['coordinates'] #[59.940197, 30.41823]

        print(address)





