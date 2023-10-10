import os

import requests
from dotenv import load_dotenv

from utils import fetch_images


def get_nasa_image_urls(api_token):
    params = {'api_key': api_token,
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
    load_dotenv()

    api_token = os.environ.get('NASA_API_TOKEN')

    filename = 'nasa_apod'
    fetch_images(get_nasa_image_urls(api_token), filename, api_token)


if __name__ == '__main__':
    main()
