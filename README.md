# Upload_photos_of_space_to_Telegram

# Project Description
 - The program consists of several scripts and can upload Astronomy Picture of the Day(apod) photos, Earth Polychromatic Imaging Camera (epic) from NASA and shuttle launch photos from SpaceX. The files are uploaded to the "images" folder. If it is not there, it is automatically created in your repository.
 - The program also has two scripts for posting photos to Telegram:
1. 'publish_photo_bot' can send the selected photo to the chat. If no photo is selected, a random photo from the storage will be sent. 
2. 'publish_all_photos_bot' sends a random photo from the repository to the chat after a specified period of time. If the time interval is not specified, the photo will be sent according to the default time interval

## Technologies and tools
 - Python 3.9.10

## How to use
1. Clone this repository and go to the project folder:
   ```bash
   cd /c/project_folder # for example
   ```
   ```bash
   git clone git@github.com:JacobKleim/Upload_photos_of_space_to_Telegram.git
   ```
   ```bash
   cd /c/project_folder/Upload_photos_of_space_to_Telegram 
   ```

2. Create a .env file with parameters:
   ```
   LAUNCH_ID=default spacex launch id for downloading photos
   ```
   ```
   TELEGRAM_TOKEN=token for your bot
   ```
   ```
   TELEGRAM_CHANNEL_ID=id of your Telegram channel or chat
   ```
   ```
   PUBLICATION_FREQUENCY=the default time interval for sending photos
   ```

3. Сreate and activate a virtual environment:
   ```
   python -m venv venv
   ```
   ```bash
   source venv/Scripts/activate
   ```

4. Install dependencies:
   ```
   python -m pip install --upgrade pip
   ```
   ```
   pip install -r requirements.txt
   ```

5. Start the project:
   If you want to use your SpaceX startup ID, then specify it when running the script:
   ```
   python fetch_nasa_apod_images.py -l 5eb87d47ffd86e000604b38a
   ```
   If you want to use the default identifier that indicates the last launch of SpaceX, then run the script without parameters:
   ```
   python fetch_nasa_apod_images.py
   ```
   To download EPIC images from NASA, use the following command:
   ```
   python fetch_nasa_epic_images.py
   ```
   To download APOD images from NASA, use the following command:
   ```
   python fetch_apod_images.py
   ```
   If you want to send an image to the telegram channel, then specify its name:
   ```
   python publish_photo_bot.py -i spacex_1.jpg (specify your file name)
   ```
   If you want to send a random image, then run without parameters:
   ```
   python publish_photo_bot.py
   ```
   python If you want to launch a bot with the specified time interval, then specify the duration in seconds as an integer:
   ```
   python publish_all_photos_bot.py -p 100
   ```
   If you want to run the bot with the default time interval, then run the script without parameters:
   ```
   python publish_all_photos_bot.py
   ```



## Example of work
 
![tg](https://github.com/JacobKleim/Upload_photos_of_space_to_Telegram/assets/119351169/ab15c6c9-79a1-4df5-b4f0-5284683e4bf3)
