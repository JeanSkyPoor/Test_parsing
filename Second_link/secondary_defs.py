import requests
import json

def create_request(link):
    r = requests.get(link).json()

    return r
