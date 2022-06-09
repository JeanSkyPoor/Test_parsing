from secondary_defs import *



link_1 = 'https://api.kfc.com/api/store/v2/store.get_restaurants?showClosed=true'
link_2 = 'https://www.ziko.pl/lokalizator/'

#Solve first link
data = create_request_and_return_json_first_link(link_1)
solve_first_link(data)

