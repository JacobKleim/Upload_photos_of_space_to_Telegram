import requests
from utils import fetch_spacex_last_launch


def get_nasa_image_url():
    params = {'api_key': 'MYyGVtySmAkcUE1YrfZHTTSKbhf09dbXruwo0HrW',
              'count': '2'}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    info = response.json()
    image_urls = []
    for list_i in info:
        url = list_i['url']
        image_urls.append(url)
    return image_urls


def main():
    fetch_spacex_last_launch(get_nasa_image_url())


if __name__ == '__main__':
    main()
