import argparse
import os
import random
import time

import requests
import telegram
from dotenv import load_dotenv


def publish_photo_bot(channel_id, tg_token, image):
    bot = telegram.Bot(token=tg_token)
    image_directory = 'images'
    if image:
        image_to_publish = image
    else:
        images = os.walk(image_directory)
        for _, _, files in images:
            image = files
        image_to_publish = random.choice(image)

    image_path = os.path.join(image_directory, image_to_publish)
    bot.send_photo(chat_id=channel_id,
                   photo=open(image_path, 'rb'))


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--image',
                        help='The image to use.')

    args = parser.parse_args()

    image = args.image

    tg_token = os.environ.get('TELEGRAM_TOKEN_FOR_BOT')
    channel_id = os.environ.get('TELEGRAM_CHANNEL_ID')

    max_retries = 5
    retry_count = 0

    try:
        publish_photo_bot(channel_id, tg_token, image)
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


if __name__ == '__main__':
    main()
