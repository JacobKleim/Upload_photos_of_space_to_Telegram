import os
from os.path import splitext
from pathlib import Path
from urllib.parse import urlparse

import requests
import telegram


def get_file_extension(url):
    parts_url = urlparse(url)
    path = parts_url.path
    basename = os.path.basename(path)
    splitted_path = splitext(basename)
    extension = splitted_path[1]
    return extension


def fetch_image(url, filename, url_number, extension, api_key=None):
    path = Path('images')
    path.mkdir(parents=True, exist_ok=True)
    params = {'api_key': api_key}
    filepath = path / f'{filename}_{url_number}{extension}'
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)


def publish_photo_bot(channel_id, tg_token,
                      image_to_publish,
                      image_directory):

    bot = telegram.Bot(token=tg_token)
    image_path = os.path.join(image_directory, image_to_publish)

    with open(image_path, 'rb') as photo:
        bot.send_photo(chat_id=channel_id,
                       photo=photo)

    return image_to_publish
