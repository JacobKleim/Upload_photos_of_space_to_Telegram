import datetime

import requests

from utils import fetch_spacex_last_launch


def get_urls_epic_nasa_image():
    params = {'api_key': 'MYyGVtySmAkcUE1YrfZHTTSKbhf09dbXruwo0HrW'}
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
    filename = 'nasa_epic'

    fetch_spacex_last_launch(get_urls_epic_nasa_image(), filename)


if __name__ == '__main__':
    main()
