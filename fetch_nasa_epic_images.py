import requests
import datetime

from utils import fetch_spacex_last_launch


def get_epic_nasa_image_url():
    params = {'api_key': 'MYyGVtySmAkcUE1YrfZHTTSKbhf09dbXruwo0HrW'}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status
    info_photos = response.json()[:5]
    urls = []
    for info_photo in info_photos:
        image_name = info_photo['image']
        date_string = str(info_photo['date']).split(' ')[0]
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

        date_form = date.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_form}/png/{image_name}.png'
        urls.append(image_url)
    return urls


def main():
    fetch_spacex_last_launch(get_epic_nasa_image_url())


if __name__ == '__main__':
    main()
