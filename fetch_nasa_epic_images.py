import os
import datetime

import requests
from dotenv import load_dotenv

from utils import fetch_images


def get_urls_epic_nasa_image(api_token, images_quantity):
    params = {'api_key': api_token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status()
    photos = response.json()[:images_quantity]
    urls = []
    for photo in photos:
        image_name = photo['image']
        date_string = str(photo['date']).split(' ')[0]
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        date_form = date.strftime('%Y/%m/%d')
        image_url = ('https://api.nasa.gov/EPIC/archive/natural/'
                     f'{date_form}/png/{image_name}.png')
        urls.append(image_url)
    return urls


def main():
    load_dotenv()

    api_token = os.environ.get('NASA_API_TOKEN')

    filename = 'nasa_epic'

    images_quantity = 5

    fetch_images(get_urls_epic_nasa_image(api_token, images_quantity),
                 filename, api_token)


if __name__ == '__main__':
    main()
