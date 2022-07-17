from django.shortcuts import render
from django.http import HttpResponse
from scryfall import api


def index(request):
    number = request.GET['number']
    image_url = api.get_card_image_url(number)
    return render(request, "index.html")