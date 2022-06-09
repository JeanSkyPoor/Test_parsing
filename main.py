from bs4 import BeautifulSoup
import requests
from secondary_defs import *
import json


link_1 = 'https://api.kfc.com/api/store/v2/store.get_restaurants?showClosed=true'

#Solve first link
data = create_request_and_return_json_first_link(link_1)
solve_first_link(data)

