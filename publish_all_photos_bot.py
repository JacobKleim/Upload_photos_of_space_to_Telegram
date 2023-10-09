import argparse
import os
import random
import time

import requests
import telegram
from dotenv import load_dotenv


def publish_all_photos_bot(channel_id, tg_token, images):

    bot = telegram.Bot(token=tg_token)
    image_directory = 'images'

    if not images:
        images = os.walk(image_directory)
        for _, _, files in images:
            images = files
        random.shuffle(images)

    image_to_publish = images.pop(0)
    image_path = os.path.join(image_directory, image_to_publish)
    bot.send_photo(chat_id=channel_id,
                   photo=open(image_path, 'rb'))

    return images


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--publication_frequency',
                        type=int,
                        help='The publication_frequency to use.',
                        default=os.environ.get('PUBLICATION_FREQUENCY'))

    args = parser.parse_args()

    publication_frequency = int(args.publication_frequency)

    tg_token = os.environ.get('BOT_TELEGRAM_TOKEN')
    channel_id = os.environ.get('TELEGRAM_CHANNEL_ID')

    max_retries = 5
    retry_count = 0

    images = []

    while True:
        try:
            images = publish_all_photos_bot(channel_id, tg_token, images)
            retry_count = 0
        except ConnectionError as con_error:
            print(con_error)
            retry_count += 1
            if retry_count >= max_retries:
                time.sleep(30)
                retry_count = 0
        except requests.exceptions.ReadTimeout as rt_error:
            print(rt_error)
        except Exception as e:
            print(e)

        time.sleep(publication_frequency)


if __name__ == '__main__':
    main()
