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


def fetch_image(url, filename, url_number, extension, api_key=None):
    path = Path('images')
    path.mkdir(parents=True, exist_ok=True)
    params = {'api_key': api_key}
    filepath = path / f'{filename}_{url_number}{extension}'
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)
