import argparse
import os
import requests

from dotenv import load_dotenv

from utils import fetch_spacex_last_launch


def get_url_spacex(id):
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    response.raise_for_status
    info = response.json()
    links = info['links']
    flickr = links['flickr']
    images = flickr['original']
    return images


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--lauch_id',
                        help='The lauch ID to use.',
                        default=os.environ.get('LAUNCH_ID'))

    args = parser.parse_args()

    lauch_id = args.lauch_id
    fetch_spacex_last_launch(get_url_spacex(lauch_id))


if __name__ == '__main__':
    main()
