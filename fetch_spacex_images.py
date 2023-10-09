import argparse
import os

import requests
from dotenv import load_dotenv

from utils import fetch_spacex_last_launch


def get_urls_spacex_launch_image(id):
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    response.raise_for_status
    info = response.json()
    images = info['links']['flickr']
    images_url = images['original']
    return images_url


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--lauch_id',
                        help='The lauch ID to use.',
                        default=os.environ.get('LAUNCH_ID'))

    args = parser.parse_args()

    filename = 'spacex'

    lauch_id = args.lauch_id

    fetch_spacex_last_launch(get_urls_spacex_launch_image(lauch_id), filename)


if __name__ == '__main__':
    main()
