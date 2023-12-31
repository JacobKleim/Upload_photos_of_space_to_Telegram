import argparse
import os

import requests
from dotenv import load_dotenv

from utils import fetch_image, get_file_extension


def get_urls_spacex_launch_image(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    launch = response.json()
    images = launch['links']['flickr']
    images_url = images['original']
    return images_url


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='Fetches images related to SpaceX launches'
                    'using a specified launch ID as a command-line argument.'
        )

    parser.add_argument(
        '-l', '--lauch_id',
        help='The lauch ID to use.',
        default=os.environ.get('LAUNCH_ID'))

    args = parser.parse_args()

    filename = 'spacex'

    lauch_id = args.lauch_id

    for url_number, url in enumerate(get_urls_spacex_launch_image(lauch_id)):
        extension = get_file_extension(url)
        if extension:
            fetch_image(url, filename, url_number, extension, api_key=None)


if __name__ == '__main__':
    main()
