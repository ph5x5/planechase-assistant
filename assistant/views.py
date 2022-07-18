from django.shortcuts import render
from django.http import HttpResponse
from scryfall import api
import random


def index(request):
    number = ''

    args = {}
    number = request.GET['number']
    random = request.GET['random']

    random_bool = bool(random)
    if random:
        number = random.randint(1, 86)

    if number:
        image_url, error = api.get_card_image_url(number)
    else:
        image_url, error = '', ''
    args['image_url'] = image_url
    args['error'] = error
    return render(request, "index.html", args)