import requests
import json

def create_request_and_return_json_first_link(link) -> list:
    r = requests.get(link).json()['searchResults']
    return r


def get_address_from_json_first_link(data) -> str:
    """
    return correct address form like '195027, Санкт-Петербург, Брантовская дорога, 3' or 'StreetAddress not found'
    """
    try:
        address = data['storePublic']['contacts']['streetAddress']['ru'] 
        return address
    except KeyError:
        return "StreetAddress not found"
        

def get_latlon_from_json_first_link(data) -> list:
    """
    return correct latlon form like [59.940197, 30.41823] or 'Cannot find latlon coordinate'
    """
    try:
        latlon = data['storePublic']['contacts']['coordinates']['geometry']['coordinates'] 
        
        return latlon
    except KeyError:
        return "Cannot find latlon coordinate"


def get_name_from_json_first_link(data) -> str:
    """
    return correct name form like 'KFC Охта Молл Санкт-Петербург' or 'Cannot find restaurant name'
    """
    try:
        name = data['storePublic']['title']['ru'] 
        return name
    except KeyError:
        return "Cannot find restaurant name"


def get_phone_from_json_first_link(data) -> dict:
    """
    return raw phone data like {'number': '+79218976467', 'extensions': []} or 'Cannot find phone numbers'
    """
    try:
        phone = data['storePublic']['contacts']['phone'] 
        return phone
    except KeyError:
        return "Cannot find phone numbers"


def get_working_hour_from_json_first_link(data) -> list:
    """
    return raw working_hours data form like [{'weekDay': 1, 'weekDayName': 'Monday', 'timeFrom': '10:00:00', 'timeTill': '21:45:00'},... or 'Cannot find working hours'
    """
    try:
        working_hours = data['storePublic']['openingHours']['regularDaily'] 
        return working_hours
    except KeyError:
        return "Cannot find working hours"


def transform_phone_data_first_link(phones) -> list:
    """
    return correct data phones form like ['+79218976467', ['+awdaw', 'awdawd']] or 'Cannot find phone numbers'
    """
    if phones == "Cannot find phone numbers":
        return "Cannot find phone numbers"
    
    keys = phones.keys()
    fast_list = []
    for i in keys:
        fast_list.append(phones[i])

    if fast_list[1] == []:
        fast_list.pop(1)

    return fast_list


def get_status_first_link(i) -> str:
    """
    return status like 'Open' or 'Cannot find status'
    """
    try:
        status = i['storePublic']['status']
        return status
    except KeyError:
        return "Cannot find status"


def pop_raw_info_from_json_first_link(i) -> list:
    """
    return list [address, latlon, name, phones, working_hours, status]
    """
    address = get_address_from_json_first_link(i)
    latlon = get_latlon_from_json_first_link(i)
    name = get_name_from_json_first_link(i)
    phones = get_phone_from_json_first_link(i)
    working_hours = get_working_hour_from_json_first_link(i)
    status = get_status_first_link(i)
    return [address, latlon, name, phones, working_hours, status]


def format_data(raw_data):
    result = []
    for key, value in raw_data.items():
        result.append({"day": key, "time": value})

    return result


def create_working_day_groups(raw_working_data):
    current_day = raw_working_data[0]
    groups = []
    current_pair = []
    for index, day in enumerate(raw_working_data):
        if index == len(raw_working_data) - 1:
            current_pair.append(day)
            groups.append(current_pair)
            break

        if day['time'] == current_day['time']:
            current_pair.append(day)
        else:
            groups.append(current_pair)
            current_day = day
            current_pair = [day]

    return groups


def format_working_day_groups(groups):
    result = []

    for group in groups:
        if len(group) == 1:
            result.append(f'{group[0]["day"]} {group[0]["time"]}')
        else:
            first_item = group[0]
            last_item = group[-1]

            result.append(f'{first_item["day"]}-{last_item["day"]} {first_item["time"]}')

    return result


def transform_working_hours_first_link(data, status) -> dict:
    if status == "Closed":
        return ["closed"]

    if type(status) == type(None):
        return "Cannot find status"

    if status == "Cannot find working hours":
        return "Cannot find working hours"

    map_days = {'Monday': 'пн',
        'Tuesday': 'вт',
        'Wednesday': 'ср',
        'Thursday': 'чт',
        'Friday':'пт',
        'Saturday': 'сб',
        'Sunday': 'вс'}

    fast_dict = {}
    try:
        for i in data:
            start_day = i['timeFrom'][:5]
            end_day = i['timeTill'][:5]
            working_hours = f'{start_day}-{end_day}'

            formatted_day = map_days[i['weekDayName']]
            fast_dict[formatted_day] = working_hours 
        
        formatted_data = format_data(fast_dict)
        working_day_groups = create_working_day_groups(formatted_data)
        working_day_result = format_working_day_groups(working_day_groups)
        return working_day_result

    except TypeError:
        return ["Cannot find working hours"]
     

def create_json_before_save_first_link(data) -> dict:
    fast_dict = {
        "address": data[0],
        "latlon": data[1],
        "name": data[2],
        "phones": data[3],
        'working_hours': data[4]
    }
    return fast_dict
    

def save_json_file_first_link(data) -> None:

    json_object = json.dumps(data, indent = 4, ensure_ascii=False)
  
    with open("sample_first_link.json", "w") as outfile:
        outfile.write(json_object)


def solve_first_link(data) -> None:
    print(f"Кол-во элементов во время запроса: {len(data)}") 
    fast_list = []

    for i in data:
        raw_data_from_json = pop_raw_info_from_json_first_link(i)
        raw_data_from_json[3] = transform_phone_data_first_link(raw_data_from_json[3])
        raw_data_from_json[4] = transform_working_hours_first_link(raw_data_from_json[4], raw_data_from_json[5])

        fast_list.append(create_json_before_save_first_link(raw_data_from_json))
    print(f"Кол-во элементов в записанном файле: {len(fast_list)}") 
    
    save_json_file_first_link(fast_list)