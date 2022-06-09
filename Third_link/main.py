from secondary_defs import *
link = 'https://monomax.by/map'


data = get_soup_data(link)
data = get_shop_forms(data)

solve_third_link(data)
    