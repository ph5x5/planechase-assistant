from django.shortcuts import render
from django.http import HttpResponse
from scryfall import api
import random


def index(request):
    error = ''
    
    number = request.GET.get('number', '')
    get_random_plane = request.GET.get('random', 'false')

    try:
        get_random_plane_bool = bool(get_random_plane)
        if get_random_plane_bool:
            number = random.randint(1, 86)
    except Exception as e:
        error = f"Can't process the random parameter: {e}"   

    if number:
        image_url, error = api.get_card_image_url(number)
    else:
        image_url = ''

    args = {
        'image_url': image_url,
        'error': error
    }

    return render(request, "index.html", args)