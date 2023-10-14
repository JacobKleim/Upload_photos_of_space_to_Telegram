import argparse
import os
import random

from dotenv import load_dotenv

from utils import publish_photo_bot


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='The path to the image file'
                    'you want to publish on Telegram.',
    )

    parser.add_argument(
        '-i', '--image',
        help='The image to use.')

    args = parser.parse_args()

    image = args.image

    tg_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    channel_id = os.environ.get('TELEGRAM_CHANNEL_ID')

    image_directory = 'images'

    if image:
        image_to_publish = image
    else:
        images = os.walk(image_directory)
        for _, _, files in images:
            image = files
        image_to_publish = random.choice(image)

    publish_photo_bot(channel_id, tg_token, image_to_publish, image_directory)


if __name__ == '__main__':
    main()
