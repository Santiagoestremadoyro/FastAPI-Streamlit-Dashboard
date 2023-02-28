from url import url
import requests


def get_sex():
    return requests.get(url+"/all/pinguins").json()

def get_island():
    return requests.get(url+"/all/pinguins/islan").json()

def get_species():
    return requests.get(url+"/all/pinguins/specie").json()

def get_id_follow_up(id, group):
    return requests.get(url+f"/id/{id}/{group}").json()

def get_info(number, group):
    return requests.get(url+f"/info/{number}/{group}").json()

