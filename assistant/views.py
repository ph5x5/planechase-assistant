from django.shortcuts import render
from django.http import HttpResponse
from scryfall import api


def index(request):
    args = {}
    number = request.GET['number']
    image_url, error = api.get_card_image_url(number)
    args['image_url'] = image_url
    args['error'] = error
    return render(request, "index.html", args)