from secondary_defs import *




link_site = 'https://www.ziko.pl/lokalizator/'
link_json = 'https://www.ziko.pl/wp-admin/admin-ajax.php?action=get_pharmacies'
soup = create_request_and_return_soup(link_site)
json = create_request_json(link_json)
solve_second_link(soup, json)