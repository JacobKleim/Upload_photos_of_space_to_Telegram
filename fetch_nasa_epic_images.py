import os
import datetime

import requests
from dotenv import load_dotenv

from utils import fetch_images


def get_urls_epic_nasa_image(api_token):
    params = {'api_key': api_token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status
    photos_info = response.json()[:5]
    urls = []
    for photo_info in photos_info:
        image_name = photo_info['image']
        date_string = str(photo_info['date']).split(' ')[0]
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

    fetch_images(get_urls_epic_nasa_image(api_token), filename, api_token)


if __name__ == '__main__':
    main()
