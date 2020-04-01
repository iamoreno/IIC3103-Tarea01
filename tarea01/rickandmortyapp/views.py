from django.shortcuts import render
from django.http import HttpResponse
from .services import get_episodes, get_episode_by_id, get_multiple_char, get_char_by_id, get_location_by_name, get_char_by_name
from .services import get_episode_by_name, get_characters, get_locations, e_img

def home(request):
    lista = []
    for i in range(31):
        lista.append(i+1)
    context = {
        'results': get_episodes(lista),
        'imagenes': e_img
        }
    return render(request, 'rickandmortyapp/home.html', context)

def episode(request, id):
    episode = get_episode_by_id(id)
    lista = []
    for char in episode['characters']:
        element = char.rsplit(sep = "/", maxsplit = 1)
        lista.append(int(element[1]))
    chars = get_multiple_char(lista)
    context = {
        "episode" : episode,
        "chars" : chars,
        "imagen": e_img[id]
    }
    return render(request, 'rickandmortyapp/episode.html', context)

def character(request, id):
    personaje = get_char_by_id(id)
    lista = []
    for ep in personaje['episode']:
        episode = ep.rsplit(sep = "/", maxsplit = 1)
        lista.append(int(episode[1]))
    episodes = get_episodes(lista)
    context = {
        'char': personaje,
        'episodes': episodes
    }
    return render(request, 'rickandmortyapp/character.html', context)

def characters(request):
    chars = get_characters()
    context = {
        'personajes': chars
        }
    return render(request, 'rickandmortyapp/characters.html', context)

def location(request, name):
    context = get_location_by_name(name)
    lista = []
    for char in context['results']:
        for residente in char['residents']:
            personaje = residente.rsplit(sep = "/", maxsplit = 1)
            lista.append(int(personaje[1]))
    chars = get_multiple_char(lista)
    context['characters'] = chars
    return render(request, 'rickandmortyapp/location.html', context)

def locations(request):
    locations = get_locations()
    context = {
        'lugares': locations
        }
    return render(request, 'rickandmortyapp/locations.html', context)

def search(request):
    query = request.GET.get('query')
    personajes = get_char_by_name(query)
    episodios = get_episode_by_name(query)
    lugares = get_location_by_name(query)
    context = {
        'personajes': personajes,
        'episodios': episodios,
        'lugares': lugares,
        'imagenes': e_img
    }
    return render(request, 'rickandmortyapp/search.html', context)









