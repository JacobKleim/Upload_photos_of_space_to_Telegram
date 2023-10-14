import argparse
import os
import random
import time

from dotenv import load_dotenv

from utils import publish_photo_bot


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

    images_to_publish = []
    image_directory = 'images'

    while True:
        if not images_to_publish:
            images = os.walk(image_directory)
            for _, _, files in images:
                images_to_publish = [*files]
            random.shuffle(images_to_publish)

        image_to_publish = images_to_publish.pop(0)

        publish_photo_bot(channel_id, tg_token,
                          image_to_publish, image_directory)

        time.sleep(publication_frequency)


if __name__ == '__main__':
    main()
