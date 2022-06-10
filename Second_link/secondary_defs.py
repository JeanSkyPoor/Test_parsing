import requests
import json
from bs4 import BeautifulSoup


def create_request_and_return_soup(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')

    return soup

def find_table(soup):

    return soup.find('table', class_='mp-pharmacies-table').text

def get_all_raw_info(data):
    for i in data:
        address = i.find('td', class_='mp-pharmacy-element')
        print(address)
        break