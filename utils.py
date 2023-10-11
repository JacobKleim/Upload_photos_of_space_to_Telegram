import os
from os.path import splitext
from pathlib import Path
from urllib.parse import urlparse

import requests


def get_file_extension(url):
    parts_url = urlparse(url)
    path = parts_url.path
    basename = os.path.basename(path)
    splitted_path = splitext(basename)
    extension = splitted_path[1]
    return extension


def is_extension(extension):
    if not extension or extension == '':
        return False
    else:
        return True


def fetch_image(url, url_number, filename, api_key):
    path = Path('images')
    path.mkdir(parents=True, exist_ok=True)
    params = {'api_key': api_key}
    extension = get_file_extension(url)
    if is_extension(extension):
        filepath = path / f'{filename}_{url_number}{extension}'
        response = requests.get(url, params=params)
        response.raise_for_status()

        with open(filepath, 'wb') as file:
            file.write(response.content)


def fetch_images(urls, filename, api_key=None):
    for url_number, url in enumerate(urls):
        fetch_image(url, url_number, filename, api_key)
