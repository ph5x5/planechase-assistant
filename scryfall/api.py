import requests
from decouple import config


def get_card_list():
    error = ''
    scryfall_url = config('SCRYFALL_URL')
    url = f"{scryfall_url}/cards/search?q=set%3Aopca"
    try:
        response = requests.get(url)
        card_list = response.json()['data']
    except Exception as e:
        error = f"Can't access the Scryfall API: {e}"
        return [], error
    return card_list, error


def get_card_image_url(number_string):
    error = ''
    try:
        number = int(number_string)
    except Exception as e:
        error = f"Can't convert pointed number to integer: {e}"
        return '', error
    card_list, error = get_card_list()
    if not error:
        try:
            image_url = card_list[number - 1]['image_uris']['normal']
        except Exception as e:
            error = f"Can't get the information from the Scryfall response: {e}"
            return '', error
    return image_url, error
