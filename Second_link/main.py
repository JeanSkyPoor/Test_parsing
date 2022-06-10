from secondary_defs import *



link = 'https://www.ziko.pl/lokalizator/'

r = create_request_and_return_soup(link)

r = find_table(r)

print(len(r))
