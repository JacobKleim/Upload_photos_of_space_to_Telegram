import requests

from utils import fetch_spacex_last_launch


def get_nasa_image_urls():
    params = {'api_key': 'MYyGVtySmAkcUE1YrfZHTTSKbhf09dbXruwo0HrW',
              'count': '30'}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status
    photos_info = response.json()
    image_urls = []
    for photo_info in photos_info:
        url = photo_info['url']
        image_urls.append(url)
    return image_urls


def main():
    filename = 'nasa_apod'

    fetch_spacex_last_launch(get_nasa_image_urls(), filename)


if __name__ == '__main__':
    main()
