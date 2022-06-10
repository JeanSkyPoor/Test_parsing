from secondary_defs import *



link = 'https://www.ziko.pl/wp-admin/admin-ajax.php?action=get_pharmacies'

r = create_request(link)


print(len(r))