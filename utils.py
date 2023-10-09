import os
import requests
from pathlib import Path
from urllib.parse import urlparse
from os.path import splitext


def get_filename_and_extension(url):
    parts_url = urlparse(url)
    path = parts_url.path
    basename = os.path.basename(path)
    print(basename)
    splitted_path = splitext(basename)
    filename = splitted_path[0]
    print(filename)
    extension = splitted_path[1]
    print(extension)
    return filename, extension


def fetch_spacex_last_launch(urls):
    path = Path("images")
    path.mkdir(parents=True, exist_ok=True)
    params = {'api_key': 'MYyGVtySmAkcUE1YrfZHTTSKbhf09dbXruwo0HrW'}
    for url_number, url in enumerate(urls):
        filename, extension = get_filename_and_extension(url)
        # print(filename)
        filepath = path / f'{filename}_{url_number}{extension}'
        response = requests.get(url, params=params)
        response.raise_for_status()

        with open(filepath, 'wb') as file:
            file.write(response.content)
