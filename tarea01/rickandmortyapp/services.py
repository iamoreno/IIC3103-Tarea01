import requests
url_e = "https://rickandmortyapi.com/api/episode"
url_c = "https://rickandmortyapi.com/api/character"
url_l = "https://rickandmortyapi.com/api/location"
e_img = [0,
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707117/tarea1/1_dazehb.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707117/tarea1/2_tut89o.png',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707117/tarea1/3_xxvhhg.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707117/tarea1/4_oidbfb.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/5_rcwzdq.png',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707117/tarea1/6_wxccrc.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/7_swcu5q.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585711962/tarea1/8_zsr6n6.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/9_nj3ar5.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/10_g4kmpj.png',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/11_xaha0r.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/12_c19pbz.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/13_mlznsq.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/14_lhytw6.png',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/15_ysxrq9.png',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/16_rxjpbs.png',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/17_hvibrn.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707118/tarea1/18_chdsyr.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/19_nueyyp.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/20_e2d0rv.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/21_bwbeqn.png',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/22_vehbtf.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/23_s4mxmr.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/24_alamov.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/25_rvdaxj.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/26_bo1znr.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/27_twwheq.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/28_otprfs.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/29_fquwld.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/30_ymxffx.jpg',
         'https://res.cloudinary.com/advicesiic2513/image/upload/v1585707119/tarea1/31_ev5uss.jpg']

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
