from bs4 import BeautifulSoup
import requests
from secondary_defs import *
import json


link_1 = 'https://api.kfc.com/api/store/v2/store.get_restaurants?showClosed=true'


data = create_request_and_return_json_first_link(link_1)
raw_data_from_json = pop_raw_info_from_json_first_link(data)

