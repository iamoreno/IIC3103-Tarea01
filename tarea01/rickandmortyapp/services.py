import requests
url_e = "https://rickandmortyapi.com/api/episode"
url_c = "https://rickandmortyapi.com/api/character"
url_l = "https://rickandmortyapi.com/api/location"

def get_episodes(lista, params={}):
    response = requests.get(url_e+f"/{lista}", params=params)
    if response.status_code == 200:
        return response.json()

def get_characters(params=""):
    lista = [i+1 for i in range(394)]
    response = requests.get(url_c+f"/{lista}")
    if response.status_code == 200:
        return response.json()

def get_episode_by_id(id, params = {}):
    response = requests.get(url_e+f"/{id}")
    if response.status_code == 200:
        return response.json()

def get_multiple_char(lista, params = {}):
    response = requests.get(url_c+f"/{lista}")
    if response.status_code == 200:
        return response.json()

def get_char_by_id(id, params = {}):
    response = requests.get(url_c+f"/{id}")
    if response.status_code == 200:
        return response.json()

def get_locations(params = {}):
    lista = [i+1 for i in range(76)]
    response = requests.get(url_l+f"/{lista}")
    if response.status_code == 200:
        return response.json()

def get_location_by_name(name, params={}):
    response = requests.get(url_l+"/?name="+name)
    if response.status_code == 200:
        return response.json()

def get_char_by_name(name, params={}):
    response = requests.get(url_c+"/?name="+name)
    if response.status_code == 200:
        return response.json()

def get_episode_by_name(name, params={}):
    response = requests.get(url_e+"/?name="+name)
    if response.status_code == 200:
        return response.json()
