import argparse
import os
import random

import telegram
from dotenv import load_dotenv


def publish_photo_bot(channel_id, tg_token, image_to_publish, image_directory):
    bot = telegram.Bot(token=tg_token)
    image_path = os.path.join(image_directory, image_to_publish)
    with open(image_path, 'rb') as photo:
        bot.send_photo(chat_id=channel_id,
                       photo=photo)


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
