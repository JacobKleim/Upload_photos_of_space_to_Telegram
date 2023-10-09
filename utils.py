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


def fetch_spacex_last_launch(urls, filename):
    path = Path("images")
    path.mkdir(parents=True, exist_ok=True)
    params = {'api_key': 'MYyGVtySmAkcUE1YrfZHTTSKbhf09dbXruwo0HrW'}
    for url_number, url in enumerate(urls):
        extension = get_file_extension(url)
        if not extension or extension == "":
            pass
        filepath = path / f'{filename}_{url_number}{extension}'
        response = requests.get(url, params=params)
        response.raise_for_status()

        with open(filepath, 'wb') as file:
            file.write(response.content)
