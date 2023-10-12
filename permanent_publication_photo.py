import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def permanent_publication_photo(channel_id, tg_token, images, image_directory):
    bot = telegram.Bot(token=tg_token)
    image_to_publish = images.pop(0)
    image_path = os.path.join(image_directory, image_to_publish)
    with open(image_path, 'rb') as photo:
        bot.send_photo(chat_id=channel_id,
                       photo=photo)

    return images


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='Manages a Telegram bot that publishes images'
                    'to a Telegram channel, with control over'
                    'the publication frequency as a command-line argument.'
    )

    parser.add_argument(
        '-p', '--publication_frequency',
        type=int,
        help='The publication_frequency to use.',
        default=os.environ.get('PUBLICATION_FREQUENCY'))

    args = parser.parse_args()

    publication_frequency = int(args.publication_frequency)

    tg_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    channel_id = os.environ.get('TELEGRAM_CHANNEL_ID')

    images = []
    image_directory = 'images'

    while True:
        if not images:
            images = os.walk(image_directory)
            for _, _, files in images:
                images = files
            random.shuffle(images)

        images = permanent_publication_photo(channel_id, tg_token,
                                             images, image_directory)

        time.sleep(publication_frequency)


if __name__ == '__main__':
    main()
