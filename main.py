from bs4 import BeautifulSoup
import requests
from secondary_defs import *
import json

link_1 = 'https://api.kfc.com/api/store/v2/store.get_restaurants?showClosed=true'
link_2 = 'https://www.ziko.pl/lokalizator/'
link_3 = 'https://monomax.by/map'

response_1 = create_request_and_return_json_first_link(link_1)

# print(len(response_1[0]['storePublic'])), print(type(response_1[0]['storePublic']))
# print(response_1[0]['storePublic'])
#print(type(response_1)), print(len(response_1)), print(response_1[0])
read_json_and_create_dict(response_1)