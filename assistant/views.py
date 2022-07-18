from django.shortcuts import render
from django.http import HttpResponse
from scryfall import api
import random


def index(request):
    number = ''

    args = {}
    number = request.GET['number']
    get_random_plane = request.GET['random']

    get_random_plane_bool = bool(get_random_plane)
    if get_random_plane_bool:
        number = random.randint(1, 86)

    if number:
        image_url, error = api.get_card_image_url(number)
    else:
        image_url, error = '', ''
    args['image_url'] = image_url
    args['error'] = error
    return render(request, "index.html", args)