import os

import requests
from dotenv import load_dotenv

from utils import fetch_image, get_file_extension


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

    image_urls = get_nasa_image_urls(api_token, images_quantity)

    for url_number, url in enumerate(image_urls):
        extension = get_file_extension(url)
        if extension:
            fetch_image(url, filename, url_number,
                        extension, api_token)


if __name__ == '__main__':
    main()
