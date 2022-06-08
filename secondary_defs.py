from re import S
import requests
from bs4 import BeautifulSoup
import json

def create_request_and_return_json_first_link(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml').text
    soup = json.loads(soup)['searchResults']
    return soup


def read_phone_number(i):
    first_number = i['storePublic']['contacts']['phone']['number']
    second_number = i['storePublic']['contacts']['phone']['extensions']
    if len(second_number) == 0:
        return first_number
    else:
        return [first_number, second_number]

       

def sort_dict(dict):
    s = set()
    for dic in dict:
        for val in dict.values():
            s.add(val)
    new_dict = {}

    for i in s:
        new_dict[i] = [k for k in dict if dict[k] == i]
    sorted_tuples = sorted(new_dict.items(), key=lambda item: len(item[1]), reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}
    return sorted_dict

def read_working_hours(i):
    
    data = i['storePublic']['openingHours']['regularDaily']
    fast_dict = {}
    for i in data:        
        day = i['weekDayName']
        open_time = i['timeFrom']
        closed_time = i['timeTill']
        key = '{} - {}'.format(open_time, closed_time)
        fast_dict[day] = key
    
    
    sorted_dict = sort_dict(fast_dict)
    print(sorted_dict)

def read_json_and_create_dict(data):
    for i in data[:5]:
        # name = i['storePublic']['title']['ru']
        #address = i['storePublic']['contacts']['streetAddress']['ru']
        #talton = i['storePublic']['contacts']['coordinates']['geometry']['coordinates']
        #phones = read_phone_number(i) #two items in here
        working_hours = read_working_hours(i)

        #print(working_hours)
