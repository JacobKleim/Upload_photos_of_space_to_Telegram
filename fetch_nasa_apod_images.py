import os

import requests
from dotenv import load_dotenv

from utils import fetch_images


def get_nasa_image_urls(api_token,  images_quantity):
    params = {'api_key': api_token,
              'count': images_quantity}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()
    photos = response.json()
    image_urls = [photo['url'] for photo in photos]
    return image_urls


def main():
    load_dotenv()

    api_token = os.environ.get('NASA_API_TOKEN')

    filename = 'nasa_apod'
    images_quantity = 30

    fetch_images(get_nasa_image_urls(api_token, images_quantity),
                 filename, api_token)


if __name__ == '__main__':
    main()
